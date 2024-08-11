# Import Tools
from flask import Flask, request, render_template, redirect, flash, jsonify, url_for, session
from flask_debugtoolbar import DebugToolbarExtension

# Import Files
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "bogglemaster"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/boggle')
def render_board():
    return render_template("boggle.html")
    