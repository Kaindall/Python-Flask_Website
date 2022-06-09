from asyncio import format_helpers
from threading import current_thread
from First_Site import app, database, bcrypt
from flask import render_template, url_for, request, flash, redirect
from First_Site.forms import FormLogin, FormCreateAcc, FormEditProfile
from First_Site.models import User
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image



@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/users')
@login_required
def users():
    user_list = User.query.all()
    return render_template('users.html', user_list=user_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    f_login = FormLogin()
    f_createacc = FormCreateAcc()
    print('Ok, here')
    if f_login.validate_on_submit() and 'btnsubmit_login' in request.form:
        user = User.query.filter_by(email=f_login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, f_login.password.data):
            login_user(user, remember=f_login.remember_login.data)
            flash(f'Login successfully! Welcome {f_login.email.data}', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Login failed. Email or password wrong.', 'alert-danger')
        
    if f_createacc.validate_on_submit() and 'btnsubmit_createaccount' in request.form:
        secure_pw = bcrypt.generate_password_hash(f_createacc.password.data)
        account = User(username=f_createacc.username.data, email=f_createacc.email.data, password=secure_pw)
        database.session.add(account)
        database.session.commit()
        flash(f'Account created, nice to meet you {f_createacc.username.data}.', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', f_login=f_login, f_createacc=f_createacc)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f'Logout successfuly! I hope see you later.', 'alert-success')
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    profile_img = url_for('static', filename=f'img_database/{current_user.profile_img}')
    return render_template('profile.html', profile_img=profile_img)

def save_photo(img):
    code = secrets.token_hex(8)
    name, type = os.path.splitext(img.filename)
    final_file = name + code + type
    complete_path = os.path.join(app.root_path, 'static/img_database', final_file)
    size = (400, 400)
    img_resized = Image.open(img)
    img_resized.thumbnail(size)
    img_resized.save(complete_path)
    return final_file

def edit_knowledge(form):
    know_how = []
    for field in form:
        if 'knowledge' in field.name:
            if field.data:
                know_how.append(field.label.text)
    return ';'.join(know_how)
            

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def profile_edit():
    f_editprofile = FormEditProfile()
    if f_editprofile.validate_on_submit():
        current_user.email = f_editprofile.email.data
        current_user.username = f_editprofile.username.data
        if f_editprofile.profile_img.data:
            img_name = save_photo(f_editprofile.profile_img.data)
            current_user.profile_img = img_name
        current_user.knowledge = edit_knowledge(f_editprofile)
        database.session.commit()
        flash(f'Profile updated successfully!', 'alert-success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        f_editprofile.email.data = current_user.email
        f_editprofile.username.data = current_user.username
    profile_img = url_for('static', filename=f'img_database/{current_user.profile_img}')
    return render_template('profile_edit.html', profile_img=profile_img, f_editprofile = f_editprofile)

@app.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    return render_template('createpost.html')
