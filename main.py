# main.py

import tkinter as tk
from tkinter import messagebox
from ui_main import ToDoListGUI
from models import Task
import controllers

def main() -> None:
    """
    Initialize and run the To-Do List Manager application.
    """
    root = tk.Tk()
    gui = ToDoListGUI(root)
    task_list: list[Task] = []

    def refresh_table() -> None:
        """
        Clear and repopulate the task table from the task_list.
        """
        gui.task_table.delete(*gui.task_table.get_children())
        for i, task in enumerate(task_list):
            gui.task_table.insert('', 'end', iid=i, values=(task.task_name, task.due_date, task.priority, task.completed))

    def add_task_handler() -> None:
        """
        Handle adding a new task from input fields.
        """
        try:
            name = gui.task_entry.get()
            date = gui.date_entry.get()
            priority = gui.priority_combo.get()

            controllers.add_task(task_list, name, date, priority)
            refresh_table()
            gui.status_label.config(text="Task added successfully.", fg="green")
            gui.task_entry.delete(0, tk.END)
            gui.date_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", str(e))
            gui.status_label.config(text="Failed to add task.", fg="red")

    def delete_task_handler() -> None:
        """
        Handle deleting the selected task.
        """
        try:
            selected = gui.task_table.selection()
            if not selected:
                raise ValueError("No task selected.")

            index = int(selected[0])
            controllers.delete_task(task_list, index)
            refresh_table()
            gui.status_label.config(text="Task deleted successfully.", fg="green")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            gui.status_label.config(text="Failed to delete task.", fg="red")

    def mark_complete_handler() -> None:
        """
        Handle marking a task as completed.
        """
        try:
            selected = gui.task_table.selection()
            if not selected:
                raise ValueError("No task selected.")

            index = int(selected[0])
            task_list[index].mark_completed()
            refresh_table()
            gui.status_label.config(text="Task marked as completed.", fg="green")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            gui.status_label.config(text="Failed to mark task.", fg="red")

    def save_tasks_handler() -> None:
        """
        Save tasks to CSV.
        """
        try:
            controllers.save_tasks_to_csv(task_list)
            gui.status_label.config(text="Tasks saved to CSV.", fg="green")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            gui.status_label.config(text="Failed to save tasks.", fg="red")

    def load_tasks_handler() -> None:
        """
        Load tasks from CSV.
        """
        try:
            task_list.clear()
            task_list.extend(controllers.load_tasks_from_csv())
            refresh_table()
            gui.status_label.config(text="Tasks loaded from CSV.", fg="green")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            gui.status_label.config(text="Failed to load tasks.", fg="red")

    # Connect GUI buttons to handlers
    gui.add_button.config(command=add_task_handler)
    gui.delete_button.config(command=delete_task_handler)
    gui.mark_complete_button.config(command=mark_complete_handler)
    gui.save_button.config(command=save_tasks_handler)
    gui.load_button.config(command=load_tasks_handler)

    # Load existing tasks
    load_tasks_handler()

    root.mainloop()

if __name__ == "__main__":
    main()
