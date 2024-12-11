"""Module for task dataclass and creating it"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any
from datetime import datetime
import sys


class Status(Enum):
    """Status enum"""

    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


@dataclass
class Task:
    """Dataclass for task"""

    task_id: int
    description: str
    status: Status = Status.TODO
    created_at: str = ""
    updated_at: str = ""

    def __post_init__(self):
        # Convert string to Status enum
        if isinstance(self.status, str):
            self.status = Status(self.status)

        # Mock datetime and set 'created_at' and 'updated_at'
        if not self.created_at:
            self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        if not self.updated_at:
            self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    def to_dict(self) -> Dict[str, Any]:
        """Returns the object as a dictionary

        Returns:
            Dict
        """
        return {
            "id": self.task_id,
            "description": self.description,
            "updatedAt": self.updated_at,
            "createdAt": self.created_at,
            "status": self.status.value,
        }


def map_json_dict_to_task(data: Dict[str, Any]) -> Task:
    """Create Task object from dictionary

    Args:
        data (Dict): _description_

    Returns:
        _type_: _description_
    """
    try:
        return Task(
            task_id=data["id"],
            description=data["description"],
            status=data["status"],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
        )
    except KeyError as e:
        print(f"Error: missing key value: {e}")
        sys.exit(1)
