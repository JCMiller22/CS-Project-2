# utils.py

import datetime

def validate_task_name(task_name: str) -> None:
    """
    Validate that the task name is not empty.

    Args:
        task_name (str): The name of the task.

    Raises:
        ValueError: If the task name is empty.
    """
    if not task_name.strip():
        raise ValueError("Task name cannot be empty.")


def validate_due_date(due_date: str) -> None:
    """
    Validate that the due date is in the correct 'YYYY-MM-DD' format.

    Args:
        due_date (str): The due date as a string.

    Raises:
        ValueError: If the due date format is incorrect or invalid.
    """
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in 'YYYY-MM-DD' format.")


def validate_priority(priority: str) -> None:
    """
    Validate that the priority is one of 'Low', 'Medium', or 'High'.

    Args:
        priority (str): The priority level.

    Raises:
        ValueError: If the priority is invalid.
    """
    if priority not in ['Low', 'Medium', 'High']:
        raise ValueError("Priority must be 'Low', 'Medium', or 'High'.")
