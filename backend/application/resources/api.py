from flask_restful import (
    Resource,
    fields,
    marshal_with,
    reqparse,
    marshal
    
)
from application.database import db
from ..models import (
    Course,
    Enrollment,
    Module,
    Note,
    Lecture,
    Assignment,
    ProgrammingAssignment,
    TestCase,
    RolesUsers,
    Question,
    Submission,
    VirtualInstructorQuery,
    InstructorContentPlanner,
    CourseStatistics,
    AdminCourseManagement,
    StudentDetailsManagement,
    AssignmentStatus
)

course_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'instructor_id': fields.Integer
}


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
}

enrollment_fields = {
    'id': fields.Integer,
    'student_id': fields.String,
    'course_id': fields.String
}

module_fields = {
    'id': fields.Integer,
    'course_id': fields.String,
    'title': fields.String,
    'description': fields.String,
    'week': fields.Integer
}

note_fields = {
    'id': fields.String,
    'course_id': fields.String,
    'title': fields.String,
    'content': fields.String,
    'pdflink': fields.String
}

lecture_fields = {
    'id': fields.String,
    'module_id': fields.String,
    'title': fields.String,
    'content': fields.String
}

assignment_fields = {
    'id': fields.String,
    'title': fields.String,
    'description': fields.String
}

programming_assignment_fields = {
    'id': fields.String,
    'modules_id':fields.String,
    'p_question': fields.String,
    'editor_content':fields.String,
    'sandbox_environment': fields.String
}

test_case_fields = {
    'id': fields.String,
    'programming_assignment_id': fields.String,
    'input': fields.String,
    'expected_output': fields.String
}

question_fields = {
    'id': fields.String,
    'assignment_id': fields.String,
    'question_text': fields.String,
    'options': fields.String,
    'marks': fields.Integer,
    'correct_answer': fields.String
}

submission_fields = {
    'id': fields.String,
    'assignment_id': fields.String,
    'student_id': fields.String
}

virtual_instructor_query_fields = {
    'id': fields.String,
    'student_id': fields.String,
    'query': fields.String
}

instructor_content_planner_fields = {
    'id': fields.String,
    'course_id': fields.String
}

course_statistics_fields = {
    'id': fields.String,
    'course_id': fields.String
}


class CourseResource(Resource):
    def __init__(self):
            self.parser = reqparse.RequestParser()
            self.parser.add_argument('title', type=str, required=True)
            self.parser.add_argument('description', type=str, required=True)
            self.parser.add_argument('instructorId', type=int, help='Instructor ID is required')

    def get(self, course_id=None):
        if course_id == None:
            courses = Course.query.all()
            if not courses:
                return [], 200
            formatted_courses =[
                marshal(cour, course_fields) for cour in courses
            ]
            return formatted_courses, 200
        course = Course.query.get(course_id)
        if course:
            return marshal(course, course_fields)
        else:
            return {'message': 'Course not found'}, 404

    @marshal_with(course_fields)
    def post(self):
        args = self.parser.parse_args()
        course = Course(title=args['title'], description=args['description'], instructor_id=args['instructorId'])
        db.session.add(course)
        db.session.commit()
        return course, 201

    @marshal_with(course_fields)
    def put(self, course_id):
        course = Course.query.get(course_id)
        if course:
            args = self.parser.parse_args()
            course.title = args['title']
            course.description = args['description']
            db.session.commit()
            return course
        else:
            return {'message': 'Course not found'}, 404

    def delete(self, course_id):
        course = Course.query.get(course_id)
        if course:
            db.session.delete(course)
            db.session.commit()
            return {'message': 'Course deleted'}
        else:
            return {'message': 'Course not found'}, 404


class EnrollmentResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('student_id', type = str, required = True)
        self.parser.add_argument('course_id', type = str, required = True)
        self.parser.add_argument(
            'enrollment_date', type = str, required = True)
        self.parser.add_argument('status', type = str, required = True)

    @marshal_with(enrollment_fields)
    def get(self, enrollment_id):
        enrollment = Enrollment.query.get(enrollment_id)
        if enrollment:
            return enrollment
        else:
            return {'message': 'Enrollment not found'}, 404

    @marshal_with(enrollment_fields)
    def post(self):
        args = self.parser.parse_args()
        enrollment = Enrollment(student_id = args['student_id'], course_id = args['course_id'],
                                enrollment_date = args['enrollment_date'], status = args['status'])
        db.session.add(enrollment)
        db.session.commit()
        return enrollment, 201

    @marshal_with(enrollment_fields)
    def put(self, enrollment_id):
        enrollment = Enrollment.query.get(enrollment_id)
        if enrollment:
            args = self.parser.parse_args()
            enrollment.student_id = args['student_id']
            enrollment.course_id = args['course_id']
            enrollment.enrollment_date = args['enrollment_date']
            enrollment.status = args['status']
            db.session.commit()
            return enrollment
        else:
            return {'message': 'Enrollment not found'}, 404

    def delete(self, enrollment_id):
        enrollment = Enrollment.query.get(enrollment_id)
        if enrollment:
            db.session.delete(enrollment)
            db.session.commit()
            return {'message': 'Enrollment deleted'}
        else:
            return {'message': 'Enrollment not found'}, 404


class ModuleResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('course_id', type=str)
        self.parser.add_argument('title', type = str, required = True)
        self.parser.add_argument(
            'description', type = str, required = True)
        self.parser.add_argument('week', type = int)

    def get(self, module_id=None):
        if module_id is None:
            modules = Module.query.all()
            if not modules:
                    return [], 200
            formatted_modules =[
                marshal(mod, module_fields) for mod in modules
            ]
            return formatted_modules, 200
        module = Module.query.get(module_id)
        if module:
            return marshal(module, module_fields)
        else:
            return {'message': 'Module not found'}, 404

    @marshal_with(module_fields)
    def post(self):
        args = self.parser.parse_args()
        module = Module(course_id = args['course_id'], title = args['title'], description = args['description'],
                        week = args['week'])
        db.session.add(module)
        db.session.commit()
        return module, 201

    @marshal_with(module_fields)
    def put(self, module_id):
        module = Module.query.get(module_id)
        if module:
            args = self.parser.parse_args()
            module.title = args['title']
            module.description = args['description']
            module.week = args['week']
            db.session.commit()
            return module
        else:
            return {'message': 'Module not found'}, 404

    def delete(self, module_id):
        module = Module.query.get(module_id)
        if module:
            db.session.delete(module)
            db.session.commit()
            return {'message': 'Module deleted'}
        else:
            return {'message': 'Module not found'}, 404

#use this done
class LectureResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('module_id', type = str, required = True)
        self.parser.add_argument('title', type = str, required = True)
        self.parser.add_argument('content', type = str, required = True)

    def get(self, lecture_id=None):
        if lecture_id is None:
            lectures = Lecture.query.all()
            if not lectures:
                    return [], 200
            formatted_lectures =[
                marshal(lec, lecture_fields) for lec in lectures
            ]
            return formatted_lectures, 200
        lecture = Lecture.query.get(lecture_id)
        if lecture:
            return marshal(lecture, module_fields)
        else:
            return {'message': 'Module not found'}, 404

    @marshal_with(lecture_fields)
    def post(self):
        args = self.parser.parse_args()
        lecture = Lecture(
            module_id=args['module_id'], title=args['title'], content=args['content'])
        db.session.add(lecture)
        db.session.commit()
        return lecture, 201

    @marshal_with(lecture_fields)
    def put(self, lecture_id):
        lecture = Lecture.query.get(lecture_id)
        if lecture:
            args = self.parser.parse_args()
            lecture.module_id = args['module_id']
            lecture.title = args['title']
            lecture.content = args['content']
            db.session.commit()
            return lecture
        else:
            return {'message': 'Lecture not found'}, 404

    def delete(self, lecture_id):
        lecture = Lecture.query.get(lecture_id)
        if lecture:
            db.session.delete(lecture)
            db.session.commit()
            return {'message': 'Lecture deleted'}
        else:
            return {'message': 'Lecture not found'}, 404


class NoteResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('course_id', type=str, required=True)
        self.parser.add_argument('title', type=str, required=True)
        self.parser.add_argument('content', type=str, required=True)
        self.parser.add_argument('pdflink', type=str)

    def get(self, note_id=None):
        if note_id is None:
            notes = Note.query.all()
            if not notes:
                    return [], 200
            formatted_notes =[
                marshal(note, note_fields) for note in notes
            ]
            return formatted_notes, 200
        note = Note.query.get(note_id)
        if note:
            return marshal(note, note_fields)
        else:
            return {'message': 'Note not found'}, 404

    @marshal_with(note_fields)
    def post(self):
        args = self.parser.parse_args()
        note = Note(course_id=args['course_id'],
                    title=args['title'], content=args['content'], pdflink=args['pdflink'])
        db.session.add(note)
        db.session.commit()
        return note, 201

    @marshal_with(note_fields)
    def put(self, note_id):
        note = Note.query.get(note_id)
        if note:
            args = self.parser.parse_args()
            note.title = args['title']
            note.content = args['content']
            note.pdflink = args['pdflink']
            db.session.commit()
            return note, 201
        else:
            return {'message': 'Note not found'}, 404

    def delete(self, note_id):
        note = Note.query.get(note_id)
        if note:
            db.session.delete(note)
            db.session.commit()
            return {'message': 'Note deleted'}
        else:
            return {'message': 'Note not found'}, 404

#uselesss
class AssignmentResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, required=True)
        self.parser.add_argument('description', type=str, required=True)

    @marshal_with(assignment_fields)
    def get(self, assignment_id):
        assignment = Assignment.query.get(assignment_id)
        if assignment:
            return assignment
        else:
            return {'message': 'Assignment not found'}, 404

    @marshal_with(assignment_fields)
    def post(self):
        args = self.parser.parse_args()
        assignment = Assignment(
            title=args['title'], description=args['description'])
        db.session.add(assignment)
        db.session.commit()
        return assignment, 201

    @marshal_with(assignment_fields)
    def put(self, assignment_id):
        assignment = Assignment.query.get(assignment_id)
        if assignment:
            args = self.parser.parse_args()
            assignment.title = args['title']
            assignment.description = args['description']
            db.session.commit()
            return assignment
        else:
            return {'message': 'Assignment not found'}, 404

    def delete(self, assignment_id):
        assignment = Assignment.query.get(assignment_id)
        if assignment:
            db.session.delete(assignment)
            db.session.commit()
            return {'message': 'Assignment deleted'}
        else:
            return {'message': 'Assignment not found'}, 404

#use this
class ProgrammingAssignmentResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('module_id', type=str, required=True)
        self.parser.add_argument('p_question', type=str)

    @marshal_with(programming_assignment_fields)
    def get(self, programming_assignment_id=None):
        if programming_assignment_id is None:
            programming_assignments = ProgrammingAssignment.query.all()
            if not programming_assignments:
                    return [], 200
            formatted_programming_assignments =[
                marshal(p, programming_assignment_fields) for p in programming_assignments
            ]
            return formatted_programming_assignments , 200
        p = ProgrammingAssignment.query.get(programming_assignment_id)
        if p:
            return marshal(p, programming_assignment_fields)
        else:
            return {'message': 'Module not found'}, 404

    @marshal_with(programming_assignment_fields)
    def post(self):
        args = self.parser.parse_args()
        programming_assignment = ProgrammingAssignment(
            assignment_id=args['module_id'], language=args['p_question'])
        db.session.add(programming_assignment)
        db.session.commit()
        return programming_assignment, 201

    @marshal_with(programming_assignment_fields)
    def put(self, programming_assignment_id):
        programming_assignment = ProgrammingAssignment.query.get(
            programming_assignment_id)
        if programming_assignment:
            args = self.parser.parse_args()
            programming_assignment.assignment_id = args['assignment_id']
            programming_assignment.language = args['language']
            db.session.commit()
            return programming_assignment
        else:
            return {'message': 'Programming Assignment not found'}, 404

    def delete(self, programming_assignment_id):
        programming_assignment = ProgrammingAssignment.query.get(
            programming_assignment_id)
        if programming_assignment:
            db.session.delete(programming_assignment)
            db.session.commit()
            return {'message': 'Programming Assignment deleted'}
        else:
            return {'message': 'Programming Assignment not found'}, 404

# usethis
class TestCaseResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('programming_assignment_id', type=str, required=True)
        self.parser.add_argument('input', type=str)
        self.parser.add_argument('expected_output', type=str)

    @marshal_with(test_case_fields)
    def get(self):
        test_cases = TestCase.query.all()
        if not test_cases:
                return [], 200
        formatted_test_cases =[
            marshal(t, test_case_fields) for t in test_cases
            ]
        return formatted_test_cases , 200

    @marshal_with(test_case_fields)
    def post(self):
        args = self.parser.parse_args()
        test_case = TestCase(
            assignment_id=args['programming_assignment_id'], input=args['input'], output=args['expected_output'])
        db.session.add(test_case)
        db.session.commit()
        return test_case, 201

    @marshal_with(test_case_fields)
    def put(self, test_case_id):
        test_case = TestCase.query.get(test_case_id)
        if test_case:
            args = self.parser.parse_args()
            test_case.assignment_id = args['programming_assignment_id']
            test_case.input = args['input']
            test_case.output = args['expected_output']
            db.session.commit()
            return test_case
        else:
            return {'message': 'Test Case not found'}, 404

    def delete(self, test_case_id):
        test_case = TestCase.query.get(test_case_id)
        if test_case:
            db.session.delete(test_case)
            db.session.commit()
            return {'message': 'Test Case deleted'}
        else:
            return {'message': 'Test Case not found'}, 404

#usethis done
class QuestionResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('module_id', type=str, required=True)
        self.parser.add_argument('question_text', type=str)
        self.parser.add_argument('options', type=str)
        self.parser.add_argument('correct_answer', type=str)
        self.parser.add_argument('marks', type=str)

    def get(self, question_id=None):
        if question_id is None:
            questions = Question.query.all()
            if not questions:
                    return [], 200
            formatted_questions =[
                marshal(q, question_fields) for q in questions
            ]
            return formatted_questions, 200
        question = Question.query.get(question_id)
        if question:
            return marshal(question, question_fields)
        else:
            return {'message': 'Module not found'}, 404

    @marshal_with(question_fields)
    def post(self):
        args = self.parser.parse_args()
        question = Question(
            assignment_id=args['assignment_id'], question_text=args['question_text'], options = args['options'], correct_answer=args['correct_answer'], marks=args['marks'])
        db.session.add(question)
        db.session.commit()
        return question, 201

    @marshal_with(question_fields)
    def put(self, question_id):
        question = Question.query.get(question_id)
        if question:
            args = self.parser.parse_args()
            question.assignment_id = args['assignment_id']
            question.question_text = args['question_text']
            question.correct_answer= args['correct_answer']
            question.marks = args['marks']
            question.options = args['options']
            db.session.commit()
            return question
        else:
            return {'message': 'Question not found'}, 404

    def delete(self, question_id):
        question = Question.query.get(question_id)
        if question:
            db.session.delete(question)
            db.session.commit()
            return {'message': 'Question deleted'}
        else:
            return {'message': 'Question not found'}, 404


class SubmissionResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('assignment_id', type=str, required=True)
        self.parser.add_argument('student_id', type=str, required=True)

    @marshal_with(submission_fields)
    def get(self, submission_id):
        submission = Submission.query.get(submission_id)
        if submission:
            return submission
        else:
            return {'message': 'Submission not found'}, 404

    @marshal_with(submission_fields)
    def post(self):
        args = self.parser.parse_args()
        submission = Submission(
            assignment_id=args['assignment_id'], student_id=args['student_id'])
        db.session.add(submission)
        db.session.commit()
        return submission, 201

    @marshal_with(submission_fields)
    def put(self, submission_id):
        submission = Submission.query.get(submission_id)
        if submission:
            args = self.parser.parse_args()
            submission.assignment_id = args['assignment_id']
            submission.student_id = args['student_id']
            db.session.commit()
            return submission
        else:
            return {'message': 'Submission not found'}, 404

    def delete(self, submission_id):
        submission = Submission.query.get(submission_id)
        if submission:
            db.session.delete(submission)
            db.session.commit()
            return {'message': 'Submission deleted'}
        else:
            return {'message': 'Submission not found'}, 404


class CourseStatisticsResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('course_id', type=str, required=True)

    @marshal_with(course_statistics_fields)
    def get(self, statistics_id):
        statistics = CourseStatistics.query.get(statistics_id)
        if statistics:
            return statistics
        else:
            return {'message': 'Course Statistics not found'}, 404

    @marshal_with(course_statistics_fields)
    def post(self):
        args = self.parser.parse_args()
        statistics = CourseStatistics(course_id=args['course_id'])
        db.session.add(statistics)
        db.session.commit()
        return statistics, 201

    @marshal_with(course_statistics_fields)
    def put(self, statistics_id):
        statistics = CourseStatistics.query.get(statistics_id)
        if statistics:
            args = self.parser.parse_args()
            statistics.course_id = args['course_id']
            db.session.commit()
            return statistics
        else:
            return {'message': 'Course Statistics not found'}, 404

    def delete(self, statistics_id):
        statistics = CourseStatistics.query.get(statistics_id)
        if statistics:
            db.session.delete(statistics)
            db.session.commit()
            return {'message': 'Course Statistics deleted'}
        else:
            return {'message': 'Course Statistics not found'}, 404


class AdminCourseManagementResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('course_id', type=str, required=True)

    @marshal_with(course_fields)
    def get(self, management_id):
        management = AdminCourseManagement.query.get(management_id)
        if management:
            return management
        else:
            return {'message': 'Admin Course Management not found'}, 404

    @marshal_with(course_fields)
    def post(self):
        args = self.parser.parse_args()
        management = AdminCourseManagement(course_id=args['course_id'])
        db.session.add(management)
        db.session.commit()
        return management, 201

    @marshal_with(course_fields)
    def put(self, management_id):
        management = AdminCourseManagement.query.get(management_id)
        if management:
            args = self.parser.parse_args()
            management.course_id = args['course_id']
            db.session.commit()
            return management
        else:
            return {'message': 'Admin Course Management not found'}, 404

    def delete(self, management_id):
        management = AdminCourseManagement.query.get(management_id)
        if management:
            db.session.delete(management)
            db.session.commit()
            return {'message': 'Admin Course Management deleted'}
        else:
            return {'message': 'Admin Course Management not found'}, 404


class StudentDetailsManagementResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('management_id', type=str, required=True)

    @marshal_with(user_fields)
    def get(self, management_id):
        management = StudentDetailsManagement.query.get(management_id)
        if management:
            return management
        else:
            return {'message': 'Student Details Management not found'}, 404

    @marshal_with(user_fields)
    def post(self):
        args = self.parser.parse_args()
        management = StudentDetailsManagement(
            management_id=args['management_id'])
        db.session.add(management)
        db.session.commit()
        return management, 201

    @marshal_with(user_fields)
    def put(self, management_id):
        management = StudentDetailsManagement.query.get(management_id)
        if management:
            args = self.parser.parse_args()
            management.management_id = args['management_id']
            db.session.commit()
            return management
        else:
            return {'message': 'Student Details Management not found'}, 404

    def delete(self, management_id):
        management = StudentDetailsManagement.query.get(management_id)
        if management:
            db.session.delete(management)
            db.session.commit()
            return {'message': 'Student Details Management deleted'}
        else:
            return {'message': 'Student Details Management not found'}, 404


class AssignmentStatusResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('status', type=str, required=True)

    @marshal_with(assignment_fields)
    def get(self, status_id):
        status = AssignmentStatus.query.get(status_id)
        if status:
            return status
        else:
            return {'message': 'Assignment Status not found'}, 404

    @marshal_with(assignment_fields)
    def post(self):
        args = self.parser.parse_args()
        status = AssignmentStatus(status=args['status'])
        db.session.add(status)
        db.session.commit()
        return status, 201

    @marshal_with(assignment_fields)
    def put(self, status_id):
        status = AssignmentStatus.query.get(status_id)
        if status:
            args = self.parser.parse_args()
            status.status_id = args['status_id']
            db.session.commit()
            return status
        else:
            return {'message': 'Assignment Status not found'}, 404

    def delete(self, status_id):
        status = AssignmentStatus.query.get(status_id)
        if status:
            db.session.delete(status)
            db.session.commit()
            return {'message': 'Assignment Status deleted'}
        else:
            return {'message': 'Assignment Status not found'}, 404
