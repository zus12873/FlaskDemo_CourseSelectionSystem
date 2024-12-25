import os

class Config:
    #MySQL的连接地址
    HOSTNAME = '127.0.0.1'
    # MySQL监听的端口号，默认3306
    PORT = 3306
    # 连按MySQL的用户名
    USERNAME = "root"
    # 连按MYSQL的密码
    PASSWORD = "123456"
    # MYSQL上创建的数据库名称
    DATABASE = "course_selection_db"
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/course_selection_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MIGRATE_DIR = os.path.join(os.getcwd(), 'migrations')


