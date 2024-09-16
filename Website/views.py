from flask import Blueprint, render_template
from flask_login import login_required, current_user

#make this file to be a blueprint file (have routes in this)
views = Blueprint('views', __name__)

#home endpoint
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)