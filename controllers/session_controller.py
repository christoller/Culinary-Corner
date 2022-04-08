from flask import Blueprint, request, redirect, render_template, session, flash
from models.user import get_user_by_email
import bcrypt


session_controller = Blueprint("session_controller", __name__, template_folder="../templates/user")

@session_controller.route('/login')
def loginpage():
    if session.get('user_id'):
        return redirect('/home')
    else:
        return render_template('login.html')

@session_controller.route('/login/create', methods=["POST"])
def login():

    email = request.form.get('email')
    user = get_user_by_email(email)
    password = request.form.get('password')
    
    if user and bcrypt.checkpw(password.encode(), user['password'].encode()):
        session['user_id'] = user['id']
        session['user_name'] = user['first_name']
        session['avatar'] = user['avatar']
        return redirect('/home')
    else:
        flash('Incorrect Username or Password. Please Try Again.')
        return redirect('/login?error=Incorrect')  


@session_controller.route('/sessions/delete', methods=["POST"])
def logout():
    session['user_id'] = None
    session['user_name'] = None
    return redirect('/')