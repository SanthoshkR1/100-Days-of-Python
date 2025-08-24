import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    email = email_entry.get()

    if not name or not age or not grade or not email:
        messagebox.showwarning("Input Error", "Please fill out all fields")
        return

    # You can store or process the data here
    print("Student Details:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    print(f"Email: {email}")
    messagebox.showinfo("Submitted", "Student information submitted successfully!")

# Set up the window
root = tk.Tk()
root.title("Student Form")

# Labels and Entries
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Grade").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Email").grid(row=3, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
grade_entry = tk.Entry(root)
email_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry.grid(row=1, column=1, padx=10, pady=5)
grade_entry.grid(row=2, column=1, padx=10, pady=5)
email_entry.grid(row=3, column=1, padx=10, pady=5)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()