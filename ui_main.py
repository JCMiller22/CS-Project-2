# ui_main.py

import tkinter as tk
from tkinter import ttk

class ToDoListGUI:
    """
    Class responsible for building the tkinter UI layout.
    It does not implement business logic — that is handled in controllers.
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Initialize the GUI layout.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("700x500")

        # Input frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        # Task name
        tk.Label(self.input_frame, text="Task Name:").grid(row=0, column=0, padx=5, pady=5)
        self.task_entry = tk.Entry(self.input_frame, width=30)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        # Due date
        tk.Label(self.input_frame, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.input_frame, width=30)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        # Priority
        tk.Label(self.input_frame, text="Priority:").grid(row=2, column=0, padx=5, pady=5)
        self.priority_combo = ttk.Combobox(self.input_frame, values=["Low", "Medium", "High"], state="readonly")
        self.priority_combo.grid(row=2, column=1, padx=5, pady=5)
        self.priority_combo.current(1)  # Default: Medium

        # Add Task Button
        self.add_button = tk.Button(self.input_frame, text="Add Task")
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Task List (Table)
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=10)

        self.task_table = ttk.Treeview(self.table_frame, columns=("Name", "Due Date", "Priority", "Completed"), show="headings")
        self.task_table.heading("Name", text="Task Name")
        self.task_table.heading("Due Date", text="Due Date")
        self.task_table.heading("Priority", text="Priority")
        self.task_table.heading("Completed", text="Completed")
        self.task_table.column("Name", width=200)
        self.task_table.column("Due Date", width=120)
        self.task_table.column("Priority", width=100)
        self.task_table.column("Completed", width=80)
        self.task_table.pack()

        # Buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        self.delete_button = tk.Button(self.buttons_frame, text="Delete Selected")
        self.delete_button.grid(row=0, column=0, padx=10)

        self.mark_complete_button = tk.Button(self.buttons_frame, text="Mark as Completed")
        self.mark_complete_button.grid(row=0, column=1, padx=10)

        self.save_button = tk.Button(self.buttons_frame, text="Save Tasks")
        self.save_button.grid(row=0, column=2, padx=10)

        self.load_button = tk.Button(self.buttons_frame, text="Load Tasks")
        self.load_button.grid(row=0, column=3, padx=10)

        # Status Label
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.pack(pady=5)
