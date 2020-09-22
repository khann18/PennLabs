from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

DB_FILE = "clubreview.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE}"
db = SQLAlchemy(app)

from models import *
from bootstrap import create_user, add_favorite_club, new_club

@app.route('/')
def main():
    return "Welcome to Penn Club Review!"

@app.route('/api/home')
def home():
    return render_template('home.html')

@app.route('/api')
def api():
    return jsonify({"message": "Welcome to the Penn Club Review API!."})

@app.route('/api/user/<uname>', methods=["GET"])
def profile(uname):
    return jsonify(User.query.get(uname).get_profile())

@app.route('/api/clubs', methods=['POST', 'GET'])
def get_clubs():
    if request.method == 'POST':
        not_valid = valid_club(request)
        if not_valid:
            return not_valid
        else:
            new_club(request.form['code'], request.form['name'], request.form['description'], request.form['tags'])
            return "Club added."
    if request.method == 'GET':
        searchword = request.args.get('search', '')
        if searchword:
            return jsonify([x.serialize() for x in Club.query.filter(Club.name.contains(searchword))])
    # return jsonify([x.serialize() for x in Club.query.all()])

@app.route('/api/clubs/<clubcode>', methods=['PATCH'])
def modify_club(clubcode):
    if request.method == 'PATCH':
        club = Club.query.filter_by(code=clubcode).first()
        if club:
            req = request.get_json()
            for k, v in req.items():
                if k != code:
                    club.k = v
            db.session.add(club)
            db.session.commit()
            return "Club updated."
        return "Club does not exist."

@app.route('/api/<clubname>/favorite', methods=["POST"])
def favorite(clubname):
    add_favorite_club(request.form['user'], clubname)

@app.route('/api/tag_count', methods=["GET"])
def show_num_tags():
    return jsonify([x.serialize() for x in Tag.query.all()])

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

def valid_club(request):
    to_return = ""
    if request.form['name'] and request.form['code'] and request.form['description']:
        if Club.query.filter_by(code=request.form['code']).first():
            to_return += "Club code already taken. "
        if Club.query.filter_by(name=request.form['name']).first():
            to_return += "Club name already taken."
        return to_return
    to_return += "Club code, name, and description are mandatory fields."
    return to_return

@app.route("/add_club", methods=['GET', 'POST'])
def add_club_route():
    return render_template('add_club.html')

@app.route('/api/search_clubs')
def search_clubs():
    return render_template('search_clubs.html')

@app.route('/api/search_users')
def search_users():
    return render_template('search_users.html')
                  

if __name__ == '__main__':
    app.run()
