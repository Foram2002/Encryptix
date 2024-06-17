import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to mark a selected task as completed
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.itemconfig(selected_task_index, {'fg': 'gray'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Create the main application window
root = tk.Tk()
root.title("To-Do List Application")

# Create GUI elements
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

task_listbox = tk.Listbox(root, width=60, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=0, padx=10, pady=10)

complete_button = tk.Button(root, text="Mark Completed", command=mark_completed)
complete_button.grid(row=2, column=1, padx=10, pady=10)

# Start the main tkinter event loop
root.mainloop()
