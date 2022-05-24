from First_Site import app, database, bcrypt
from flask import render_template, url_for, request, flash, redirect
from First_Site.forms import FormLogin, FormCreateAcc
from First_Site.models import User
from flask_login import login_user, logout_user

user_list = ['Diana', 'Zeus', 'Jubileu']

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/users')
def users():
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
def logout():
    logout_user()
    flash(f'Logou successfuly! I hope see you later.', 'alert-success')
    return redirect(url_for('home'))

app.route('/profile')
def profile():
    render_template('profile.html')

app.route('/post/create')
def create_post():
    render_template('createpost.html')

