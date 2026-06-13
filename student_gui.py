import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from student_model import StudentModel


class StudentGUI:

    def __init__(self, root):
        self.root = root
        self.model = StudentModel()

        self.root.title("Student Information System")
        self.root.geometry("860x560")
        self.root.minsize(760, 500)

        self.student_id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.year_level_var = tk.StringVar()
        self.search_var = tk.StringVar()
        self.total_var = tk.StringVar(value="Total: 0")

        self.build_layout()
        self.load_students()

    def build_layout(self):
        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(
            main_frame,
            text="Student Information System",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(anchor=tk.W, pady=(0, 12))

        content = ttk.Frame(main_frame)
        content.pack(fill=tk.BOTH, expand=True)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(0, weight=1)

        form_frame = ttk.LabelFrame(content, text="Student Form", padding=12)
        form_frame.grid(row=0, column=0, sticky="ns", padx=(0, 12))

        self.add_form_field(form_frame, "Student ID", self.student_id_var, 0)
        self.add_form_field(form_frame, "Name", self.name_var, 1)
        self.add_form_field(form_frame, "Age", self.age_var, 2)
        self.add_form_field(form_frame, "Course", self.course_var, 3)
        self.add_form_field(form_frame, "Year Level", self.year_level_var, 4)

        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(12, 0))
        button_frame.columnconfigure((0, 1), weight=1)

        ttk.Button(button_frame, text="Add", command=self.add_student).grid(row=0, column=0, sticky="ew", padx=(0, 4), pady=4)
        ttk.Button(button_frame, text="Update", command=self.update_student).grid(row=0, column=1, sticky="ew", padx=(4, 0), pady=4)
        ttk.Button(button_frame, text="Delete", command=self.delete_student).grid(row=1, column=0, sticky="ew", padx=(0, 4), pady=4)
        ttk.Button(button_frame, text="Clear", command=self.clear_form).grid(row=1, column=1, sticky="ew", padx=(4, 0), pady=4)

        table_area = ttk.Frame(content)
        table_area.grid(row=0, column=1, sticky="nsew")
        table_area.rowconfigure(1, weight=1)
        table_area.columnconfigure(0, weight=1)

        search_frame = ttk.Frame(table_area)
        search_frame.grid(row=0, column=0, sticky="ew", pady=(0, 8))
        search_frame.columnconfigure(1, weight=1)

        ttk.Label(search_frame, text="Search ID").grid(row=0, column=0, padx=(0, 8))
        ttk.Entry(search_frame, textvariable=self.search_var).grid(row=0, column=1, sticky="ew", padx=(0, 8))
        ttk.Button(search_frame, text="Search", command=self.search_student).grid(row=0, column=2, padx=(0, 8))
        ttk.Button(search_frame, text="Show All", command=self.load_students).grid(row=0, column=3)

        columns = ("student_id", "name", "age", "course", "year_level")
        self.tree = ttk.Treeview(table_area, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("student_id", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("age", text="Age")
        self.tree.heading("course", text="Course")
        self.tree.heading("year_level", text="Year Level")

        self.tree.column("student_id", width=100, anchor=tk.CENTER)
        self.tree.column("name", width=180)
        self.tree.column("age", width=70, anchor=tk.CENTER)
        self.tree.column("course", width=150)
        self.tree.column("year_level", width=110, anchor=tk.CENTER)
        self.tree.grid(row=1, column=0, sticky="nsew")
        self.tree.bind("<<TreeviewSelect>>", self.fill_form_from_selection)

        scrollbar = ttk.Scrollbar(table_area, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        footer = ttk.Frame(table_area)
        footer.grid(row=2, column=0, sticky="ew", pady=(8, 0))
        footer.columnconfigure(0, weight=1)
        ttk.Label(footer, textvariable=self.total_var).grid(row=0, column=0, sticky=tk.W)
        ttk.Button(footer, text="Count Students", command=self.show_count).grid(row=0, column=1, sticky=tk.E)

    def add_form_field(self, parent, label, variable, row):
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky=tk.W, pady=5)
        ttk.Entry(parent, textvariable=variable, width=24).grid(row=row, column=1, sticky=tk.EW, pady=5)

    def get_form_data(self):
        student_id = self.student_id_var.get().strip()
        name = self.name_var.get().strip()
        age_text = self.age_var.get().strip()
        course = self.course_var.get().strip()
        year_level = self.year_level_var.get().strip()

        if not all([student_id, name, age_text, course, year_level]):
            messagebox.showwarning("Missing Information", "Please fill in all fields.")
            return None

        try:
            age = int(age_text)
        except ValueError:
            messagebox.showwarning("Invalid Age", "Age must be a number.")
            return None

        return {
            "student_id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "year_level": year_level
        }

    def load_students(self):
        self.search_var.set("")
        self.display_students(self.model.get_all_students())
        self.update_total()

    def display_students(self, students):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for student in students:
            self.tree.insert("", tk.END, values=student)

    def add_student(self):
        student = self.get_form_data()
        if student is None:
            return

        try:
            self.model.add_student(student)
        except sqlite3.IntegrityError:
            messagebox.showerror("Duplicate ID", "A student with this ID already exists.")
            return

        self.clear_form()
        self.load_students()
        messagebox.showinfo("Success", "Student added.")

    def update_student(self):
        student = self.get_form_data()
        if student is None:
            return

        if not self.model.search_student(student["student_id"]):
            messagebox.showerror("Not Found", "Student ID was not found.")
            return

        self.model.update_student(
            student["student_id"],
            student["name"],
            student["age"],
            student["course"],
            student["year_level"]
        )
        self.load_students()
        messagebox.showinfo("Success", "Student updated.")

    def delete_student(self):
        student_id = self.student_id_var.get().strip()
        if not student_id:
            messagebox.showwarning("Missing ID", "Enter or select a student ID first.")
            return

        if not self.model.search_student(student_id):
            messagebox.showerror("Not Found", "Student ID was not found.")
            return

        if not messagebox.askyesno("Confirm Delete", "Delete this student?"):
            return

        self.model.delete_student(student_id)
        self.clear_form()
        self.load_students()
        messagebox.showinfo("Success", "Student deleted.")

    def search_student(self):
        student_id = self.search_var.get().strip()
        if not student_id:
            self.load_students()
            return

        student = self.model.search_student(student_id)
        if not student:
            self.display_students([])
            messagebox.showinfo("Not Found", "No student found with that ID.")
            return

        self.display_students([student])
        self.fill_form(student)

    def show_count(self):
        total = self.model.count_students()
        self.total_var.set(f"Total: {total}")
        messagebox.showinfo("Student Count", f"Total students: {total}")

    def update_total(self):
        self.total_var.set(f"Total: {self.model.count_students()}")

    def fill_form_from_selection(self, event=None):
        selection = self.tree.selection()
        if not selection:
            return

        values = self.tree.item(selection[0], "values")
        self.fill_form(values)

    def fill_form(self, student):
        self.student_id_var.set(student[0])
        self.name_var.set(student[1])
        self.age_var.set(student[2])
        self.course_var.set(student[3])
        self.year_level_var.set(student[4])

    def clear_form(self):
        self.student_id_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.course_var.set("")
        self.year_level_var.set("")
        self.tree.selection_remove(self.tree.selection())


def main():
    root = tk.Tk()
    app = StudentGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
