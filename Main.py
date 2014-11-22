__author__ = 'pa'

from flask import request, Flask, render_template, jsonify


app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()