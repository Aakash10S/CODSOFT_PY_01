import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        # Task input
        self.task_input = tk.Entry(self.root, width=30, font=("Arial", 14))
        self.task_input.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Arial", 12))
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Selected Task", command=self.delete_task, font=("Arial", 12))
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear All Tasks", command=self.clear_tasks, font=("Arial", 12))
        self.clear_button.pack(pady=5)

        # Task list
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_input.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "No task selected to delete!")

    def clear_tasks(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
            self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
