from flask import Blueprint, request, redirect, render_template, session, flash
import database
from datetime import datetime


from models.message_board import delete_post, get_all_posts, create_post, delete_post

message_board_controller = Blueprint("message_board_controller", __name__, template_folder="../templates")


@message_board_controller.route('/home')
def homepage():
    if session['user_id']:
        posts = get_all_posts()
        user_id = session['user_id']

        return render_template('main.html', posts=posts, user_id=user_id)
    else:
        return redirect('/login')

@message_board_controller.route('/post/create', methods=["POST"])
def make_post():
    now = datetime.now()
    user_id = session['user_id']
    post = request.form.get('post-content')
    date_submitted = now.strftime("%y-%m-%d %H:%M:%S")
    category = request.form.get('category')

    create_post(user_id, post, date_submitted, category)
    return redirect('/home')

@message_board_controller.route('/post/delete', methods=['POST'])
def remove_post():

    id = request.form.get('id')
    delete_post(id)

    return redirect('/home')
