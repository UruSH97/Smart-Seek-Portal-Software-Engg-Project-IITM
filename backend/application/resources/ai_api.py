from flask_restful import (
    Resource,
    fields,
    marshal_with,
    reqparse,
    marshal,
    abort
)
from application.database import db
from ..models import (
    Course,
    VirtualInstructorQuery,
    InstructorContentPlanner,
    StudentCuration,
    User,
    Enrollment
)
from sqlalchemy.exc import SQLAlchemyError 
import marko
import google.generativeai as genai
import textwrap

GOOGLE_API_KEY = 'AIzaSyAZCfPg4CG778dEtoWW4BwDICXjven5u-k'
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable")

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)



safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              safety_settings=safety_settings)

##########Virtual Instructer#######################################################################
vi_parser = reqparse.RequestParser()
# Add arguments to the parser
vi_parser.add_argument('student_id', type=str, required=True, help="Student ID is required")
vi_parser.add_argument('course_id', type=str, required=True, help="Course ID is required")
vi_parser.add_argument('gen_query_text', type=str, required=True, help="Query is required")


# Define user fields for the parser
vi_fields = {
    'id': fields.String,
    'student_id': fields.String,
    'course_id': fields.String,
    'gen_query': fields.String,
    'response': fields.String,
    'created_at': fields.DateTime
}


class VirtualInstructorQueryResource(Resource):
    def get(self, course_id, student_id):
        queries = VirtualInstructorQuery.query.filter_by(course_id=course_id, student_id=student_id).order_by(VirtualInstructorQuery.created_at).all()
        if not queries:
            return [], 200
        formatted_queries =[
            marshal(vi, vi_fields) for vi in queries
        ]
        return formatted_queries, 200

    @marshal_with(vi_fields)
    def post(self):
        args = vi_parser.parse_args()
        student_id = args['student_id']
        course_id = args['course_id']
        gen_query_text = args['gen_query_text']
        
        course = Course.query.filter_by(id=course_id).first()
        if not course:
            abort(404, message="Course not found")
        
        prompt = f"Please answer the following question with respect to the subject {course.title}: {gen_query_text} within 250 words"

        response = model.generate_content(prompt)

        new_query = VirtualInstructorQuery(
            student_id=student_id,
            course_id=course_id,
            gen_query=gen_query_text,
            response=to_markdown(response.text)
        )

        try:
            db.session.add(new_query)
            db.session.commit()
            return new_query, 201
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Error saving query to the database")
            
    def delete(self, course_id, student_id):
        print(f"Attempting to delete queries for course_id: {course_id}, student_id: {student_id}")
        try:
            # Debug: List available attributes of the model
            # print(f"Attributes of VirtualInstructorQuery: {dir(VirtualInstructorQuery)}")
            
            deleted_count = VirtualInstructorQuery.query.filter_by(course_id = course_id, student_id = student_id).delete()
            db.session.commit()
            if deleted_count == 0:
                return {'message': 'No queries found to delete'}, 404
            return {'message': 'All queries deleted'}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error: {e}")
            abort(500, message="Error deleting queries from the database")
######################## End of API ###############################################################


##########Instructer content planner API#######################################################################
# Add arguments to the parser
icp_parser = reqparse.RequestParser()
icp_parser.add_argument('instructor_id', type=str, help="Instructor ID is required")
icp_parser.add_argument('course_id', type=str, help="Course ID is required")
icp_parser.add_argument('gen_query_text', type=str, help="Query is required")
icp_parser.add_argument('content_type', type=str, help="Content type is required")
icp_parser.add_argument('difficulty_level', type=str,help="Difficulty level is required")

# Define fields for the parser
icp_fields = {
    'id': fields.String,
    'instructor_id': fields.String,
    'course_id': fields.String,
    'content_type': fields.String,
    'gen_query_text': fields.String,
    'gen_ai_resources': fields.String,
    'gen_ai_questions': fields.String,
    'gen_ai_answers': fields.String,
    'gen_ai_question_detail': fields.String,
    'difficulty_level': fields.String,
}

class InstructorContentPlannerResource(Resource):
    def get(self, instructor_id, course_id, content_type):
        contents = InstructorContentPlanner.query.filter_by(instructor_id=instructor_id, course_id=course_id).all()
        if not contents:
            return [], 200
        
        formatted_contents = []
        if content_type == 'resource' :
            for content in contents:
                if content.content_type == 'resource':
                    formatted_contents.append({
                        "id" : content.id,
                        'content_type': 'resource',
                        'gen_query_text' : content.gen_query_text,
                        'gen_ai_resources': content.gen_ai_resources,
                        'difficulty_level': content.difficulty_level,
                    })
            return formatted_contents, 200
        else:
            for content in contents:
                if content.content_type == 'question':
                    formatted_contents.append({
                        "id" : content.id,
                        'content_type': 'question',
                        'gen_query_text': content.gen_query_text,
                        'gen_ai_questions': content.gen_ai_questions,
                        'gen_ai_answers': content.gen_ai_answers,
                        'gen_ai_question_detail': content.gen_ai_question_detail,
                        'difficulty_level': content.difficulty_level,
                    })
            return formatted_contents, 200
        

    @marshal_with(icp_fields)
    def post(self):
        args = icp_parser.parse_args()
        instructor_id = args['instructor_id']
        course_id = args['course_id']
        gen_query_text = args['gen_query_text']
        content_type = args['content_type']
        difficulty_level = args['difficulty_level']

        course = Course.query.filter_by(id=course_id).first()
        if not course:
            abort(404, message="Course not found")
        
        course_title = course.title
        course_description = course.description

        if content_type == 'resource':
            prompt = f"With reference to {course_title} which has this {course_description} generate notes on the following topic {gen_query_text} with {difficulty_level} difficulty level."
            response = model.generate_content(prompt)
            new_content = InstructorContentPlanner(
                instructor_id=instructor_id,
                gen_query_text = gen_query_text,
                course_id=course_id,
                content_type='resource',
                gen_ai_resources=to_markdown(response.text),
                difficulty_level=difficulty_level
            )
        elif content_type == 'question':
            question_prompt = f"With reference to {course_title} which has this {course_description} generate 1 True/False question on the following topic {gen_query_text} with {difficulty_level} difficulty level."
            question_response = model.generate_content(question_prompt)

            answer_prompt = f"With reference to {course_title} which has this {course_description} generate 1 True/False answer in one word only on the following topic {to_markdown(question_response.text)} with {difficulty_level} difficulty level."
            answer_response = model.generate_content(answer_prompt)

            description_prompt = f"With reference to {course_title} which has this {course_description} generate question solution description on the following topic {to_markdown(question_response.text)} with {difficulty_level} difficulty level n 250 words."
            description_response = model.generate_content(description_prompt)

            new_content = InstructorContentPlanner(
                instructor_id=instructor_id,
                course_id=course_id,
                content_type='question',
                gen_query_text=gen_query_text,
                gen_ai_questions=to_markdown(question_response.text),
                gen_ai_answers=to_markdown(answer_response.text),
                gen_ai_question_detail=to_markdown(description_response.text),
                difficulty_level=difficulty_level
            )
        else:
            abort(400, message="Invalid content type")

        try:
            db.session.add(new_content)
            db.session.commit()
            return new_content, 201
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Error saving content to the database")

    def delete(self, query_id):
            content = InstructorContentPlanner.query.filter_by(id=query_id).first()
            if not content:
                return {'message': 'Content not found'}, 404

            try:
                db.session.delete(content)
                db.session.commit()
                return {'message': 'Content deleted successfully'}, 200
            except SQLAlchemyError as e:
                db.session.rollback()
                abort(500, message="Error deleting content from the database")

######################## End of API ###############################################################

#########Student Planner #########################################################################
student_planner_fields = {
    'id': fields.Integer,
    'student_id': fields.String,
    'response': fields.String,
    'level': fields.String,
    'content_type': fields.String,
    'gen_query': fields.String,
}

# Define arguments for the parser
sp_parser = reqparse.RequestParser()
sp_parser.add_argument('student_id', type=str, required=True, help="Student ID is required")
sp_parser.add_argument('level', type=str,help="Level is required")
sp_parser.add_argument('content_type', type=str, help="Content type is required")
sp_parser.add_argument('gen_query', type=str,help="Gen query is required")

class StudentPlannerResource(Resource):
    @marshal_with(student_planner_fields)
    def get(self):
        args = sp_parser.parse_args()
        student_id = args['student_id']
        content_type = args['content_type']

        curations = StudentCuration.query.filter_by(student_id=student_id, content_type=content_type).first()
        if not curations:
            return [], 200

        return curations, 200

    @marshal_with(student_planner_fields)
    def post(self):
        args = sp_parser.parse_args()
        student_id = args['student_id']
        level = args['level']
        content_type = args['content_type']
        gen_query = args['gen_query']


        student = User.query.filter_by(id=student_id).first()
        if not student:
            abort(404, message="Student not found")

        enrolled_courses = Enrollment.query.filter_by(student_id=student_id).all()
        course_titles = [Course.query.filter_by(id=enrollment.course_id).first().title for enrollment in enrolled_courses]

        if not course_titles:
            abort(404, message="No enrolled courses found for the student")

        prompt = f"For a student of BS Degree in Data Science And Programming with courses {', '.join(course_titles)}  at {level} give me {content_type} and {gen_query} optimized within 500 words."
        response = model.generate_content(prompt)  # Assuming there's a model to generate the content

        new_curation = StudentCuration(
            student_id=student_id,
            response=to_markdown(response.text),
            level=level,
            content_type=content_type,
            gen_query=gen_query
        )

        try:
            db.session.add(new_curation)
            db.session.commit()
            return new_curation, 201
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Error saving curation to the database")

    def delete(self, query_id):
        curation = StudentCuration.query.filter_by(id=query_id).first()
        if not curation:
            return {'message': 'Curation not found'}, 404

        try:
            db.session.delete(curation)
            db.session.commit()
            return {'message': 'Curation deleted successfully'}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Error deleting curation from the database")

######################## End of API ###############################################################
