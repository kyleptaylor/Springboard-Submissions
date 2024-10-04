"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenPotPie"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Added for app context
app.app_context().push() 

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_home():
    """ Display homepage """
    return render_template('home.html')

@app.route('/new-user')
def show_new_user_form():
    """ Display user form """
    return render_template('new_user.html')

@app.route('/new-user', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form.get("image_url")
    if not image_url:
        image_url = None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f'/users/{new_user.id}')

@app.route('/users/<user_id>')
def show_user(user_id):
    """ Show details for user based on pet id"""
    user = User.query.get_or_404(user_id)
    return render_template('user.html', user = user)

@app.route('/users')
def show_users():
    """ List all users from db """
    users = User.query.all()
    return render_template('users.html', users = users)

@app.route('/delete-user/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    """ Remove user from db """
    user = User.query.get_or_404(user_id)
    user.delete_user()
    return redirect(f'/users')

@app.route('/edit-user/<int:user_id>')
def show_edit_user_form(user_id):
    """ Get user and display eidt user form """
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user = user)

@app.route('/edit-user/<int:user_id>', methods=["POST"])
def edit_user(user_id):
    
    # Get user from db 
    current_user = User.query.get_or_404(user_id)

    # Get the form data
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form.get("image_url")

    if not image_url:
        image_url = None

    current_user.first_name = first_name
    current_user.last_name = last_name
    current_user.image_url = image_url

    db.session.commit()

    return redirect(f'/users/{current_user.id}')