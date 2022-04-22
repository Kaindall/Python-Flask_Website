from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/contact')
def contact():
    return render_template('contact')

@app.route('/users')
def users
    return render_template('users')

if __name__ == '__main__':
    app.run(debug=True)