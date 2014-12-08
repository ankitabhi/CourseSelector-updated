__author__ = 'pa'

import sqlite3

conn =  sqlite3.connect('courseSelector.db',check_same_thread=False)

class Register:
    pass

    def getMajors(self):
        cursor = conn.execute('SELECT major_code,major_name FROM majors_lookup order by id')
        entries = [dict(code=row[0], name=row[1]) for row in cursor.fetchall()]
        return entries

    def getCourses(self):
        cursor = conn.execute('SELECT course_code,course_name FROM course_lookup order by major_code')
        entries = [dict(code=row[0], name=row[1]) for row in cursor.fetchall()]
        return entries

    def insertAccDtls(self,accountDtls):

        cursor = conn.execute('insert into student_account_details(title,first_name,middle_name,last_name,email,birth_date,password) values (?,?,?,?,?,?,?)',
                              [accountDtls['title'],
                               accountDtls['fName'],
                               accountDtls['mName'],
                               accountDtls['lName'],
                               accountDtls['email'],
                               accountDtls['birthdate'],
                               accountDtls['password']])
        conn.commit()
        last_id = cursor.lastrowid

        courseDetails = accountDtls['courseDtls']
        cursor = conn.execute('insert into student_academic_details(degree,major,semester) values (?,?,?)',
                              [courseDetails['degree'],
                               courseDetails['major'],
                               courseDetails['semester']])
        conn.commit()

        coursesTaken = courseDetails['coursesTaken']
        coursesCodeTaken = courseDetails['coursesCodeTaken']
        print coursesTaken

        coursesNameList = coursesTaken.split("\n")
        coursesCodeList = coursesCodeTaken.split("\n")
        for i in range(len(coursesNameList)-1):
            cursor = conn.execute('insert into student_course_details(id,course_name,course_code,semester) values (?,?,?,?)',
                                  [last_id,
                                   coursesNameList[i],
                                   coursesCodeList[i],
                                   courseDetails['semester']])

        conn.commit()
        return "inserted"

    def checkIfUserExists(self,username):
        cursor = conn.execute('SELECT * from student_account_details s where s.email="'+username+'"')
        cur = cursor.fetchall()
        if cur.__len__()>0:
            return True
        else:
            return False


    def updateStudCourses(self,courseName,courseCode,semester,user):
        cursor = conn.execute('select id from student_account_details where email = "'+user+'"')
        cur = cursor.fetchone()
        id =  cur[0]

        cursor = conn.execute('insert into student_course_details(id,course_name,course_code,semester) values (?,?,?,?)',
                              [id,
                              courseName,
                              courseCode,
                              semester])
        conn.commit()
        return "inserted"

    def deleteStudCourse(self,code,user):
        cursor = conn.execute('select id from student_account_details where email = "'+user+'"')
        cur = cursor.fetchone()
        id =  cur[0]

        query = "delete from student_course_details where course_code =\""+ code + "\" and id ="+str(id)
        print query
        cursor = conn.execute(query)
        conn.commit()
        return "deleted"

    def getOtherCourses(self,id):
        cursor = conn.execute('select c.course_code,c.course_name from course_lookup c where c.course_code not in ( select s.course_code from student_course_details s where s.id= '+str(id)+')')
        entries = [dict(code=row[0], name=row[1]) for row in cursor.fetchall()]
        return entries
