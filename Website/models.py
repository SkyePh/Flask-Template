##DB MODELS
from datetime import datetime, timezone

#import db var from current package
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func #using this to auto get date and time

#Notes table
class Note(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #'1 to many' relationship (user can have many notes). store key in notes that shows which user wrote it


#User table
class User(db.Model, UserMixin):

    #unique id for each user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.relationship('Note')