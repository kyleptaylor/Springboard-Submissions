from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "ChickenCatMan"
app.debug = True

debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return "TESTING"
