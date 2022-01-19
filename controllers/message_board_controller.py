from flask import Blueprint, request, redirect, render_template, session
from datetime import datetime


from models.message_board import delete_post, get_all_posts, create_post, delete_post,filter_posts

message_board_controller = Blueprint("message_board_controller", __name__, template_folder="../templates")


@message_board_controller.route('/home', methods=["POST","GET"])
def homepage():
    if request.method == "GET":
        if session['user_id']:
            posts = get_all_posts()
            user_id = session['user_id']

            return render_template('main.html', posts=posts, user_id=user_id)
        else:
            return redirect('/login')
    else:
        category = request.form.get('filter')
        if category == 'all':
            posts = get_all_posts()
            user_id = session['user_id']
            return render_template('main.html', posts=posts, user_id=user_id)
        else:
            posts = filter_posts(category)
            user_id = session['user_id']
            return render_template('main.html', posts=posts, user_id=user_id)


        

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
