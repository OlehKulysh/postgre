from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///db_name'

db = SQLAlchemy(app)


class Faculties(db.Model):
    __tablename__ = 'faculties'
    name_faculty = db.Column('NAME_FACULTY', db.String(11), primary_key=True)
    students_count = db.column('STUDENTS_COUNT', db.Integer)
    teachers_count = db.column('TEACHERS_COUNT', db.Integer)

    teachers = db.relationship('Teachers', backref='faculties', lazy='dynamic')
    groups = db.relationship('Groups', backref='faculties', lazy='dynamic')

    def __init__(self, name_faculty, students_count, teachers_count):
        self.name_faculty = name_faculty
        self.students_count = students_count
        self.teachers_count = teachers_count

    def __repr__(self):
        return '<Faculties: name_faculty=%r; students_count=%r; teachers_count=%r>' % \
               self.name_faculty, self.students_count, self.teachers_count


class Teachers(db.Model):
    __tablename__ = 'TEACHERS'
    passport_number = db.Column('PASSPORT_NUMBER', db.String(11), primary_key=True)
    full_name = db.Column('FULL_NAME', db.String(50))
    salary = db.Column('SALARY', db.Integer)
    faculty = db.Column('FACULTY', db.String(11), db.ForeignKey('faculties.NAME_FACULTY'), primary_key=True)

    audiencesEndLesson = db.relationship('AudiencesEndLesson', backref='TEACHERS', lazy='dynamic')
    questionTeacher = db.relationship('QuestionTeacher', backref='TEACHERS', lazy='dynamic')

    def __init__(self, passport_number, full_name, salary, faculty):
        self.passport_number = passport_number
        self.full_name = full_name
        self.salary = salary
        self.faculty = faculty

    def __repr__(self):
        return '<Teachers: passport_number=%r; full_name=%r; salary=%r; faculty=%r>' % \
               self.passport_number, self.full_name, self.salary, self.faculty


class EducationalBuildings(db.Model):
    __tablename__ = 'EDUCATIONAL_BUILDINGS'
    number_building = db.Column('number_BUILDING', db.Integer, primary_key=True)
    name_building = db.Column('name_BUILDING', db.String(50))

    audiencesEndLesson = db.relationship('AudiencesEndLesson', backref='EDUCATIONAL_BUILDINGS', lazy='dynamic')
    questionEducationalBuildings = db.relationship('QuestionEducationalBuildings', backref='EDUCATIONAL_BUILDINGS', lazy='dynamic')

    def __init__(self, number_building, name_building):
        self.number_building = number_building
        self.name_building = name_building

    def __repr__(self):
        return '<Educational Buildings: number_building=%r; name_building=%r>' % \
               self.number_building, self.name_building


class Groups(db.Model):
    __tablename__ = 'groups'
    name_groups = db.Column('name_groups', db.String(11), primary_key=True)
    name_faculty = db.Column('name_FACULTY', db.String(11), db.ForeignKey('faculties.NAME_FACULTY'), primary_key=True)
    count_student = db.Column('count_student', db.Integer)

    audiencesEndLesson = db.relationship('AudiencesEndLesson', backref='groups', lazy='dynamic')

    def __init__(self, name_groups, name_faculty, count_student):
        self.name_groups = name_groups
        self.name_faculty = name_faculty
        self.count_student = count_student

    def __repr__(self):
        return '<Groups: name_groups=%r; name_faculty=%r; count_student=%r>' % \
               self.name_groups, self.name_faculty, self.count_student


class AudiencesEndLesson(db.Model):
    __tablename__ = 'AUDIENCES_end_lesson'
    id_lesson = db.Column('di_lesson', db.Integer, primary_key=True)
    number_building = db.Column('number_BUILDING', db.Integer, db.ForeignKey('EDUCATIONAL_BUILDINGS.number_BUILDING'), primary_key=True)
    number_audience = db.Column('number_audience', db.Integer)
    day_lesson = db.Column('day_lesson', db.Integer, )
    number_lesson = db.Column('number_lesson', db.Integer)
    passport_number_teacher = db.Column('PASSPORT_NUMBER_teacher', db.String(11), db.ForeignKey('TEACHERS.PASSPORT_NUMBER'), primary_key=True)
    name_group = db.Column('name_group', db.String(11), db.ForeignKey('groups.name_groups'), primary_key=True)

    def __init__(self, id_lesson, number_building, number_audience, day_lesson, number_lesson, passport_number_teacher,
                 name_group):
        self.id_lesson = id_lesson
        self.number_building = number_building
        self.number_audience = number_audience
        self.day_lesson = day_lesson
        self.number_lesson = number_lesson
        self.passport_number_teacher = passport_number_teacher
        self.name_group = name_group

    def __repr__(self):
        return '<Audiences EndLesson: id_lesson=%r; number_building=%r; number_audience=%r; day_lesson=%r; number_lesson=%r; passport_number_teacher=%r; name_group=%r>' % \
               self.id_lesson, self.number_building, self.number_audience, self.day_lesson, self.number_lesson, self.passport_number_teacher, self.name_group


class QuestionTeacher(db.Model):
    __tablename__ = 'question_teacher'
    teacher_passport_number = db.Column('TEACHER_PASSPORT_NUMBER', db.String(50), db.ForeignKey('TEACHERS.PASSPORT_NUMBER'), primary_key=True)
    count_question = db.Column('count_question', db.Integer)

    def __init__(self, teacher_passport_number, count_question):
        self.teacher_passport_number = teacher_passport_number
        self.count_question = count_question

    def __repr__(self):
        return '<Question Teacher: teacher_passport_number=%r; count_question=%r>' % \
               self.teacher_passport_number, self.count_question


class QuestionEducationalBuildings(db.Model):
    __tablename__ = 'question_EDUCATIONAL_BUILDINGS'

    number_educational_buildings = db.Column('number_EDUCATIONAL_BUILDINGS', db.Integer, db.ForeignKey('EDUCATIONAL_BUILDINGS.number_BUILDING'), primary_key=True)
    count_question = db.Column('count_question', db.Integer)

    def __init__(self, number_educational_buildings, count_question):
        self.number_educational_buildings = number_educational_buildings
        self.count_question = count_question

    def __repr__(self):
        return '<Question Educational Buildings: number_educational_buildings=%r; count_question=%r>' % \
               self.number_educational_buildings, self.count_question
