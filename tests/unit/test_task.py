from tasssktracker.tasssktracker.task import Task, Status, map_json_dict_to_task
from datetime import datetime
import pytest

def test_initialize_task(mocker):
    # Patch the datetime class and mock 'now' method used in the Task class
    mock_datetime = mocker.patch('tasssktracker.tasssktracker.task.datetime')
    
    # Mock the return value of datetime.now() to a specific datetime
    mock_now = mocker.Mock()
    mock_datetime.now.return_value = mock_now
    
    # Mock the strftime method on the mocked datetime object
    mock_now.strftime.return_value = '2024-12-11T12:46:41'
    
    # Create the task instance
    task = Task(1, 'desc')
    
    # Assert the task properties
    assert task.task_id == 1
    assert task.description == 'desc'
    assert task.status == Status.TODO
    assert task.created_at == '2024-12-11T12:46:41'
    assert task.updated_at == '2024-12-11T12:46:41'

def test_map_json_to_task_valid_data():
    # Given: a valid JSON-like dictionary
    data = {
        'id': 1,
        'description': 'Test task',
        'status': 'todo',
        'createdAt': '2024-12-11T12:46:41',
        'updatedAt': '2024-12-11T12:46:41'
    }

    # When: we map the JSON to a Task object
    task = map_json_dict_to_task(data)

    # Then: the Task object should have the correct attributes
    assert task.task_id == 1
    assert task.description == 'Test task'
    assert task.status == Status.TODO  # Assuming Status is an Enum with 'TODO'
    assert task.created_at == '2024-12-11T12:46:41'
    assert task.updated_at == '2024-12-11T12:46:41'


def test_map_json_to_task_missing_key():
    # Given: a JSON-like dictionary missing the 'description' key
    data = {
        'id': 1,
        'status': 'todo',
        'createdAt': '2024-12-11T12:46:41',
        'updatedAt': '2024-12-11T12:46:41'
    }

    # When: we attempt to map the JSON to a Task object
    with pytest.raises(SystemExit):  # sys.exit() is called on KeyError
        map_json_dict_to_task(data)


def test_map_json_to_task_missing_multiple_keys():
    # Given: a JSON-like dictionary missing 'description' and 'createdAt'
    data = {
        'id': 1,
        'status': 'todo',
        'updatedAt': '2024-12-11T12:46:41'
    }

    # When: we attempt to map the JSON to a Task object
    with pytest.raises(SystemExit):  # sys.exit() is called on KeyError
        map_json_dict_to_task(data)


