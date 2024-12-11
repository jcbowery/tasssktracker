"""Module for tasklist object"""

from datetime import datetime
from typing import Any, Dict, List

from tasssktracker.tasssktracker.task import Task

class TaskList:
    """Handling tasklist items"""
    def __init__(self, task_list: List[Task]):
        self._task_list = task_list

    def add(self, description):
        """add a new task to tasklist via a description

        Args:
            description (str)
        """
        new_id = self._generate_next_id()
        new_task = Task(new_id, description)
        self._task_list.append(new_task)

    def get_dict_list(self) -> List[Dict[str, Any]]:
        """convert the list of task to a list of dictionary objects

        Returns:
            List[Dict[str, Any]]: _description_
        """
        dict_list = []
        for task in self._task_list:
            dict_list.append(task.to_dict())
        return dict_list

    def _generate_next_id(self):
        task_id = 0
        for task in self._task_list:
            task_id = max(task_id, task.task_id)
        return task_id + 1

    def _get_current_time(self):
        return datetime.now()
