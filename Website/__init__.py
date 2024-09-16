from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#create db
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fueh carti'
    #store db in website file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_db(app)

    return app


##check if db is already created. if not then create it
def create_db(app):
    with app.app_context():

        if not path.exists('Website/' + DB_NAME):
            db.create_all()
            print('Database created')