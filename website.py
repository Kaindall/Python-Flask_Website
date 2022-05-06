from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCreateAcc, FormLogin


app=Flask(__name__)
app.config['SECRET_KEY'] = 'I15NxqBiJ7R9nnUWhM3Nd5dCu3TUM8su'

user_list = ['Jax', 'Fiora', 'Gnar', 'Khazix', 'Viktor']




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
        flash(f'Account created, nice to meet you {f_createacc.username.data}.', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', f_login=f_login, f_createacc=f_createacc)




if __name__ == '__main__':
    app.run(debug=True)