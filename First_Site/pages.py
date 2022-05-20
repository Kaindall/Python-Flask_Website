from First_Site import app
from flask import render_template, url_for, request, flash, redirect
from First_Site.forms import FormLogin, FormCreateAcc
from First_Site.models import User

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
        flash(f'Login successfully! Welcome {f_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if f_createacc.validate_on_submit() and 'btnsubmit_createaccount' in request.form:
        account = User(username=f_createacc.username.data, email=f_createacc.email.data, password=f_createacc.password.data)
        flash(f'Account created, nice to meet you {f_createacc.username.data}.', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', f_login=f_login, f_createacc=f_createacc)