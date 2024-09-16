from flask import Blueprint, render_template

#make this file to be a blueprint file (have routes in this)
views = Blueprint('views', __name__)

#home endpoint
@views.route('/')
def home():
    return render_template("home.html")