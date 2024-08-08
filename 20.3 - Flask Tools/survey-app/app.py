from flask import Flask, request, render_template, redirect, flash, jsonify, url_for, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys 

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickencatman"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

# Home route where a user can select a survey 
@app.route('/')
def show_survey_options():
    return render_template("home.html", surveys = surveys)

# Routes user to the survey type with info about the survey and a link to start (If valid survey)
@app.route('/survey/<survey_type>')
def show_survey(survey_type):

    if survey_type not in surveys:
        return "Survey not found", 404
    else:
        survey_info = surveys[survey_type] 
        return render_template("survey.html", survey_info = survey_info, survey_type = survey_type)

# Routes the user to a dynamic survey type and the question number as an integer
# Checks for responses in the session; if none, creates a new session with an empty list
# Redirects the user if the question number does not match the response length
# Renders a dynamic question page for the survey type and question number
@app.route('/survey/<survey_type>/questions/<int:question_num>')
def show_survey_questions(survey_type, question_num):
    if survey_type not in surveys or question_num >= len(surveys[survey_type].questions):
        return "Survey or question not found", 404
    
    if 'responses' not in session:
        session['responses'] = []
    
    responses = session['responses']
    
    if len(responses) != question_num:
        flash('Please complete the question before moving on to the next question.', 'error')
        return redirect(url_for('show_survey_questions', survey_type=survey_type, question_num=len(responses)))

    survey_info = surveys[survey_type] 
    return render_template("questions.html", survey_info = survey_info, survey_type = survey_type, question_num = question_num)

# Handles the survey answers and adds responses to the session
# Creates a number for the next question if the current question is not the last
# Redirects the user to the next question or the completed survey page if the current question is the last
@app.route('/survey/<survey_type>/answers/<int:question_num>')
def handle_answers(survey_type, question_num):
    if survey_type not in surveys:
        return "Survey not found", 404

    answer = request.form.get('answer', '')
    responses = session.get('responses', [])

    responses.append(answer)
    session['responses'] = responses

    if question_num >= len(surveys[survey_type].questions):
        return "Question not found", 404

    if question_num + 1 < len(surveys[survey_type].questions):
        next_question_num = question_num + 1
        return redirect(url_for('show_survey_questions', survey_type=survey_type, question_num=next_question_num))
    else:
        return redirect(url_for('survey_complete', survey_type=survey_type))
    
# Renders the survey completion page and removes responses from the session
@app.route('/survey_complete/<survey_type>')
def survey_complete(survey_type):
    if survey_type not in surveys:
        return "Survey not found", 404
    
    session.pop('responses', None)
    return render_template("complete.html", survey_type=survey_type)
