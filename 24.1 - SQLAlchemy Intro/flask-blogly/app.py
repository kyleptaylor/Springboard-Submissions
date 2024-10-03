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
def show_users():
    """ List all users from db """
    users = User.query.all()
    return render_template('users.html', users = users)