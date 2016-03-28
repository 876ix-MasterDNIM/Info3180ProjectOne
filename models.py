from app import db


class Wishlist(db.Model):
    __table__name = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric(10, 2))
    title = db.Column(db.String(255))
    description = db.Column(db.String(2000))
    item_url = db.Column(db.String(255))
    image_url = db.Column(db.String(300))
    userid = db.Column(db.Integer)
    
    def __init__(self, price, title, desc, item_url, img_url, userid):
        self.price = price
        self.title = title 
        self.description = desc 
        self.item_url = item_url
        self.image_url = img_url
        seld.userid = userid

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