import sqlite3


class StudentModel:

    def __init__(self):

        self.conn = sqlite3.connect("database/students.db")
        self.cursor = self.conn.cursor()
