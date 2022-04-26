from flask import Flask, render_template, url_for

app=Flask(__name__)

user_list = ['Jax', 'Fiora', 'Gnar', 'Khazix', 'Viktor']

app.config['SECRET_KEY'] = 'I15NxqBiJ7R9nnUWhM3Nd5dCu3TUM8su'




@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/users')
def users():
    return render_template('users.html', user_list=user_list)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)