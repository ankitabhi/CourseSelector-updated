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


