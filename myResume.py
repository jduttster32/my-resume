import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.Text)
    courses = db.relationship('Course', backref='teacher', cascade='delete')


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    name = db.Column(db.String(256))
    description = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/teachers')
def show_all_teachers():
    teachers = Teacher.query.all()
    return render_template('teacher-all.html', teachers=teachers)

@app.route('/teacher/add', methods=['GET', 'POST'])
def add_teachers():
    if request.method == 'GET':
        return render_template('teacher-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        department = request.form['department']

        # insert the data into the database
        teacher = Teacher(name=name, department=department)
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('show_all_teachers'))

@app.route('/teacher/edit/<int:id>', methods=['GET', 'POST'])
def edit_teacher(id):
    teacher = Teacher.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('teacher-edit.html', teacher=teacher)
    if request.method == 'POST':
        # update data based on the form data
        teacher.name = request.form['name']
        teacher.department = request.form['department']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_teachers'))

@app.route('/teacher/delete/<int:id>', methods=['GET', 'POST'])
def delete_teacher(id):
    teacher = Teacher.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('teacher-delete.html', teacher=teacher)
    if request.method == 'POST':
        # delete the artist by id
        # all related songs are deleted as well
        db.session.delete(teacher)
        db.session.commit()
        return redirect(url_for('show_all_teachers'))

@app.route('/courses')
def show_all_courses():
    courses = Course.query.all()
    return render_template('course-all.html', courses=courses)

@app.route('/course/add', methods=['GET', 'POST'])
def add_courses():
    if request.method == 'GET':
        teachers = Teacher.query.all()
        return render_template('course-add.html', teachers=teachers)
    if request.method == 'POST':
        # get data from the form
        number = request.form['number']
        name = request.form['name']
        description = request.form['description']
        teacher_name = request.form['teacher']
        teacher = Teacher.query.filter_by(name=teacher_name).first()
        course = Course(name=name, number=number, teacher=teacher, description=description)

        # insert the data into the database
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('show_all_courses'))

@app.route('/course/edit/<int:id>', methods=['GET', 'POST'])
def edit_course(id):
    course = Course.query.filter_by(id=id).first()
    teachers = Teacher.query.all()
    if request.method == 'GET':
        return render_template('course-edit.html', course=course, teachers=teachers)
    if request.method == 'POST':
        course.number = request.form['number']
        course.name = request.form['name']
        course.description = request.form['description']
        teacher_name = request.form['teacher']
        teacher = Teacher.query.filter_by(name=teacher_name).first()
        course.teacher = teacher
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_courses'))

@app.route('/course/delete/<int:id>', methods=['GET', 'POST'])
def delete_course(id):
    course = Course.query.filter_by(id=id).first()
    teachers = Teacher.query.all()
    if request.method == 'GET':
        return render_template('course-delete.html', song=song, artists=artists)
    if request.method == 'POST':
        # use the id to delete the song
        # song.query.filter_by(id=id).delete()
        db.session.delete(course)
        db.session.commit()
        return redirect(url_for('show_all_courses'))

@app.route('/about')
def get_about():
    #return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True);
