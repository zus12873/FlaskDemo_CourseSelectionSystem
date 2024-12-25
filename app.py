from flask import Flask, render_template, request, redirect, url_for, session
from flask_migrate import Migrate
from models import db, Course, SelectedCourse, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

#首页，默认所有课程列表
@app.route('/')
def index():
    courses = Course.query.all()
    user_id = 'user_123'
    return render_template('index.html', courses=courses,user_id=user_id)

#选课页面
@app.route('/select/<int:course_id>')
def select_course(course_id):
    course = Course.query.get_or_404(course_id)
    if 'selected_courses' not in session:
        session['selected_courses'] = []
    # 这里我们使用简单的用户ID，你可以替换为实际的用户认证系统
    user_id = 'user_123'
    selected_course = SelectedCourse.query.filter_by(user_id=user_id, course_id=course_id).first()
    if not selected_course:
        new_selected_course = SelectedCourse(user_id=user_id, course_id=course_id)
        db.session.add(new_selected_course)
        db.session.commit()
    return redirect(url_for('selected_courses', user_id=user_id))

#删除选课页面
@app.route('/delete/<int:course_id>')
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    if 'selected_courses' not in session:
        session['selected_courses'] = []
    # 替换为实际的用户认证系统
    user_id = 'user_123'
    selected_course = SelectedCourse.query.filter_by(user_id=user_id, course_id=course_id).first()
    db.session.delete(selected_course)
    db.session.commit()
    return redirect(url_for('selected_courses', user_id=user_id))

#已选课程列表
@app.route('/selected_courses/<user_id>')
def selected_courses(user_id):
    selected_courses = SelectedCourse.query.filter_by(user_id=user_id).all()
    course_names = [course.course.name for course in selected_courses]
    course_id = [course.course.id for course in selected_courses]
    course = {course_id[i]: course_names[i] for i in range(len(course_id))}
    return render_template('selected_courses.html', course=course)


#选课页面
@app.route('/add_course', methods=['GET','POST'])
def add_course():
    if request.method == 'GET':
        return render_template('add_course.html')
    else:
        course_name = request.form['course_name']
        course = Course(name=course_name)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('add_course'))

if __name__ == '__main__':
    with app.app_context():
        #创建所有表
        db.create_all()
    app.run()