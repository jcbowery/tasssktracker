from tasssktracker.tasssktracker.task import Task
from tasssktracker.tasssktracker.tasklist import TaskList
from typing import List, Dict, Any

def test_initialize_tasklist(mocker):
    task1 = mocker.Mock()
    task2 = mocker.Mock()
    task3 = mocker.Mock()
    tasks = [task1, task2, task3]

    tl = TaskList(tasks)

    assert tl._task_list == tasks

def test_generate_id_gives_next_highest_id(mocker):
    task1 = mocker.Mock()
    task2 = mocker.Mock()
    task3 = mocker.Mock()
    task1.task_id = 1
    task2.task_id = 2
    task3.task_id = 3
    tasks = [task1, task2, task3]
    tl = TaskList(tasks)

    new_id = tl._generate_next_id()

    assert new_id == 4

def test_add_appends_new_task_item(mocker):
    mocker.patch('tasssktracker.tasssktracker.tasklist.TaskList._generate_next_id', return_value=4)
    mocker.patch('tasssktracker.tasssktracker.tasklist.Task')
    
    task1 = mocker.Mock()
    task2 = mocker.Mock()
    task3 = mocker.Mock()
    tasks = [task1, task2, task3]
    tl = TaskList(tasks)

    tl.add('new_desc')

    assert len(tl._task_list) == 4

def test_get_dict_list_returns_dict_list(mocker):
    # Mock the Task class
    task_mock = mocker.Mock(spec=Task)  # Mocking the Task class using the spec to ensure it's correctly mocked
    task_mock.to_dict.return_value = {}  # Mock the to_dict method to return an empty dictionary
    
    # Create a list of mocked task objects
    tasks = [task_mock, task_mock, task_mock]
    
    # Initialize TaskList with the mocked tasks
    tl = TaskList(tasks)

    # Call get_dict_list method
    dl = tl.get_dict_list()

    # Assert that dl is a list
    assert isinstance(dl, list), "Object should be a list"
    
    # Assert that each item in the list is a dictionary
    for item in dl:
        assert isinstance(item, dict), f"Item {item} should be a dictionary"