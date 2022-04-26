from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Lenght, Email, EqualTo

class Form_CreateAcc(FlaskForm):
    username = StringField('Nickname', validator=[DataRequired()])
    email = StringField('E-mail adress', validator=[DataRequired(), Email()])
    password = PasswordField('Password', validator=[DataRequired(), Lenght(6, 20)])
    pw_confirmation = PasswordField('Confirm Password', validator=[DataRequired(), EqualTo('password')])
    submit_createaccount = SubmitField('Create Account')

class Form_Login(FlaskForm):
    email = StringField('E-mail', validator=[DataRequired(), Email()])
    password = PasswordField('Password', validator=[DataRequired(), Lenght(6, 20)])
    submit_login = SubmitField('Login')