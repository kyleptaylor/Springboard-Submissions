from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ Pet Model """

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True, server_default='true')
    

    def __repr__(self):
        return f"<Pet: {self.id} {self.name} {self.species}>"