from flask.ext.wtf import Form
from flask.ext.wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField, HiddenField
from wtforms.validators import DataRequired


class SignUpForm(Form):
    username = StringField('Username: ', validators=[DataRequired()])
    firstname = StringField('Firstname: ', validators=[DataRequired()])
    lastname = StringField('Lastname: ', validators=[DataRequired()])
    age = IntegerField('Age: ', validators=[DataRequired()])
    gender = SelectField('Gender: ', choices=[('Male', 'Male'), ('Female', 'Female')])
    image = FileField('Profile Picture: ',
                      validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images Only')
                                  ])
    userid = HiddenField()
    submit = SubmitField('Submit')

