__author__ = 'pa'

from flask import Flask, render_template,request,session,flash,redirect,url_for,jsonify
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
    print request.method

    print "1"
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['password']
        print "2"
        if not l.ifUserExists(username,password):
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            session['username'] = request.form['login']
            print session['username']
            flash('You were logged in')
            dtls = l.getStudDtls(username)
            d =  dtls[0]
            print d['id']
            courseDtls = l.getCourseDtls(d['id'])
            print courseDtls
            r = Register()
            courseList = r.getCourses()
            return render_template("userHomePage.html",studentDtls=dtls,courses = courseDtls,username = username,allcourses = courseList)
    else:
        print "in this one"
        if session['logged_in'] == True:
            print request.args.get('username')
            dtls = l.getStudDtls()
            d =  dtls[0]
            print d['id']
            courseDtls = l.getCourseDtls(d['id'])
            print courseDtls
            r = Register()
            courseList = r.getCourses()
            return render_template("userHomePage.html",studentDtls=dtls,courses = courseDtls,username = username,allcourses = courseList)

    return render_template('index.html', error=error)

@app.route('/home',methods=['GET','POST'])
def homepage():
    print "in homepage"
    print str(request.method)
    email = ""
    if request.method == 'POST':
        print "POST"
        r = Register()
        exists = r.checkIfUserExists(request.form['email'])
        print "ooooo"
        print exists
        if not exists:
            accountDetails = {"email":request.form['email'],
                          "password":request.form['password'],
                          "title": request.form['title'],
                          "fName": request.form['first_name'],
                          "mName":request.form['middle_name'],
                          "lName":request.form['last_name'],
                          "gender" : request.form['sex'],
                          "city" : request.form['city'],
                          "state" : request.form['state'],
                          "street" : request.form['street'],
                          "country" : request.form['country'],
                          "birthdate" : request.form['birthdate'],
                          "courseDtls" :{"degree":request.form['degree'],
                                         "major":request.form['major'],
                                         "semester":request.form['semester'],
                                         "coursesTaken":request.form['courses'],
                                         "coursesCodeTaken":request.form['coursesCode']}}
            q =  accountDetails['courseDtls']
            print q['coursesTaken']
            email = request.form['email']
            result = r.insertAccDtls(accountDetails)
            print "result" + result
            if(result == "inserted"):
                l = loginAccount()
                dtls = l.getStudDtls(accountDetails['email'])
                d =  dtls[0]
                courseDtls = l.getCourseDtls(d['id'])
                r = Register()
                courseList = r.getCourses()
                return render_template("userHomePage.html",studentDtls=dtls,courses = courseDtls,usernames = email,allcourses = courseList)
        else:
            error = "Email ID already exists"
            return render_template('register.html',error = error)

    else:

        print "in GET" + str('admin')
        l = loginAccount()
        dtls = l.getStudDtls(email)
        d =  dtls[0]
        courseDtls = l.getCourseDtls(d['id'])
        return render_template("userHomePage.html",studentDtls=dtls,courses = courseDtls)



@app.route('/logout',methods=['GET','POST'])
def logout():
    if request.method == 'POST':
        session['logged_in'] == False
        return render_template('index.html')
    return render_template('index.html')

@app.route('/feedback',methods=['GET','POST'])
def feedback():
    print "in feedback" + session['username']
    user = session['username']
    l = loginAccount()
    dtls = l.getStudDtls(user)
    d =  dtls[0]
    courseDtls = l.getCourseDtls(d['id'])
    return render_template('feedbackform.html',courses = courseDtls,username = user )


@app.route('/homepage',methods=['GET','POST'])
def home():
    print request.method
    print "in homepage email" + session['username']
    user = session['username']
    l = loginAccount()
    dtls = l.getStudDtls(user)
    d =  dtls[0]
    courseDtls = l.getCourseDtls(d['id'])
    r = Register()
    courseList = r.getOtherCourses(d['id'])
    if request.method == 'GET':
        if not request.args.get('courseName') == None:
            courseName = request.args.get('courseName')
            courseCode = request.args.get('courseCode')
            semester = request.args.get('semester')
            print courseName + semester
            reg = Register()
            result = reg.updateStudCourses(courseName,courseCode,semester,user)
            print result
            if result == "inserted":
                dtls = l.getStudDtls(user)
                d =  dtls[0]
                courseDtls = l.getCourseDtls(d['id'])
                r = Register()
                courseList = r.getCourses()
                message = {"msg":"success"}
                return jsonify(message)
        elif not request.args.get('code') == None:
            courseCode = request.args.get('code')
            print courseCode
            reg = Register()
            result = reg.deleteStudCourse(courseCode,user)
            print result
            if result == "deleted":
                dtls = l.getStudDtls(user)
                d =  dtls[0]
                courseDtls = l.getCourseDtls(d['id'])
                r = Register()
                courseList = r.getCourses()
                message = {"msg":"success"}
                return jsonify(message)

    return render_template("userHomePage.html",studentDtls=dtls,courses = courseDtls,allcourses = courseList)

@app.route('/planner',methods=['GET','POST'])
def planner():
    return render_template("planner.html")

if __name__ == '__main__':
    app.run()
