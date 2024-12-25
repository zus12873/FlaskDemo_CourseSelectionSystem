#从flask_sqlalchemy模块里导入SQLAlchemy类
from flask_sqlalchemy import SQLAlchemy

#初始化SQLAlchemy实例
db = SQLAlchemy()

#定义课程的模型类
class Course(db.Model):
    __name__ = 'tb_Course'
    #定义课程id字段，作为主键
    id = db.Column(db.Integer, primary_key=True)
    #定义课程名称字段，长度不超过100的字符串，不能为空
    name = db.Column(db.String(100), nullable=False)

class  User(db.Model):
    __name__ = 'tb_User'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    user_id = db.Column(db.String(100), primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_role = db.Column(db.String(50))
    pwd_hash = db.Column(db.String(100), nullable=False)
    user_remark = db.Column(db.String(50))

#定义选课表的模型类
class SelectedCourse(db.Model):
    #定义表中的id字段，作为主键
    id = db.Column(db.Integer, primary_key=True)
    #定义用户地钻，长度不超过100的字符串，不能为空
    user_id = db.Column(db.String(100), nullable=False)
    #定义课程id字段，是课程表中id字段的外键
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    # 定义与课程模型的关系，表示一个SelectedCourse对应一个Course
    # backref参数用于在Course模型中反向引用SelectedCourse，名为selected_courses
    # lazy=True表示这个反向引用在访问时才会加载相关对象，避免不必要的数据库查询
    #通过db.relationship定义了这两个模型之间的关系，使得可以通过SelectedCourse实例访问其关联的Course实例，反之亦然（通过selected_courses属性）
    course = db.relationship('Course', backref=db.backref('selected_courses', lazy=True))


