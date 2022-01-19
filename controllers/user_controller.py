from flask import Blueprint, render_template, redirect, request,session
import bcrypt
from models.user import  get_user, insert_user, get_posts_from_user


user_controller = Blueprint('user_controller', __name__,template_folder='/..templates/user')

@user_controller.route('/signup')
def signup():

    return render_template('user/signup.html')

@user_controller.route('/users', methods=["POST"])
def create_user():

    first_name = request.form.get('fName')
    last_name = request.form.get('lName')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    location = request.form.get('location')
    avatar = request.form.get('avatar')

    insert_user(first_name, last_name, email, hashed_pw, location, avatar)
    return redirect('/login')

@user_controller.route('/posts')
def user_posts():
    if session['user_id']:
        user_id = session['user_id']
        posts = get_posts_from_user(user_id)
        print(posts)

        return render_template('main.html', posts=posts, user_id=user_id)
    else:
        return redirect('/login')

@user_controller.route('/profile/<user_id>')
def user_profile(user_id):
    if session['user_id']:
        results = get_user(user_id)
        user_info = results[0]

        print(user_info)

        return render_template('profile.html', user_info=user_info)
    else:
        return redirect('/login')
    