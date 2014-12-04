__author__ = 'pa'

from flask import Flask, render_template,request,session,flash,redirect,url_for
from register import Register
from Login import loginAccount

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
    r = Register()
    majorList = r.getMajors()
    courseList = r.getCourses()
    return render_template('register.html',majors = majorList,courses = courseList)

@app.route('/login', methods=['GET', 'POST'])
def login():
    print "in login"
    error = None
    l = loginAccount()
    username = request.form['login']
    password = request.form['password']
    if request.method == 'POST':
        if not l.ifUserExists(username,password):
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            dtls = l.getStudDtls(username)
            d =  dtls[0]
            print d['id']
            courseDtls = l.getCourseDtls(d['id'])
            print courseDtls

            return render_template("userHomePage.html",studentDtls=dtls,courses = courseDtls)
    return render_template('index.html', error=error)

@app.route('/home',methods=['GET','POST'])
def homepage():
    print "in homepage"
    if request.method == 'POST':
        email =  request.form['email']
        password = request.form['password']

    return render_template("userHomePage.html")

if __name__ == '__main__':
    app.run()