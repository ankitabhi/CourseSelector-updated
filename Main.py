__author__ = 'pa'

from flask import Flask, render_template,request,session,flash,redirect,url_for

USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print "in login"
    error = None
    if request.method == 'POST':
        if request.form['login'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template("userHomePage.html")
    return render_template('index.html', error=error)



if __name__ == '__main__':
    app.run()