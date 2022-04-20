from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/sobre_nos')
def us():
    return render_template('sobre_nos')

if __name__ == '__main__':
    app.run(debug=True)