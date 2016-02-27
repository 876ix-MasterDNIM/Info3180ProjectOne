"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os, time, sys, logging
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename 
from form import SignUpForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Info3180'
if os.environ.get('INFO3180_URL') is None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3180@localhost/info3180'
else: 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['INFO3180_URL']

db = SQLAlchemy(app)
import models

###
# Routing for your application.
###

@app.route('/profile', methods=['GET', 'POST'])
def form():
    form = SignUpForm()
    if request.method == 'POST':
        username = request.form['username']
        fname = request.form['firstname']
        lname = request.form['lastname']
        age = request.form['age']
        gender = request.form['gender']
        userid = request.form['userid']
        image = request.files['image']
        created = time.strftime("%a, %-d %b %Y")
        filename = secure_filename(image.filename)
        image.save(os.path.join('static/uploads', filename))
        
        user = models.User(username, userid, fname, lname, age, gender, filename, created)
        
        db.session.add(user)
        db.session.commit()
        return '' + created + ' ' + lname + 'Fname' + fname
    else:
        return render_template('form.html', form=form)
        
@app.route('/profile/<userid>', methods=['POST', 'GET'])
def profile(userid):
    user = models.User.query.filter_by(userid=userid).first()
    if user:
        if request.headers['Content-Type'] == 'application/json' or request.method == 'POST':
            return jsonify({'userid': user.userid, 'username': user.username, 'image': user.image,
            'sex':user.gender, 'age': user.age, 'profile_add_on': user.created.strftime("%a, %-d %b %Y")})
        else:
            return render_template('profile.html', name = user.firstname + ' ' + user.lastname,
                time = user.created.strftime("%a, %-d %b %Y"), username = user.username, id = user.userid, gender = user.gender,
                age = user.age, img = user.image)
    return 'USER NOT FOUND'

@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    users = models.User.query.all()
    if users:
        formatted_users = []
        for user in users:
            formatted_users.append({'username': user.username, 'userid': user.userid})
        if request.headers['Content-Type'] == 'application/json' or request.method == 'POST':
            return jsonify(users=formatted_users)
        return render_template('profiles.html',users=formatted_users)
    return 'No user in database'

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
    app.run(debug=True,host='0.0.0.0',port=8080)
