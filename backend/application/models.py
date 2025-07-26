from application.database import db
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref
from application.database import db
from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey, UnicodeText, Float
from datetime import datetime
from pytz import timezone

ist = timezone('Asia/Kolkata')


# Creating models/tables for the database


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
    permissions = Column(UnicodeText)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True)
    password = Column(String(255), nullable=False)
    profile_img = Column(String(255))
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    fs_uniquifier = Column(String(255), unique=True)
    confirmed_at = Column(DateTime())
    enrollments = relationship('Enrollment', backref='student', lazy=True)
    submissions = relationship('Submission', backref='student', lazy=True)
    virtual_instructor_queries = relationship(
        'VirtualInstructorQuery', backref='student', lazy=True)
    courses = relationship(
        'Course', backref='instructor', lazy=True)

    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))
    # student_curation= relationship('StudentCuration', backref='user',lazy='dynamic')


class Course(db.Model):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    instructor_id = Column(String, ForeignKey('user.id'))
    created_at = Column(DateTime, default= datetime.now(ist))
    
    enrollments = relationship('Enrollment', backref='course', lazy=True)
    modules = relationship('Module', backref='course', lazy=True)
    notes = relationship('Note', backref='module', lazy=True)
    course_statistics = relationship(
        'CourseStatistics', backref='course', lazy=True)
    admin_course_management = relationship(
        'AdminCourseManagement', backref='course', lazy=True)
    student_details_management = relationship(
        'StudentDetailsManagement', backref='course', lazy=True)
    virtualinstructor = relationship(
        'VirtualInstructorQuery', backref='course', lazy=True)
    instructorcontentplanner = relationship(
        'InstructorContentPlanner', backref='course', lazy=True)


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(String, ForeignKey('user.id'))
    course_id = Column(String, ForeignKey('courses.id'))
    enrollment_date = Column(DateTime, default= datetime.now(ist))
    status = Column(String)


class Module(db.Model):
    __tablename__ = 'modules'
    id = Column(Integer, primary_key=True)
    course_id = Column(String, ForeignKey('courses.id'))
    title = Column(String)
    description = Column(String)
    week = Column(Integer)
    created_at = Column(DateTime, default= datetime.now(ist))
    lectures = relationship('Lecture', backref='module', lazy=True)
    assignments = relationship('Assignment', backref='module', lazy=True)
    question = relationship('Question', backref='module', lazy=True)
    passignment = relationship('ProgrammingAssignment', backref='module', lazy=True)


class Lecture(db.Model):
    __tablename__ = 'lectures'
    id = Column(Integer, primary_key=True)
    module_id = Column(String, ForeignKey('modules.id'))
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default= datetime.now(ist))


class Note(db.Model):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    course_id = Column(String, ForeignKey('courses.id'))
    title = Column(String)
    content = Column(String)
    pdflink = Column(String)
    created_at = Column(DateTime, default= datetime.now(ist))


class Assignment(db.Model):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True)
    module_id = Column(String, ForeignKey('modules.id'))
    title = Column(String)
    description = Column(String)
    due_date = Column(DateTime)
    created_at = Column(DateTime, default= datetime.now(ist))
    submissions = relationship('Submission', backref='assignment', lazy=True)
    assignment_status = relationship(
        'AssignmentStatus', backref='assignment', lazy=True)


class ProgrammingAssignment(db.Model):
    __tablename__ = 'programming_assignments'
    id = Column(Integer, primary_key=True)
    modules_id = Column(String, ForeignKey('modules.id'))
    p_question = Column(String)
    editor_content = Column(String)
    sandbox_environment = Column(String)
    help_button_enabled = Column(Boolean)
    created_at = Column(DateTime, default= datetime.now(ist))
    test_cases = relationship(
        'TestCase', backref='programming_assignment', lazy=True)


class TestCase(db.Model):
    __tablename__ = 'test_cases'
    id = Column(Integer, primary_key=True)
    programming_assignment_id = Column(
        String, ForeignKey('programming_assignments.id'))
    input=Column(String)
    expected_output = Column(String)
    created_at = Column(DateTime, default= datetime.now(ist))


class Question(db.Model):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    module_id = Column(String, ForeignKey('modules.id'))
    marks = Column(Integer)
    question_text = Column(String)
    correct_answer = Column(String)
    options = Column(String)
    created_at = Column(DateTime, default= datetime.now(ist))


class Submission(db.Model):
    __tablename__ = 'submissions'
    id = Column(Integer, primary_key=True)
    assignment_id = Column(String, ForeignKey('assignments.id'))
    student_id = Column(String, ForeignKey('user.id'))
    submission_date = Column(DateTime, default= datetime.now(ist))
    grade = Column(Float)
    feedback = Column(String)


class VirtualInstructorQuery(db.Model):
    __tablename__ = 'virtual_instructor_queries'
    id = Column(Integer, primary_key=True)
    student_id = Column(String, ForeignKey('user.id'))
    course_id = Column(String, ForeignKey('courses.id'))
    gen_query = Column(String)
    response = Column(String)
    created_at = Column(DateTime, default= datetime.now(ist))


class InstructorContentPlanner(db.Model):
    __tablename__ = 'instructor_content_planner'
    id = Column(Integer, primary_key=True)
    instructor_id = Column(String, ForeignKey('user.id'))
    course_id = Column(String, ForeignKey('courses.id'))
    content_type = Column(String) #gen_ai resourse or question
    gen_query_text = Column(String)
    gen_ai_resources = Column(String)
    gen_ai_questions = Column(String)
    gen_ai_answers = Column(String)
    gen_ai_question_detail = Column(String)
    difficulty_level = Column(String)
    created_at = Column(DateTime, default= datetime.now(ist))

#Useless Table
class CourseStatistics(db.Model):
    __tablename__ = 'course_statistics'
    id = Column(Integer, primary_key=True)
    course_id = Column(String, ForeignKey('courses.id'))
    total_students = Column(Integer)
    average_marks = Column(Float)
    total_modules = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

#Useless Table
class AdminCourseManagement(db.Model):
    __tablename__ = 'admin_course_management'
    id = Column(Integer, primary_key=True)
    admin_id = Column(String, ForeignKey('user.id'))
    course_id = Column(String, ForeignKey('courses.id'))
    action = Column(String)
    action_date = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

#Useless table
class StudentDetailsManagement(db.Model):
    __tablename__ = 'student_details_management'
    id = Column(Integer, primary_key=True)
    admin_id = Column(String, ForeignKey('user.id'))
    student_id = Column(String, ForeignKey('user.id'))
    course_id = Column(String, ForeignKey('courses.id'))
    action = Column(String)
    action_date = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

#useless table
class AssignmentStatus(db.Model):
    __tablename__ = 'assignment_status'
    id = Column(Integer, primary_key=True)
    admin_id = Column(String, ForeignKey('user.id'))
    student_id = Column(String, ForeignKey('user.id'))
    assignment_id = Column(String, ForeignKey('assignments.id'))
    status = Column(String)
    authenticity = Column(Boolean)
    feedback = Column(String)
    created_at = Column(DateTime)
    
class StudentCuration(db.Model):
    __tablename__ = 'Student_Curation'
    id = Column(Integer, primary_key=True)
    student_id = Column(String, ForeignKey('user.id'))
    response = Column(String)
    level = Column(String)
    content_type = Column(String)
    gen_query = Column(String)
    created_at = Column(DateTime, default= datetime.now(ist))