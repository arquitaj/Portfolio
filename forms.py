from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class messageMe():
    name = StringField("Username: ", render_kw={"placeholder": "username"})
    email = StringField('Email')
    message = TextAreaField('Message')
    submit = SubmitField('Send Message')