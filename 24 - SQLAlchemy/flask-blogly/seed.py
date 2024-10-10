"""Seed file for Blogly."""

from models import db, User, Post, Tag, PostTag
from app import app

def seed_data():
    """Seed the database with initial data."""
    
    # Clear existing data
    db.drop_all()  # Be careful with this; it will remove all data!
    db.create_all()  # Create all tables

    # Create sample users
    user1 = User(first_name="Shrek", last_name="Ogre", image_url='https://lastfm.freetls.fastly.net/i/u/770x0/5342164d2994e7f3e0542905546defa5.jpg#5342164d2994e7f3e0542905546defa5')
    user2 = User(first_name="Fiona", last_name="Ogre", image_url='https://static1.srcdn.com/wordpress/wp-content/uploads/2024/09/fiona-in-ogre-form-looking-surprised-in-shrek-forever-after.jpg')
    user3 = User(first_name="Donkey", last_name="Talking", image_url='https://www.ft.com/__origami/service/image/v2/images/raw/http%3A%2F%2Fcom.ft.imagepublish.upp-prod-eu.s3.amazonaws.com%2Fc963f918-05a5-11e7-aa5b-6bb07f5c8e12?source=next-article&fit=scale-down&quality=highest&width=700&dpr=1')
    user4 = User(first_name="Lord", last_name="Farquaad", image_url='https://www.dictionary.com/e/wp-content/uploads/2018/03/Lord-Farquaad.jpg')

    db.session.add_all([user1, user2, user3, user4])
    db.session.commit()

    # Create sample posts
    post1 = Post(title="Shrek's Adventure", content="Shrek goes on an adventure!", user_id=user1.id)
    post2 = Post(title="Fiona's Story", content="Fiona shares her life story.", user_id=user2.id)
    post3 = Post(title="Donkey's Joke", content="Donkey tells a funny joke.", user_id=user3.id)

    db.session.add_all([post1, post2, post3])
    db.session.commit()

    # Create sample tags
    tag1 = Tag(name="Adventure")
    tag2 = Tag(name="Story")
    tag3 = Tag(name="Humor")

    db.session.add_all([tag1, tag2, tag3])
    db.session.commit()

    # Create PostTag relationships
    post_tag1 = PostTag(post_id=post1.id, tag_id=tag1.id)
    post_tag2 = PostTag(post_id=post2.id, tag_id=tag2.id)
    post_tag3 = PostTag(post_id=post3.id, tag_id=tag3.id)
    post_tag4 = PostTag(post_id=post1.id, tag_id=tag2.id)

    db.session.add_all([post_tag1, post_tag2, post_tag3, post_tag4])
    db.session.commit()

    print("Seed data added successfully!")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        seed_data()
