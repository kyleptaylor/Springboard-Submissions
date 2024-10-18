
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, NumberRange, Optional, URL

class PetForm(FlaskForm):

    name = StringField('Pet Name', validators=[InputRequired(message="Name is Requiered")])
    # species = StringField('Pet Species', validators=[InputRequired(message="Species is Requiered")])
    species = SelectField('Pet Species', 
        choices=[('cat','Cat'),('dog', 'Dog'), ('porcupine', 'Porcupine')], 
        validators=[InputRequired(message="Species is Requiered")])

    photo_url = StringField('Photo URL', validators=[Optional(), URL(message="Must be a Valid URL")])
    age = IntegerField('Pet Age', validators=[Optional(), NumberRange(min=0, max=30, message="Must be a Valid Number (0-30)")])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Avaliable')