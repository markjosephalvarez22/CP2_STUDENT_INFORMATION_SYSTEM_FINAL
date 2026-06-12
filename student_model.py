import sqlite3


class StudentModel:

    def __init__(self):

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
