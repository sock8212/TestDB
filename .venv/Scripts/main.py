# We need sqlite3 to run all of our database software
import sqlite3
import csv

# If Database.db didn't exist here it would create it.
connect = sqlite3.connect('Database.db')
classrooms = sqlite3.connect('classrooms_with_pk.csv')
courses = sqlite3.connect('courses_with_pk.csv')
enrollments = sqlite3.connect('enrollments_with_pk.csv')
students = sqlite3.connect('students_with_pk.csv')
teachers = sqlite3.connect('teachers_with_pk.csv')

c = connect.cursor()

c.execute("DROP TABLE IF EXISTS 'classrooms';")
c.execute("DROP TABLE IF EXISTS 'courses';")
c.execute("DROP TABLE IF EXISTS 'enrollments';")
c.execute("DROP TABLE IF EXISTS 'students';")
c.execute("DROP TABLE IF EXISTS 'teachers';")

c.execute("""
CREATE TABLE Classrooms (
    CLASSROOM_ID BLOB NOT NULL PRIMARY KEY,
    ROOM_NUMBER BLOB NOT NULL,
    CAPACITY BLOB NOT NULL,
    BUILDING_NAME BLOB NOT NULL
);
""")

c.execute("""
CREATE TABLE Courses (
    COURSE_ID BLOB NOT NULL PRIMARY KEY,
    COURSE_NAME BLOB NOT NULL,
    DESCRIPTION BLOB NOT NULL,
    CREDITS BLOB NOT NULL,
    CLASSROOM_ID BLOB NOT NULL,
    TEACHER_ID BLOB NOT NULL
);
""")



c.execute("""
CREATE TABLE Enrollments (
    ENROLLMENT_ID BLOB NOT NULL PRIMARY KEY,
    STUDENT_ID BLOB NOT NULL,
    COURSE_ID BLOB NOT NULL,
    ENROLLMENT_DATE BLOB NOT NULL
);
""")

c.execute("""
CREATE TABLE Students (
    STUDENT_ID2 BLOB NOT NULL PRIMARY KEY,
    FIRST_NAME BLOB NOT NULL,
    LAST_NAME BLOB NOT NULL,
    DATE_OF_BIRTH BLOB NOT NULL,
    EMAIL BLOB NOT NULL
);
""")

c.execute("""
CREATE TABLE Teachers (
    TEACHER_ID BLOB NOT NULL PRIMARY KEY,
    FIRST_NAME2 BLOB NOT NULL,
    LAST_NAME2 BLOB NOT NULL,
    DEPARTMENT BLOB NOT NULL,
    EMAIL BLOB NOT NULL
);
""")

global enterFinished
with open('classrooms_with_pk.csv', 'r') as file:
    reader = csv.reader(file)
    # For each row in the document it will add the row to the table list
    for row in reader:
        c.execute("INSERT INTO Classrooms (CLASSROOM_ID, ROOM_NUMBER, CAPACITY, BUILDING_NAME) VALUES (?, ?, ?, ?);", (row[0], row[1], row[2], row[3]))

with open('courses_detailed_with_ids.csv', 'r') as file:
    reader = csv.reader(file)
    # For each row in the document it will add the row to the table list
    for row in reader:
        c.execute("INSERT INTO Courses (COURSE_ID, COURSE_NAME, DESCRIPTION, CREDITS, CLASSROOM_ID, TEACHER_ID) VALUES (?, ?, ?, ?, ?, ?);", (row[0], row[1], row[2], row[3], row[4], row[5]))

with open('enrollments_with_pk.csv', 'r') as file:
    reader = csv.reader(file)
    # For each row in the document it will add the row to the table list
    for row in reader:
        c.execute("INSERT INTO Enrollments (ENROLLMENT_ID, STUDENT_ID, COURSE_ID, ENROLLMENT_DATE) VALUES (?, ?, ?, ?);", (row[0], row[1], row[2], row[3]))

with open('students_with_pk.csv', 'r') as file:
    reader = csv.reader(file)
    # For each row in the document it will add the row to the table list
    for row in reader:
        c.execute("INSERT INTO Students (STUDENT_ID2, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, EMAIL) VALUES (?, ?, ?, ?, ?);", (row[0], row[1], row[2], row[3], row[4]))

with open('teachers_with_pk.csv', 'r') as file:
    reader = csv.reader(file)
    # For each row in the document it will add the row to the table list
    for row in reader:
        c.execute("INSERT INTO Teachers (TEACHER_ID, FIRST_NAME2, LAST_NAME2, DEPARTMENT, EMAIL) VALUES (?, ?, ?, ?, ?);", (row[0], row[1], row[2], row[3], row[4]))

#initial: courses with room and teacher based on student name
#initial: list of students based on teacher name
#intiial: hardcode first, then add interface. do documentation during periods
#later: change data types to more appropriate types when hardcoded checks are done
#later: add interface
#later: add diagram explaining dev process
#JOIN Courses ON Enrollments.COURSE_ID = ID2
#WHERE Courses.NAME = 'Maths' Enrollments.STUDENT_ID (SELECT DISTINCT STUDENT_ID FROM Enrollments)

c.execute("""
SELECT COURSE_NAME, STUDENT_ID, TEACHER_ID, CLASSROOM_ID FROM Courses 
JOIN Enrollments ON Enrollments.COURSE_ID = Courses.COURSE_ID

JOIN Students ON Students.STUDENT_ID2 = STUDENT_ID
WHERE Students.FIRST_NAME = 'Michael' AND Students.LAST_NAME = 'Hill'
""")
print(c.fetchall())
c.execute("""
SELECT DISTINCT FIRST_NAME, LAST_NAME, STUDENT_ID2 FROM Students 
JOIN Enrollments ON Enrollments.STUDENT_ID = Students.STUDENT_ID2
JOIN Courses ON Courses.COURSE_ID = Enrollments.COURSE_ID
JOIN Teachers ON Teachers.TEACHER_ID = Courses.TEACHER_ID
WHERE Teachers.FIRST_NAME2 = 'Karen' AND Teachers.LAST_NAME2 = 'Martin' 
""")
print(c.fetchall())
#c.execute("""
#SELECT ID2, NAME FROM Courses
#JOIN Enrollments ON Courses.ID2 = COURSE_ID
#JOIN Students ON Enrollments.STUDENT_ID = ID
#WHERE Students.FIRST_NAME = 'Rosalia' AND Students.LAST_NAME = 'Arondel'
#""")
#print(c.fetchall())
# This commits all the changes to the database.
if __name__ == '__main__':
    enterFinished = 0
    while enterFinished == 0:
        type = input("What table would you like to modify?")
        if type in ["Student"]:
            a = 0
            adding = []
            while a == 0:
                val = input("studentID?")
                try:
                    inp = str(val)
                except ValueError:
                    adding.append(val)
                    print("StudentID added.")
                    a+= 1

connect.commit()

# This closes the connection to the database.
connect.close()