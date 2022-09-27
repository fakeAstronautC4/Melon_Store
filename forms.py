from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
# from flask_bcrypt import Bcrypt



class LoginForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])



