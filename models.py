from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    userid = db.Column(db.String(10), unique=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    image = db.Column(db.String(255))
    created = db.Column(db.DateTime())

    def __init__(self, user, id, fname, lname, age, gender, image, created):
        self.username = user
        self.userid = id
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.gender = gender
        self.image = image
        self.created = created