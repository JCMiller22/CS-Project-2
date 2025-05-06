import csv
import os
from typing import List
from models import Task
from utils import validate_task_name, validate_due_date, validate_priority

def add_task(task_list: List[Task], task_name: str, due_date: str, priority: str) -> None:
    """
    Add a new task to the task list after validating inputs.

    Args:
        task_list (List[Task]): The list of existing tasks.
        task_name (str): The name of the new task.
        due_date (str): The due date of the task in 'YYYY-MM-DD' format.
        priority (str): The priority of the task ('Low', 'Medium', 'High').

    Raises:
        ValueError: If any input is invalid.
    """
    validate_task_name(task_name)
    validate_due_date(due_date)
    validate_priority(priority)

    new_task = Task(task_name, due_date, priority)
    task_list.append(new_task)


def delete_task(task_list: List[Task], index: int) -> None:
    """
    Delete a task from the task list by its index.

    Args:
        task_list (List[Task]): The list of existing tasks.
        index (int): The index of the task to delete.

    Raises:
        IndexError: If the index is out of range.
    """
    if index < 0 or index >= len(task_list):
        raise IndexError("Invalid task index.")

    del task_list[index]


def save_tasks_to_csv(task_list: List[Task], file_path: str = "data/tasks.csv") -> None:
    """
    Save all tasks to a CSV file.

    Args:
        task_list (List[Task]): The list of existing tasks.
        file_path (str): The path to the CSV file. Defaults to 'data/tasks.csv'.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Task Name", "Due Date", "Priority", "Completed"])
        for task in task_list:
            writer.writerow(task.to_list())


def load_tasks_from_csv(file_path: str = "data/tasks.csv") -> List[Task]:
    """
    Load tasks from a CSV file into a list.

    Args:
        file_path (str): The path to the CSV file. Defaults to 'data/tasks.csv'.

    Returns:
        List[Task]: List of tasks loaded from the file.
    """
    tasks: List[Task] = []

    if not os.path.exists(file_path):
        return tasks  # No file to load

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row
        for row in reader:
            if len(row) == 4:
                task_name, due_date, priority, completed_str = row
                completed = completed_str.lower() == "true"
                task = Task(task_name, due_date, priority, completed)
                tasks.append(task)

    return tasks
