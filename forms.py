from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import StringField
from wtforms import SubmitField

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(),EqualTo('password')],)
    submit = SubmitField('Register')