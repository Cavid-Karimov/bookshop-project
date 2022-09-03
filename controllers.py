from crypt import methods
from flask import render_template, request, redirect
from app import app
from models import *
from forms import CommentForm, RegistrForm, LoginForm
from werkzeug.security import  check_password_hash
from flask_login import login_user, login_required, logout_user



@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/register',methods = ['GET', 'POST'])
def register():
    post_data = request.form

    form = RegistrForm()
    if request.method == 'POST': 
        post_data = request.form  
        form = RegistrForm(data = post_data)
        if form.validate_on_submit():
            user = User(first_name=form.first_name.data,last_name = form.last_name.data,email = form.email.data,username = form.username.data,password = form.password.data)
            user.add()
            return redirect('/login')
    return render_template ("register.html",form = form)



@app.route('/login',methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST': 
        post_data = request.form
        form = LoginForm(data = post_data)  
        if form.validate_on_submit():
            user = User.query.filter_by(username = form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('/')
            else:
                print("User Login ola bilmedi")
    return render_template ("login.html",form = form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


# @app.route('/')
# def index():
#     book_list  = Book.query.all()
#     return render_template ("index.html", books = book_list)


@app.route('/book/<int:book_id>',methods = ['GET', 'POST'])
def product(book_id):
    book  = Book.query.all()[book_id -1]
    language = Language.query.filter(Language.lang_id==book_id).first()
    genre = Genre.query.filter(Genre.genre_id==book_id).first()
    comments = Comments().query.filter(Comments.book_id==book_id).all()
    post_data = request.form

    form = CommentForm()

    if request.method == 'POST':   
        form = CommentForm(data = post_data)
        if form.validate_on_submit():
            comment = Comments(full_name=post_data['full_name'], message=post_data['message'], book_id = book_id)
            Comments.add(comment)

    return render_template('product.html', book=book, language=language, genre=genre, form=form, comments=comments)



    


