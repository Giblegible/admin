from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = TextField('Username',
                           validators=[Required(), Length(min=2, max=20)])
    email = TextField('Email',
                        validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[Required(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = TextField('Email',
                        validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')