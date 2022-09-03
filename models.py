from enum import unique
from extensions import db,login_manager
from app import app as app
from sqlalchemy.sql import func
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Language(db.Model):
    lang_id =  db.Column(db.Integer(), primary_key = True, autoincrement=True)
    lang_name = db.Column(db.String(40))

    def __repr__(self):
        return self.lang_name

    def add(self):
        db.session.add(self)
        db.session.commit()

class Book(db.Model):
    book_id =  db.Column(db.Integer(), primary_key = True, autoincrement=True)
    title = db.Column(db.String(60),unique=True)
    author = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float(), default=0.00)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(60))
    stock = db.Column(db.Integer(),default=0)
    language_id = db.Column(db.Integer(),db.ForeignKey('language.lang_id'))
    publisher = db.Column(db.String(60))
    genre_id = db.Column(db.Integer(),db.ForeignKey('genre.genre_id'))


    def __repr__(self):
        return self.title

    def add(self):
        db.session.add(self)
        db.session.commit()

    # production_date = db.Column(db.Date())
    # is_new = db.Column(db.Boolean(), default=0)
    # rating = db.Column(db.Float(), default=0.0)
    # created_at = db.Column(db.DateTime(),  default=func.now())
    # updated_at = db.Column(db.DateTime(),default=func.now())
    # category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))





class Genre(db.Model):
    genre_id = db.Column(db.Integer(),  primary_key = True, autoincrement=True)
    genre_name = db.Column(db.String(40))

    def __repr__(self):
        return self.genre_name

    def add(self):
        db.session.add(self)
        db.session.commit()



class Comments(db.Model):
    id =  db.Column(db.Integer(), primary_key = True)
    full_name = db.Column(db.String(60), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(),  default=func.now())
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))


    def __repr__(self):
        return self.full_name



    def add(self):
        db.session.add(self)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(UserMixin, db.Model):
    id =  db.Column(db.Integer(), primary_key = True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique = True,nullable=False)
    username = db.Column(db.String(60),unique = True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=False)

    def __init__(self,first_name,last_name,email,username,password,is_active=True,is_superuser=False):
        self.first_name=first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.is_active = is_active
        self.is_superuser = is_superuser

    def set_password(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self,password):
        check_password_hash(self.password,password)


    def add(self):
        db.session.add(self)
        db.session.commit()