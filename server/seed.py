#!/usr/bin/env python3
#server/seed.py
# server/seed.py

from faker import Faker
from random import choice as rc


from app import app
from models import db, Pet

fake = Faker()
species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

with app.app_context():
    # Clear existing records (optional, but recommended during development)
    Pet.query.delete()

    # Create 10 fake pet records
    pets = []
    for _ in range(10):
        name = fake.first_name()
        type = rc(species)
        pet = Pet(name=name, species=type)
        pets.append(pet)

    # Add to database session and commit
    db.session.add_all(pets)
    
    db.session.commit()

    print("Database seeded successfully!")
