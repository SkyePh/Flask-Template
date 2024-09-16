from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required, current_user, login_user, logout_user

#make this file to be a blueprint file (have routes in this)
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #handle post req to login
    email = request.form.get('email')
    password = request.form.get('password')

    #query the db
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            flash('Successfully logged in!', category='success')

            login_user(user, remember=True)

            return redirect(url_for('views.home'))
        else:
            flash('Incorrect password. Try again.', category='error')
    else:
        flash('User does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #check if acc exxist already
        user = User.query.filter_by(email=email).first()

        #handle errors else create acc
        if user:
            flash('User already exists.', category='error')
        elif len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords must match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters", category="error")
        else:
            #add account to db
            ## hash.method 'sha256' not supported anymore gotta use 'pbkdf2:sha256'
            new_user = User(email=email, username=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)

            flash("You have successfully registered", category="success")

            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)