from application.resources.api import (
    ModuleResource, EnrollmentResource, LectureResource, NoteResource,
    AssignmentResource, ProgrammingAssignmentResource, TestCaseResource,
    QuestionResource, SubmissionResource,
    CourseResource, StudentDetailsManagementResource, AssignmentStatusResource,
    CourseStatisticsResource,
    AdminCourseManagementResource
)
from application.resources.ai_api import (
    VirtualInstructorQueryResource,
    InstructorContentPlannerResource,
    StudentPlannerResource
)

import logging
import os
from flask import Flask, render_template
from flask_cors import CORS
from application.config import LocalDevelopmentConfig
from application.database import db
from application.models import (
    User, Role
)
from flask_restful import Api
from flask_security import (
    Security, hash_password, SQLAlchemySessionUserDatastore)


# applying logging in the project
logging.basicConfig(
    filename='debug.log', level=logging.DEBUG,
    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)


app, api = None, None


def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
        # app.logger.info("Currently no production is being setup")
        raise Exception("Currently no production config is setup.")
    else:
        # app.logger.info("Starting local development")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    db.create_all()

    app.security = Security(app, user_datastore)

    roles = [
        ('admin', 'Administrator'),
        ('user', 'User'),
        ('instructor', 'Instructor')
    ]
    for name, description in roles:
        role = Role.query.filter_by(name=name).first()
        if role is None:
            role = Role(name=name, description=description)
            db.session.add(role)
    db.session.commit()
    # To add admin on initializing of database
    role = Role.query.filter_by(name='admin').first()
    if not app.security.datastore.find_user(email="24f20021team@sep.com"):
        app.security.datastore.create_user(
            email="24f20021team@sep.com", password=hash_password("password"))
    db.session.commit()
    user = app.security.datastore.find_user(email="24f20021team@sep.com")
    app.security.datastore.add_role_to_user(user=user, role=role)
    db.session.commit()
    api = Api(app)
    return app, api


app, api = create_app()

# app.logger.info("Starting local development")
cors = CORS(app)

from application.resources.auth_api import *

@app.errorhandler(404)
def page_not_found(e):
    # setting 404 status explicitly
    return render_template('404.html'), 404

# Set up API endpoints
api.add_resource(VirtualInstructorQueryResource,
                 '/virtual_instructor_queries/<string:course_id>/<string:student_id>',  # GET endpoint
                 '/virtual_instructor_queries',  # POST endpoint
                 '/virtual_instructor_queries/<string:course_id>/<string:student_id>')  # DELETE endpoint

api.add_resource(InstructorContentPlannerResource,
                 '/instructor_content/<string:instructor_id>/<string:course_id>/<string:content_type>',  # GET endpoint
                 '/instructor_content',  # POST endpoint
                 '/instructor_content/<string:query_id>')  # DELETE endpoint

api.add_resource(StudentPlannerResource,
                 '/student_planner/<string:student_id>/<string:content_type>',  # GET endpoint
                 '/student_planner',
                 '/student_planner/<string:query_id>')  

api.add_resource(CourseResource,
                 '/courses',  # POST endpoint
                 '/courses/<int:course_id>')  # GET, PUT, DELETE endpoint

api.add_resource(EnrollmentResource,
                 '/enrollments',  # POST endpoint
                 '/enrollments/<int:enrollment_id>')  # GET, PUT, DELETE endpoint

api.add_resource(ModuleResource,
                 '/modules',
                 '/modules/<int:module_id>')  

api.add_resource(LectureResource,
                 '/lectures',  # POST endpoint
                 '/notes/<int:module_id>'
                 '/lectures/<int:lecture_id>')  # GET, PUT, DELETE endpoint

api.add_resource(NoteResource,
                 '/notes',  # POST endpoint
                 '/notes/<string:note_id>')  # GET, PUT, DELETE endpoint

api.add_resource(AssignmentResource,
                 '/assignments',  # POST endpoint
                 '/assignments/<string:assignment_id>')  # GET, PUT, DELETE endpoint

api.add_resource(ProgrammingAssignmentResource,
                 '/programming_assignments',  # POST endpoint
                 '/programming_assignments/<string:programming_assignment_id>')  # GET, PUT, DELETE endpoint

api.add_resource(TestCaseResource,
                 '/test_cases',  # POST endpoint
                 '/test_cases/<string:test_case_id>')  # GET, PUT, DELETE endpoint

api.add_resource(QuestionResource,
                 '/questions',  # POST endpoint
                 '/questions/<string:question_id>')  # GET, PUT, DELETE endpoint

api.add_resource(SubmissionResource,
                 '/submissions',  # POST endpoint
                 '/submissions/<string:submission_id>')  # GET, PUT, DELETE endpoint

api.add_resource(CourseStatisticsResource,
                 '/course_statistics',  # POST endpoint
                 '/course_statistics/<string:statistics_id>')  # GET, PUT, DELETE endpoint

api.add_resource(AdminCourseManagementResource,
                 '/admin_course_managements',  # POST endpoint
                 '/admin_course_managements/<string:management_id>')  # GET, PUT, DELETE endpoint

api.add_resource(StudentDetailsManagementResource,
                 '/student_details_managements',  # POST endpoint
                 '/student_details_managements/<string:management_id>')  # GET, PUT, DELETE endpoint

api.add_resource(AssignmentStatusResource,
                 '/assignment_statuses',  # POST endpoint
                 '/assignment_statuses/<string:status_id>')  # GET, PUT, DELETE endpoint


if __name__ == "__main__":
    # Run the Flask app
    app.run(host='0.0.0.0', port=8000)
