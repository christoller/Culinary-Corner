from flask import Blueprint, request, redirect, render_template, session, flash
import database
from datetime import datetime


from models.message_board import get_all_posts, create_post

message_board_controller = Blueprint("message_board_controller", __name__, template_folder="../templates")

now = datetime.now()


@message_board_controller.route('/home')
def homepage():

    posts = get_all_posts()
    # post = results['post']
    # date_submitted = results['date_submitted']
    # first_name = results['first_name']
    # last_name = results['last_name']
    # category = results['category']
    # location = results['location']
    # avatar = results['avatar']
    # name = f'{first_name} {last_name}'

    #post=post, date_submitted=date_submitted, name=name, category=category, location=location, avatar=avatar

    return render_template('main.html', posts=posts)

@message_board_controller.route('/post/create', methods=["POST"])
def make_post():
    user_id = session['user_id']
    post = request.form.get('post-content')
    date_submitted = now.strftime("%y-%m-%d %H:%M:%S")
    category = request.form.get('category')

    create_post(user_id, post, date_submitted, category)


    return redirect('/home')
