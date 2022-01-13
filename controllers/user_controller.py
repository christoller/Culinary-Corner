from flask import Blueprint, render_template, redirect, request, session, flash
import bcrypt
from models.user import get_user_by_email, insert_user


user_controller = Blueprint('user_controller', __name__,template_folder='/..templates/user')

@user_controller.route('/signup')
def signup():

    return render_template('user/signup.html')

@user_controller.route('/users', methods=["POST"])
def create_user():

    first_name = request.form.get('fName')
    last_name = request.form.get('lName')
    email = request.form.get('email')
    hashed_pw = bcrypt.hashpw(request.form.get('password').encode(), bcrypt.gensalt()).decode()
    location = request.form.get('location')
    avatar = request.form.get('avatar')

    insert_user(first_name, last_name, email, hashed_pw, location, avatar)

    return redirect('/login')
