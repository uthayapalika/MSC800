import sqlite3


def create_connection():
    conn = sqlite3.connect("yoobee.db")
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            s_name TEXT NOT NULL,
            s_email TEXT NOT NULL UNIQUE
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            c_name TEXT NOT NULL,
            c_credits INTEGER
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lectures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            l_name TEXT NOT NULL,
            l_credits INTEGER
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES courses (id)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturer_courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lecturer_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (lecturer_id) REFERENCES lectures (id),
            FOREIGN KEY (course_id) REFERENCES courses (id)
        );
    ''')

    conn.commit()
    conn.close()
