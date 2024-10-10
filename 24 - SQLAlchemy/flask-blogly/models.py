"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """ User """
    __tablename__ = "users"

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

    @classmethod
    def get_all_users(cls):
        return cls.query.all()
    
    def __repr__(self):
        u = self
        return f"<User(id={u.id}, first_name={u.first_name}, last_name={u.last_name})>"

class Post(db.Model):
    """ Post """

    __tablename__ = "posts"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    
    title = db.Column(db.String, 
                      nullable=False)
    
    content = db.Column(db.Text, 
                        nullable=False)
    
    created_at = db.Column(db.DateTime, 
                           nullable=False, 
                           default=func.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref="posts")

    # Through table relationship:
    tags = db.relationship('Tag', secondary='post_tag', backref='posts')

    @classmethod
    def get_all_posts(cls):
        return cls.query.all()

    @classmethod
    def get_user_posts(cls, user_id):
        return cls.query.filter_by(user_id = user_id).all()

    def __repr__(self):
        p = self
        return f"<Post(id={p.id}, title={p.title}, user_id={p.user_id})>"

class Tag(db.Model):
    ''' Tag'n Stuff '''

    __tablename__ = 'tags'

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)

    name = db.Column(db.Text,
                    nullable=False, 
                    unique=True)
    
    @classmethod
    def get_all_tags(cls):
        return cls.query.all()
    
class PostTag(db.Model):
    ''' Through table for connection from post to tag '''

    __tablename__ = 'post_tag'

    post_id = db.Column(db.Integer, 
                        db.ForeignKey('posts.id'), 
                        primary_key=True)
    
    tag_id = db.Column(db.Integer, 
                       db.ForeignKey('tags.id'), 
                       primary_key=True)