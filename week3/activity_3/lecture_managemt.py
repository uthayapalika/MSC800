try:
    from .database import create_connection
except ImportError:
    from database import create_connection

import sqlite3


def add_lecture(name, credits):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lectures (l_name, l_credits) VALUES (?, ?)", (name, credits))
        conn.commit()
        print(" Lecture added successfully.")
    except sqlite3.IntegrityError:
        print(" Lecture name must be unique.")
    conn.close()


def view_lectures():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lectures")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_lecture(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lectures WHERE l_name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_lecture(lecture_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lectures WHERE id = ?", (lecture_id,))
    conn.commit()
    conn.close()
    print("🗑️ Lecture deleted.")
