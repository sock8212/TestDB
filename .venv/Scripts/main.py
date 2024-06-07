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
# SELECT COURSE_NAME, STUDENT_ID, Courses.TEACHER_ID, CLASSROOM_ID, Teachers.FIRST_NAME2 FROM Courses, Teachers



#c.execute("""
#SELECT ID2, NAME FROM Courses
#JOIN Enrollments ON Courses.ID2 = COURSE_ID
#JOIN Students ON Enrollments.STUDENT_ID = ID
#WHERE Students.FIRST_NAME = 'Rosalia' AND Students.LAST_NAME = 'Arondel'
#""")
#print(c.fetchall())
# This commits all the changes to the database.
def QueryStudentKey(statement):
    global adding
    global a
    val = input(statement)
    try:
        inp = int(val)
    except ValueError:
        print("Enter a Integer value.")
        return
    c.execute("SELECT STUDENT_ID2 FROM Students")
    # print(c.fetchall())
    output = c.fetchall()
    existingResults = []
    for row in output:
        existingResults.append(str(row))
    print(existingResults)
    val2 = ("('" + val + "',)")
    print(val2)
    if val2 in existingResults:
        print("Enter a non-colliding Student ID, list of pre-existing IDs above")
        return
    adding.append(val)
    print("StudentID added.")
    a += 1
def QueryEnrollmentKey(statement):
    global adding
    global a
    val = input(statement)
    try:
        inp = int(val)
    except ValueError:
        print("Enter a Integer value.")
        return
    c.execute("SELECT ENROLLMENT_ID FROM Enrollments")
    # print(c.fetchall())
    output = c.fetchall()
    existingResults = []
    for row in output:
        existingResults.append(str(row))
    print(existingResults)
    val2 = ("('" + val + "',)")
    print(val2)
    if val2 in existingResults:
        print("Enter a non-colliding Enrollment ID, list of pre-existing IDs above")
        return
    adding.append(val)
    print("Enrollment ID added.")
    a += 1
def QueryTeacherKey(statement):
    global adding
    global a
    val = input(statement)
    try:
        inp = int(val)
    except ValueError:
        print("Enter a Integer value.")
        return
    c.execute("SELECT TEACHER_ID FROM Teachers")
    # print(c.fetchall())
    output = c.fetchall()
    existingResults = []
    for row in output:
        existingResults.append(str(row))
    print(existingResults)
    val2 = ("('" + val + "',)")
    print(val2)
    if val2 in existingResults:
        print("Enter a non-colliding Teacher ID, list of pre-existing IDs above")
        return
    adding.append(val)
    print("Teacher ID added.")
    a += 1
def QueryCourseKey(statement):
    global adding
    global a
    val = input(statement)
    try:
        inp = int(val)
    except ValueError:
        print("Enter a Integer value.")
        return
    c.execute("SELECT COURSE_ID FROM Courses")
    # print(c.fetchall())
    output = c.fetchall()
    existingResults = []
    for row in output:
        existingResults.append(str(row))
    print(existingResults)
    val2 = ("('" + val + "',)")
    print(val2)
    if val2 in existingResults:
        print("Enter a non-colliding Course ID, list of pre-existing IDs above")
        return
    adding.append(val)
    print("Course ID added.")
    a += 1

def QueryClassroomKey(statement):
    global adding
    global a
    val = input(statement)
    try:
        inp = int(val)
    except ValueError:
        print("Enter a Integer value.")
        return
    c.execute("SELECT CLASSROOM_ID FROM Classrooms")
    # print(c.fetchall())
    output = c.fetchall()
    existingResults = []
    for row in output:
        existingResults.append(str(row))
    print(existingResults)
    val2 = ("('" + val + "',)")
    print(val2)
    if val2 in existingResults:
        print("Enter a non-colliding Classroom ID, list of pre-existing IDs above")
        return
    adding.append(val)
    print("Course ID added.")
    a += 1


if __name__ == '__main__':
    enterFinished = 0
    while enterFinished == 0:
        type = input("What would you like to do?")
        if type == "Add student":
            adding = []
            a = 0
            while a == 0:
                QueryStudentKey("StudentID?")
            for b in ["First name", "Last name", "Date of birth", "Email"]:
                val = input(b + "?")
                adding.append(val)
                print(b + " added.")
            print("You have added the following")
            print(adding)
            c.execute(
            "INSERT INTO Students (STUDENT_ID2, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, EMAIL) VALUES (?, ?, ?, ?, ?);",
                (adding[0], adding[1], adding[2], adding[3], adding[4]))
        if type == "Add student to enrollment":
            adding = []
            a = 0
            while a == 0:
                QueryEnrollmentKey("EnrollmentID?")
            for b in ["Student ID", "Course ID", "Enrollment date"]:
                val = input(b + "?")
                adding.append(val)
                print(b + " added.")
            print("You have added the following")
            print(adding)
            c.execute(
            "INSERT INTO Enrollments (ENROLLMENT_ID, STUDENT_ID, COURSE_ID, ENROLLMENT_DATE) VALUES (?, ?, ?, ?);",
                (adding[0], adding[1], adding[2], adding[3]))
        if type == "Add teacher":
            adding = []
            a = 0
            while a == 0:
                QueryTeacherKey("TeacherID?")
            for b in ["First name", "Last name", "Department", "Email"]:
                val = input(b + "?")
                adding.append(val)
                print(b + " added.")
            print("You have added the following")
            print(adding)
            c.execute(
                "INSERT INTO Teachers (TEACHER_ID, FIRST_NAME2, LAST_NAME2, DEPARTMENT, EMAIL) VALUES (?, ?, ?, ?, ?);",
                (adding[0], adding[1], adding[2], adding[3], adding[4]))
        if type == "Modify Courses":
            adding = []
            a = 0
            while a == 0:
                QueryCourseKey("CourseID?")
            for b in ["Course name", "Description", "Credits", "Classroom ID", "Teacher ID"]:
                val = input(b + "?")
                adding.append(val)
                print(b + " added.")
            print("You have added the following")
            print(adding)
            c.execute(
                "INSERT INTO Courses (COURSE_ID, COURSE_NAME, DESCRIPTION, CREDITS, CLASSROOM_ID, TEACHER_ID) VALUES (?, ?, ?, ?, ?, ?);",
                (adding[0], adding[1], adding[2], adding[3], adding[4], adding[5]))
        if type == "Modify Classrooms":
            adding = []
            a = 0
            while a == 0:
                QueryClassroomKey("ClassroomID?")
            for b in ["Room number", "Capacity", "Building name"]:
                val = input(b + "?")
                adding.append(val)
                print(b + " added.")
            print("You have added the following")
            print(adding)
            c.execute(
                "INSERT INTO Classrooms (CLASSROOM_ID, ROOM_NUMBER, CAPACITY, BUILDING_NAME) VALUES (?, ?, ?, ?);",
                (adding[0], adding[1], adding[2], adding[3]))
        if type == "Courses by student name":
            firstname = input("First name?")
            lastname = input("Last name?")
            c.execute("""
            SELECT Courses.COURSE_NAME, Teachers.FIRST_NAME2, Teachers.LAST_NAME2, Classrooms.BUILDING_NAME FROM Courses
            JOIN Enrollments ON Enrollments.COURSE_ID = Courses.COURSE_ID
            JOIN Students ON Students.STUDENT_ID2 = STUDENT_ID
            JOIN Classrooms ON Classrooms.CLASSROOM_ID = Courses.CLASSROOM_ID
            JOIN Teachers ON Teachers.TEACHER_ID = Courses.TEACHER_ID
            WHERE Students.FIRST_NAME = ? AND Students.LAST_NAME = ?
            """, (firstname, lastname,))
            print(c.fetchall())
        if type == "Students by teacher name":
            firstname = input("First name?")
            lastname = input("Last name?")
            c.execute("""
            SELECT DISTINCT FIRST_NAME, LAST_NAME, STUDENT_ID2 FROM Students 
            JOIN Enrollments ON Enrollments.STUDENT_ID = Students.STUDENT_ID2
            JOIN Courses ON Courses.COURSE_ID = Enrollments.COURSE_ID
            JOIN Teachers ON Teachers.TEACHER_ID = Courses.TEACHER_ID
            WHERE Teachers.FIRST_NAME2 = ? AND Teachers.LAST_NAME2 = ?
            """, (firstname, lastname,))
            print(c.fetchall())
        else:
            print("Please enter one of the following: {Add student, Add student to enrollment, Add teacher, Modify Courses, Modify Classrooms, Courses by student name, Students by teacher name}")



connect.commit()

# This closes the connection to the database.
connect.close()