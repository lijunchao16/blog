from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import abort

import json

from models.blog import Blog
from models.comment import Comment
from models.comment_reply import Reply

from routes.user import current_user

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是套路
main = Blueprint('api', __name__)


# @main.route('/todo/add', methods=['POST'])
# def add():
#     form = request.form
#     t = Todo(form)
#     r = {
#         'data': []
#     }
#     if t.valid():
#         t.save()
#         r['success'] = True
#         r['data'] = t.json()
#     else:
#         r['success'] = False
#         message = t.error_message()
#         r['message'] = message
#     return json.dumps(r, ensure_ascii=False)


# @main.route('/todo/delete/<int:todo_id>', methods=['GET'])
# def delete(todo_id):
#     print('todo_id, ',todo_id)
#     w = Todo.query.get(todo_id)
#     w.delete()
#     r = {
#         'success': True,
#         'data': w.json()
#     }
#     return json.dumps(r, ensure_ascii=False)


@main.route('/upcount', methods=['POST'])
def upcount():
    form = request.form
    t_id = form.get('blogId', '')
    upcount = int(form.get('upcount', 0))
    t = Blog.query.get(t_id)
    t.upcount = upcount + 1
    r = {
        'data': []
    }
    # if t.valid():
    t.save()
    r['success'] = True
    r['data'] = t.json()
    # else:
    # r['success'] = False
    # message = t.error_message()
    # r['message'] = message
    return json.dumps(r, ensure_ascii=False)


@main.route('/dcount', methods=['POST'])
def dcount():
    form = request.form
    t_id = form.get('blogId', '')
    downcount = int(form.get('downcount', 0))
    t = Blog.query.get(t_id)
    t.downcount = downcount + 1
    r = {
        'data': []
    }
    # if t.valid():
    t.save()
    r['success'] = True
    r['data'] = t.json()
    # else:
    # r['success'] = False
    # message = t.error_message()
    # r['message'] = message
    return json.dumps(r, ensure_ascii=False)

@main.route('/comment', methods=['POST'])
def comment():
    form = request.form
    u = current_user()
    # t = Comment.query.filter_by(blog_id=t_id).first()
    t = Comment(form)
    t.user_id = u.id
    r = {
        'data': []
    }
    if t.valid():
        t.save()
        r['success'] = True
        r['data'] = t.json()
    else:
        r['success'] = False
        message = t.error_message()
        r['message'] = message
    return json.dumps(r, ensure_ascii=False)

@main.route('/reply', methods=['POST'])
def reply():
    form = request.form
    u = current_user()
    # t = Comment.query.filter_by(blog_id=t_id).first()
    t = Reply(form)
    t.user_id = u.id
    r = {
        'data': []
    }
    if t.valid():
        t.save()
        r['success'] = True
        r['data'] = t.json()
    else:
        r['success'] = False
        message = t.error_message()
        r['message'] = message
    return json.dumps(r, ensure_ascii=False)