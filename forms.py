from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCreateAcc(Form):
    username = StringField('Nickname', validators=[DataRequired()])
    email = StringField('E-mail adress', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    pw_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit_createaccount = SubmitField('Create Account')

class FormLogin(Form):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit_login = SubmitField('Login')