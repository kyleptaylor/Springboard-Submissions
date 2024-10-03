"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """ User """
    __tablename__ = "users"

    def __repr__(self):
        u = self
        return f"<User(id={u.id}, first_name={u.first_name}, last_name={u.last_name})>"

    @classmethod
    def get_all_users(cls):
        return cls.query.filter(User).all()

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    
    first_name = db.Column(db.String(30), 
                           nullable=False)
    
    last_name = db.Column(db.String(30), 
                          nullable=False)
    
    image_url = db.Column(db.String, 
                          nullable=True,
                          default="https://lastfm.freetls.fastly.net/i/u/770x0/5342164d2994e7f3e0542905546defa5.jpg#5342164d2994e7f3e0542905546defa5")