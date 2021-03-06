from flask import Flask, g, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


from models import db
# 这里 import 具体的 Model 类是为了给 migrate 用
# 如果不 import 那么无法迁移
# 这是 SQLAlchemy 的机制
from models.todo import Todo
from models.user import User
from models.blog import Blog
from models.tag import Tag
from models.comment import Comment
from models.comment_reply import Reply
from models.message import Message
from routes.user import current_user

from routes.todo import main as routes_todo
from routes.blog import main as routes_blog
from routes.user import main as routes_user
from routes.tag import main as routes_tag
from routes.comment import main as routes_comment
from routes.api import main as routes_api
from routes.upload import main as routes_upload
from routes.message import main as routes_message
# from routes.admin_views import admin
# from routes.chest_views import chest
# from routes.question_views import question
# from routes.topic_views import topic

app = Flask(__name__)
db_path = 'blog.sqlite'
manager = Manager(app)


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'secret key'
    app.config['UPLOAD_FOLDER'] = r'C:\Users\lijunchao\userres'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gua@localhost/todo'
    db.init_app(app)
    app.register_blueprint(routes_todo, url_prefix='/todo')
    app.register_blueprint(routes_user, url_prefix='/user')
    app.register_blueprint(routes_tag, url_prefix='/tag')
    app.register_blueprint(routes_comment, url_prefix='/comment')
    app.register_blueprint(routes_api, url_prefix='/api')
    app.register_blueprint(routes_upload, url_prefix='/upload')
    app.register_blueprint(routes_message, url_prefix='/message')
    app.register_blueprint(routes_blog)


def configured_app():
    configure_app()
    return app


@app.before_request
def before_request():
    if current_user():
        user = current_user()
        count = Message.query.filter_by(status=0,user_id=user.id).count()
        g.count = count
        g.user = user


# 自定义的命令行命令用来运行服务器
@manager.command
def server():
    app = configured_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def configure_manager():
    """
    这个函数用来配置命令行选项
    """
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()
