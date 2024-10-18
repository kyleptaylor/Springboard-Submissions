from flask import Flask , request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenPotPie"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# Added for app context
app.app_context().push() 

connect_db(app)

@app.route('/')
def show_home():

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/pet/<int:pet_id>')
def show_pet(pet_id):
    """ Show details for pet based on id """
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet.html', pet=pet)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()

        flash(f"Created new pet: {name} the {species}")
        return redirect ('/')
    else:
        return render_template('add_pet.html', form = form)
    
@app.route('/pet/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Edited: {pet.name} the {pet.species}")
        return redirect (f'/pet/{pet_id}')
    else:
        return render_template('edit_pet.html', form=form, pet=pet)
    
@app.route('/pet/<int:pet_id>/delete')
def delete_pet(pet_id):
    """ Delete details for pet based on id """
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    
    flash(f"Deleted: {pet.name} the {pet.species}")
    return redirect ('/')