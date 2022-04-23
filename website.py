from flask import Flask, render_template
app=Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)