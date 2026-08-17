try:
    from .database import create_connection
except ImportError:
    from database import create_connection

import sqlite3


def add_course(name, credits):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (c_name, c_credits) VALUES (?, ?)", (name, credits))
        conn.commit()
        print(" Course added successfully.")
    except sqlite3.IntegrityError:
        print(" Course name must be unique.")
    conn.close()


def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_course(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE c_name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_course(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()
    print("🗑️ Course deleted.")
