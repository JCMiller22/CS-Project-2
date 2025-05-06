class Task:
    """
    Represents a single task in the To-Do List Manager.

    Attributes:
        task_name (str): The name of the task.
        due_date (str): The due date of the task (YYYY-MM-DD format).
        priority (str): The priority of the task ('Low', 'Medium', or 'High').
        completed (bool): Whether the task has been completed.
    """

    def __init__(self, task_name: str, due_date: str, priority: str, completed: bool = False) -> None:
        """
        Initialize a new Task object.

        Args:
            task_name (str): Name of the task.
            due_date (str): Due date in 'YYYY-MM-DD' format.
            priority (str): Priority level ('Low', 'Medium', 'High').
            completed (bool, optional): Completion status. Defaults to False.
        """
        self._task_name = task_name
        self._due_date = due_date
        self._priority = priority
        self._completed = completed

    @property
    def task_name(self) -> str:
        """Get the task name."""
        return self._task_name

    @property
    def due_date(self) -> str:
        """Get the due date."""
        return self._due_date

    @property
    def priority(self) -> str:
        """Get the priority."""
        return self._priority

    @property
    def completed(self) -> bool:
        """Get the completion status."""
        return self._completed

    def mark_completed(self) -> None:
        """
        Mark the task as completed.
        """
        self._completed = True

    def to_list(self) -> list[str]:
        """
        Convert the task attributes to a list for CSV saving.

        Returns:
            list[str]: List containing task attributes as strings.
        """
        return [self._task_name, self._due_date, self._priority, str(self._completed)]
