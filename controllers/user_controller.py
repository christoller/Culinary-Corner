from flask import Blueprint, render_template, redirect, request,session, flash
import bcrypt
from models.user import  get_user_by_email, get_user_info, insert_user, get_posts_from_user, update_user

user_controller = Blueprint('user_controller', __name__,template_folder='../templates/user')

@user_controller.route('/signup')
def signup():
    if session.get('user_id'):
        return redirect('/home')
    else:
        return render_template('signup.html')

@user_controller.route('/users', methods=["POST"])
def create_user():

    first_name = request.form.get('fName')
    last_name = request.form.get('lName')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    location = request.form.get('location')
    avatar = request.form.get('avatar')

    if get_user_by_email(email):
        flash("Error. Please try again or log in")
        return redirect('/signup')
    elif not '@' in email:
        flash("Incorrect Email Format. Please try again")
        return redirect('/signup')
    elif len(password) < 8:
        flash("Password must be at least 8 characters.")
        return redirect('/signup')
    else:
        insert_user(first_name, last_name, email, hashed_pw, location, avatar)
        return redirect('/login')

@user_controller.route('/posts')
def user_posts():
    if session.get('user_id'):
        user_id = session.get('user_id')
        posts = get_posts_from_user(user_id)

        return render_template('main.html', posts=posts, user_id=user_id)
    else:
        return redirect('/login')

@user_controller.route('/profile/<user_id>')
def user_profile(user_id):
    if session.get('user_id'):
        results = get_user_info(user_id)
        user_info = results[0]

        posts = get_posts_from_user(user_id)

        return render_template('profile.html', user_info=user_info, posts=posts)
    else:
        return redirect('/login')
    
@user_controller.route('/edit')
def edit_profile():
    if session.get('user_id'):
        results = get_user_info(session.get('user_id'))
        user_info = results[0]
        return render_template('edit-profile.html', user_info=user_info)
    else:
        return redirect('/login')


    

@user_controller.route('/update', methods=['POST'])
def update_profile():
    if session.get('user_id'):
        id = int(session.get('user_id'))
        first_name = request.form.get('fName')
        last_name = request.form.get('lName')
        location = request.form.get('location')
        job_title = request.form.get('job-title')
        workplace = request.form.get('workplace')
        interests = request.form.get('interests')
        bio = request.form.get('bio')
        avatar = request.form.get('avatar')

        update_user(id, first_name, last_name, location, job_title, workplace, interests, bio, avatar)

        return redirect('/home')
    else:
        return redirect('/login')