
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional

class AddPetForm(FlaskForm):

    name = StringField('Employee Name', validators=[InputRequired(message="Name is Requiered")])
    species = StringField('Species', validators=[InputRequired(message="Species is Requiered")])
    photo_url = StringField('Photo URL')
    age = IntegerField('Age')
    notes = TextAreaField('Notes')
    available = BooleanField('Avaliable')