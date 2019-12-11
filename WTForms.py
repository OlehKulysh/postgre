from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, Label
from wtforms import validators


class FacultiesForm(Form):

    name_faculty = StringField("Name: ", [validators.data_required("Please, enter name faculty.")])
    students_count = IntegerField("Count: ", [validators.data_required("Please, enter amount of students.")])
    teachers_count = IntegerField("Count: ", [validators.data_required("Please, enter amount of teachers.")])

    submit = SubmitField("Enter")


class TeachersForm(Form):

    passport_number = StringField("Number: ", [validators.data_required("Please, enter passport number.")])
    full_name = StringField("Name: ", [validators.data_required("Please, enter full name.")])
    salary = IntegerField("Salary: ", [validators.data_required("Please, enter a salary.")])
    faculty = StringField("Faculty: ", [validators.data_required("Please, enter a faculty.")])

    submit = SubmitField("Enter")


class GroupsForm(Form):

    name_groups = StringField("Groups: ", [validators.data_required("Please, enter name groups.")])
    name_faculty = StringField("Faculty: ", [validators.data_required("Please, enter name faculty.")])
    count_student = IntegerField("Count: ", [validators.data_required("Please, enter count student.")])

    submit = SubmitField("Enter")
