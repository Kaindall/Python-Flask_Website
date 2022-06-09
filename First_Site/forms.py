from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from First_Site.models import User
from flask_login import current_user

class FormCreateAcc(FlaskForm):
    username = StringField('Nickname', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    pw_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    btnsubmit_createaccount = SubmitField('Create Account')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-mail already registered. Log in or try again with another.')
        
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Nickname already registered. Log in or try again with another.')
            

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    remember_login = BooleanField('Remember me')
    btnsubmit_login = SubmitField('Login')
    
class FormEditProfile(FlaskForm):
    username = StringField('Nickname', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    profile_img = FileField('Update Picture', validators=[FileAllowed(['jpg','png','jpeg'])])
    
    knowledge1 = BooleanField ('Knowledge 1')
    knowledge2 = BooleanField ('Knowledge 2')
    knowledge3 = BooleanField ('Knowledge 3')
    knowledge4 = BooleanField ('Knowledge 4')
    knowledge5 = BooleanField ('Knowledge 5')
    knowledge6 = BooleanField ('Knowledge 6')
    
    btnsubmit_editprofile = SubmitField('Confirm')
    
    def validate_email(self, email):
        if current_user.email != email.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('E-mail already registered. Change refused!')