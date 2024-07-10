import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

# Create the main application window
root = tk.Tk()
root.title("Student Management System")
root.geometry("1200x800")  # Average laptop screen size

# Set up the main frame
main_frame = tk.Frame(root, bg="lightgreen")
main_frame.pack(fill="both", expand=True)

# Header Label
header = tk.Label(main_frame, text="Student Management System", bg="green", fg="white", font=("Arial", 24))
header.pack(pady=20)

# Create a form frame
form_frame = tk.Frame(main_frame, bg="lightgreen")
form_frame.pack(pady=20)

# Student Name
name_label = tk.Label(form_frame, text="Name:", bg="lightgreen", font=("Arial", 14))
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(form_frame, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Roll Number
roll_label = tk.Label(form_frame, text="Roll Number:", bg="lightgreen", font=("Arial", 14))
roll_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
roll_entry = tk.Entry(form_frame, font=("Arial", 14))
roll_entry.grid(row=1, column=1, padx=10, pady=10)

# Class
class_label = tk.Label(form_frame, text="Class:", bg="lightgreen", font=("Arial", 14))
class_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
class_entry = tk.Entry(form_frame, font=("Arial", 14))
class_entry.grid(row=2, column=1, padx=10, pady=10)

# Section
section_label = tk.Label(form_frame, text="Section:", bg="lightgreen", font=("Arial", 14))
section_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
section_entry = tk.Entry(form_frame, font=("Arial", 14))
section_entry.grid(row=3, column=1, padx=10, pady=10)

# Button Frame
button_frame = tk.Frame(main_frame, bg="lightgreen")
button_frame.pack(pady=20)

students = []

def add_student():
    name = name_entry.get()
    roll_number = roll_entry.get()
    student_class = class_entry.get()
    section = section_entry.get()
    
    if name and roll_number and student_class and section:
        student = {"Name": name, "Roll Number": roll_number, "Class": student_class, "Section": section}
        students.append(student)
        save_students()
        messagebox.showinfo("Success", f"Student {name} added successfully")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required")

def clear_entries():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    section_entry.delete(0, tk.END)

def show_students():
    if students:
        display_text = ""
        for student in students:
            display_text += f"Name: {student['Name']}, Roll Number: {student['Roll Number']}, Class: {student['Class']}, Section: {student['Section']}\n"
        messagebox.showinfo("Student Details", display_text)
    else:
        messagebox.showinfo("No Students", "No students to display")

def save_students():
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Roll Number", "Class", "Section"])
        for student in students:
            writer.writerow([student['Name'], student['Roll Number'], student['Class'], student['Section']])

def load_students():
    try:
        with open('students.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        pass

def update_student():
    roll_number = roll_entry.get()
    for student in students:
        if student['Roll Number'] == roll_number:
            student['Name'] = name_entry.get()
            student['Class'] = class_entry.get()
            student['Section'] = section_entry.get()
            save_students()
            messagebox.showinfo("Success", f"Student {roll_number} updated successfully")
            clear_entries()
            return
    messagebox.showwarning("Not Found", "Student with the given roll number not found")

def delete_student():
    roll_number = roll_entry.get()
    for student in students:
        if student['Roll Number'] == roll_number:
            students.remove(student)
            save_students()
            messagebox.showinfo("Success", f"Student {roll_number} deleted successfully")
            clear_entries()
            return
    messagebox.showwarning("Not Found", "Student with the given roll number not found")

# Add Student Button
add_button = tk.Button(button_frame, text="Add Student", bg="green", fg="white", font=("Arial", 14), command=add_student)
add_button.grid(row=0, column=0, padx=20, pady=10)

# Show Students Button
show_button = tk.Button(button_frame, text="Show Students", bg="green", fg="white", font=("Arial", 14), command=show_students)
show_button.grid(row=0, column=1, padx=20, pady=10)

# Update Student Button
update_button = tk.Button(button_frame, text="Update Student", bg="green", fg="white", font=("Arial", 14), command=update_student)
update_button.grid(row=0, column=2, padx=20, pady=10)

# Delete Student Button
delete_button = tk.Button(button_frame, text="Delete Student", bg="green", fg="white", font=("Arial", 14), command=delete_student)
delete_button.grid(row=0, column=3, padx=20, pady=10)

# Load students from file
load_students()

# Run the main loop
root.mainloop()
