import plotly
import plotly.graph_objs as go
import json

from flask import render_template, flash, request, redirect, session
from Model import *
from WTForms import *

app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/edit_faculty', methods=['GET', 'POST'])
def edit_faculty():

    form = FacultiesForm()
    select_result = Faculties.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('faculties.html', data=select_result, form=form)
        else:
            name_faculty = session['faculty_edit_pk_data']
            faculty = Faculties.query.filter_by(name_faculty=name_faculty).first()
            faculty.name_faculty = form.name_faculty.data
            faculty.students_count = form.students_count.data
            faculty.teachers_count = form.teachers_count.data
            db.session.commit()
            return render_template("faculties.html", data=select_result, form=form)

    return render_template("faculties.html", data=select_result, form=form)


@app.route('/faculties', methods=['GET', 'POST'])
def faculties():

    form = FacultiesForm()
    select_result = Faculties.query.filter_by().all()

    if request.method == 'POST':

        selected_code = request.form.get('del')
        if selected_code is not None:
            selected_row = Faculties.query.filter_by(name_faculty=selected_code).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('faculties.html', data=select_result, form=form)

        selected_code = request.form.get('edit')
        if selected_code is not None:
            selected_row = Faculties.query.filter_by(name_faculty=selected_code).first()
            session['faculty_edit_pk_data'] = selected_code
            return render_template("edit_faculty.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('faculties.html', data=select_result, form=form)
        else:
            faculty = Faculties(form.name_faculty.data)
            db.session.add(faculty)
            db.session.commit()
            select_result.append(faculty)

    return render_template('faculties.html', data=select_result, form=form)


@app.route('/edit_teacher', methods=['GET', 'POST'])
def edit_teacher():

    form = TeachersForm()
    select_result = Teachers.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('edit_teacher.html')
        else:
            number = session['teacher_edit_pk_data']
            teacher = Teachers.query.filter_by(passport_number=number).first()
            teacher.passport_number = form.name.passport_number
            teacher.full_name = form.full_name.data
            teacher.salary = form.salary.data
            teacher.faculty = form.faculty.data
            db.session.commit()
            return render_template("teachers.html", data=select_result, form=form)

    return render_template("teachers.html", data=select_result, form=form)


@app.route('/teachers', methods=['GET', 'POST'])
def teachers():

    form = TeachersForm()
    select_result = Teachers.query.filter_by().all()

    if request.method == 'POST':

        selected_number = request.form.get('del')
        if selected_number is not None:
            selected_row = Teachers.query.filter_by(passport_number=selected_number).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('teachers.html', data=select_result, form=form)

        selected_number = request.form.get('edit')
        if selected_number is not None:
            selected_row = Teachers.query.filter_by(passport_number=selected_number).first()
            session['teacher_edit_pk_data'] = selected_number
            return render_template("edit_teacher.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('teachers.html', data=select_result, form=form)
        else:
            teacher = Teachers(form.passport_number.data)
            db.session.add(teacher)
            db.session.commit()
            select_result.append(teacher)

    return render_template('teachers.html', data=select_result, form=form)


@app.route('/edit_group', methods=['GET', 'POST'])
def edit_group():

    form = GroupsForm()
    select_result = Groups.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('groups.html', data=select_result, form=form)
        else:
            name = session['group_edit_pk_data']
            group = Groups.query.filter_by(name_groups=name).first()
            group.name_groups = form.name_groups.data
            group.name_faculty = form.name_faculty.data
            group.count_student = form.count_student.data
            db.session.commit()
            return render_template("groups.html", data=select_result, form=form)

    return render_template("groups.html", data=select_result, form=form)


@app.route('/groups', methods=['GET', 'POST'])
def groups():

    form = GroupsForm()
    select_result = Groups.query.filter_by().all()

    if request.method == 'POST':

        selected_name = request.form.get('del')
        if selected_name is not None:
            selected_row = Groups.query.filter_by(name_groups=selected_name).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('groups.html', data=select_result, form=form)

        selected_name = request.form.get('edit')
        if selected_name is not None:
            selected_row = Groups.query.filter_by(name_groups=selected_name).first()
            session['group_edit_pk_data'] = selected_name
            return render_template("edit_group.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('groups.html', data=select_result, form=form)
        else:
            group = Groups(form.name_groups.data)
            db.session.add(group)
            db.session.commit()
            select_result.append(group)

    return render_template('groups.html', data=select_result, form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    last_char = None
    if request.method == 'POST':

        last_char = request.form.get('last_char')
        if len(last_char) > 1:
            return redirect('/dashboard')

    select_result_raw = Groups.query.filter_by().all()
    if last_char is not None and last_char != "":
        select_result = [select_result_row.code for select_result_row in select_result_raw
                         if select_result_row.code[-1] == last_char]
    else:
        select_result = [select_result_row.code for select_result_row in select_result_raw]

    codes_starts_result = list(map(lambda s: s[:2], select_result))
    codes = list(set(codes_starts_result))
    counting_stars = [0] * len(codes)

    for no_more_counting_dollars in codes_starts_result:
        counting_stars[codes.index(no_more_counting_dollars[:2])] += 1

    bar, pie = go.Bar(x=codes, y=counting_stars, marker=dict(color='rgb(122, 122, 122)')), go.Pie(labels=codes, values=counting_stars)

    data1, data2 = [bar], [pie]
    ids = ["1", "2"]

    graphJSON1 = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html',
                           graphJSON1=graphJSON1, graphJSON2=graphJSON2, ids=ids)


if __name__ == '__main__':
    app.run(debug=True)