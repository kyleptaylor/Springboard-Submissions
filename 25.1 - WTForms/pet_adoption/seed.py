"""Seed file to make sample data for db."""

from models import db, Pet
from app import app

try:
    # Drop and recreate the tables
    print("Dropping all tables...")
    db.drop_all()
    print("Creating all tables...")
    db.create_all()
    print("Deleting queries for all tables...")
    Pet.query.delete()

    # Seed data
    pets = [
        Pet(
            name="Bella",
            species="Dog",
            photo_url="https://www.thesprucepets.com/thmb/vyCNFRTRbPCgoiST3xWwTEJoE1A=/1280x0/filters:no_upscale():strip_icc()/shelter-training-115895910-resized-56a26a8d3df78cf772755f29.jpg",
            age=3,
            notes="Loves playing fetch",
            available=True
        ),
        Pet(
            name="Whiskers",
            species="Cat",
            photo_url="https://www.operationkindness.org/wp-content/uploads/blog-june-adopt-shelter-cat-month-operation-kindness.jpg",
            age=2,
            notes="Enjoys climbing",
            available=True
        ),
        Pet(
            name="Goldie",
            species="Fish",
            photo_url="https://dingo.care2.com/pictures/greenliving/1409/1408115.large.jpg",
            age=1,
            notes="Needs a spacious tank",
            available=True
        ),
        Pet(
            name="Spike",
            species="Lizard",
            photo_url="https://www.arl-iowa.org/webres/Image/beardeddragon.jpg",
            age=5,
            notes="Loves basking under the heat lamp",
            available=False
        ),
        Pet(
            name="Chirpy",
            species="Bird",
            photo_url="https://www.cdc.gov/healthy-pets/media/images/2024/04/Pet-bird-in-cage.jpg",
            age=4,
            notes="Can mimic words",
            available=True
        ),
        Pet(
            name="Pete",
            species="Kanagroo",
            age=12,
            notes="Hops on things",
            available=True
        )
    ]

    # Add all pets and commit
    db.session.add_all(pets)
    db.session.commit()
    print("Database seeded successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    db.session.rollback()

finally:
    db.session.close()