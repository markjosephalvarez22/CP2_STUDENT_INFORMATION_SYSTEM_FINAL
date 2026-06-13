import sqlite3
import os


class StudentModel:

    def __init__(self):

        os.makedirs("database", exist_ok=True)
        self.conn = sqlite3.connect("database/students.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            student_id TEXT PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT,
            year_level TEXT
        )
        """)

        self.conn.commit()

    def add_student(self, student):

        self.cursor.execute("""
        INSERT INTO students VALUES (?, ?, ?, ?, ?)
        """, (
            student["student_id"],
            student["name"],
            student["age"],
            student["course"],
            student["year_level"]
        ))

        self.conn.commit()

    def get_all_students(self):

        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def search_student(self, student_id):

        self.cursor.execute(
            "SELECT * FROM students WHERE student_id=?",
            (student_id,)
        )

        return self.cursor.fetchone()

    def update_student(self, student_id, name, age, course, year_level):

        self.cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?, year_level=?
        WHERE student_id=?
        """, (name, age, course, year_level, student_id))

        self.conn.commit()

    def delete_student(self, student_id):

        self.cursor.execute(
            "DELETE FROM students WHERE student_id=?",
            (student_id,)
        )

        self.conn.commit()

    def count_students(self):

        self.cursor.execute("SELECT COUNT(*) FROM students")
        return self.cursor.fetchone()[0]
