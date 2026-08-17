import sqlite3
import os
#connect db
db_path = os.path.join(os.path.dirname(__file__), "school.db")
connection = sqlite3.connect(db_path)
if connection:
    print(connection)
    print("Connection to database successful")
else:
    print("Connection to database failed")    

cursor = connection.cursor()
#create students table
command1 = '''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   
    s_name TEXT NOT NULL,
    s_email TEXT NOT NULL UNIQUE
    )'''
cursor.execute(command1)

#create courses table
command2 = '''CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    c_name TEXT NOT NULL,
    c_credits INTEGER,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
)'''
cursor.execute(command2)


#insert sample data into students table
sample_students = [ "John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]
for student in sample_students:
    cursor.execute("INSERT OR IGNORE INTO students (s_name, s_email) VALUES (?, ?)", (student, student.replace(" ", "").lower() + "@example.com"))  

#insert sample data into courses table
sample_courses = [
    ("Mathematics", 3, 1),
    ("Physics", 4, 2),
    ("Chemistry", 3, 3),
    ("Biology", 4, 4)
]
for course in sample_courses:
    cursor.execute("INSERT OR IGNORE INTO courses (c_name, c_credits, student_id) VALUES (?, ?, ?)", course)

connection.commit()
select_query = "SELECT * FROM students"
cursor.execute(select_query)
students = cursor.fetchall()

print("Tables created successfully")
print("Students:")
for student in students:
    print(student)

connection.close()