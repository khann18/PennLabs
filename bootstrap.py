import os
import json
from app import db, DB_FILE
from models import *
# from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, render_template, flash, request

def create_user():
    josh =  User(username='josh', password='josh123', id=123, email='josh@example.com', firstname='Josh', lastname='Alsojosh')
    db.session.add(josh)
    db.session.commit()

def load_data():
    with open('clubs.json') as f:
        data = json.load(f)
        for club in data:
            new_club(club['code'], club['name'], club['description'], club['tags'])

def new_club(code, name, description, tags):
    new_tags = []
    if tags:
        new_tags = tags
        if isinstance(new_tags, str):
            new_tags = [tags]
    new_club = Club(code = code,
                    name = name,
                    description = description,
                    tags = new_tags)
    db.session.add(new_club)
    db.session.commit()

def add_favorite_club(username, club_name):
    user = User.query.filter_by(username=username).first()
    if user:
        curr_clubs = user.clubs
        club = Club.query.filter_by(name=club_name).first()
        if club:
            for c in curr_clubs:
                if c.name == club.name:
                    return "This club is already a favorite."
            user.clubs.append(club)
            db.session.add(user)
            db.session.commit()
            return "Club favorited."
        return "Invalid club name."
    return "Invalid username."


# No need to modify the below code.
if __name__ == '__main__':
    # Delete any existing database before bootstrapping a new one.
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)


    db.create_all()
    create_user()
    load_data()
    # add_favorite_club("josh", "Penn Memes Club")
    # user = User.query.filter_by(username="josh").first()
    # print(user.clubs)
    # print(User.query.all())
    # print(Club.query.all())

