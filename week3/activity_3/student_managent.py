try:
    from .database import create_connection
except ImportError:
    from database import create_connection

import sqlite3


def add_student(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (s_name, s_email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" Student added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()


def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE s_name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted.")
