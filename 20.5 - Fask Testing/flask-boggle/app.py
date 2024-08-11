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
    restart = request.args.get('restart')

    if restart == 'true':
        board = boggle_game.make_board()
        session.clear()
        session['board'] = board
        return jsonify({'board': board})
    
    elif 'board' not in session:
        board = boggle_game.make_board()
        session['board'] = board
    
    else:
        board = session['board']

    return render_template("boggle.html", board=board)


@app.route('/answer', methods=['POST'])
def answer():

    if 'board' not in session:
        return jsonify({'error': 'Board not found in session'}), 400

    data = request.get_json()
    word = data.get('word').lower()
    words = data.get('words')
    board = session['board']
    points = len(word)

    # Check if the word is valid and find its positions
    is_valid = boggle_game.check_valid_word(board, word)

    # Return a JSON response with the results
    return jsonify({'result': is_valid, 'word': word, 'points': points, 'words': words})
