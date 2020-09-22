from app import db

# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

clubs = db.Table('clubs',
    db.Column('club_code', db.String(80), db.ForeignKey('club.code'), primary_key=True),
    db.Column('user_username', db.String(80), db.ForeignKey('user.username'), primary_key=True)
)

class Club(db.Model):
    code = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    _tags = db.Column(db.Text)

    @property
    def tags(self):
        return [x for x in self._tags.split(';')]

    @tags.setter
    def tags(self, tags):
        self._tags = ";".join(tags)
        for tag in tags:
            t = Tag.query.filter_by(tag=tag).first()
            if t:
                t.count = t.count + 1
            else:
                t = Tag(tag=tag, count=1)
            db.session.add(t)
            db.session.commit()

    def __repr__(self):
        return '<Club: %r>' % self.name

    def serialize(self):
        return {"code": self.code,
                "name": self.name}


class User(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    clubs = db.relationship('Club', secondary=clubs, lazy='subquery',
        backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<User: %r>' % self.username

    def get_profile(self):
        return {"username": self.username,
                "first name": self.firstname,
                "last name" : self.lastname,
                "favorited clubs" : [c.serialize() for c in self.clubs]}

class Tag(db.Model):
    tag = db.Column(db.String(120), primary_key=True)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Tag: %r' % self.tag

    def serialize(self):
        return {"tag": self.tag,
                "count": self.count}