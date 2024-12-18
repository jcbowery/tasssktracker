from tasssktracker.tasssktracker.task import Task, Status
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

def test_update_changes_value_per_field(mocker):
    # Mock Task objects with task_id and description attributes
    task_mock1 = mocker.MagicMock()(spec=Task)
    task_mock2 = mocker.MagicMock()(spec=Task)
    task_mock3 = mocker.MagicMock()(spec=Task)
    
    task_mock1.task_id = 1
    task_mock1.description = 'Old description 1'
    
    task_mock2.task_id = 2
    task_mock2.description = 'Old description 2'
    
    task_mock3.task_id = 3
    task_mock3.description = 'Old description 3'
    
    tasks = [task_mock1, task_mock2, task_mock3]

    # Create TaskList with mocked tasks
    tl = TaskList(tasks)

    # Update the description of the task with task_id 2
    success = tl.update(2, 'description', 'my_new_desc')

    # Assert that the task's description has been updated
    task_mock2.description = 'my_new_desc'
    assert tl._task_list[1].description == 'my_new_desc', f"Expected description to be 'my_new_desc', but got {tl._task_list[1].description}"
    assert success

def test_delete_removes_task(mocker):
    # Mock Task objects with task_id and description attributes
    task_mock1 = mocker.MagicMock()(spec=Task)
    task_mock2 = mocker.MagicMock()(spec=Task)
    task_mock3 = mocker.MagicMock()(spec=Task)
    
    task_mock1.task_id = 1
    task_mock1.description = 'Old description 1'
    
    task_mock2.task_id = 2
    task_mock2.description = 'Old description 2'
    
    task_mock3.task_id = 3
    task_mock3.description = 'Old description 3'
    
    tasks = [task_mock1, task_mock2, task_mock3]

    # Create TaskList with mocked tasks
    tl = TaskList(tasks)

    success = tl.delete(2)

    assert success
    assert task_mock2 not in tl._task_list

def test_list_completed(mocker):
    # Mock Task objects with task_id and description attributes
    task_mock1 = mocker.MagicMock()(spec=Task)
    task_mock2 = mocker.MagicMock()(spec=Task)
    task_mock3 = mocker.MagicMock()(spec=Task)
    
    task_mock1.task_id = 1
    task_mock1.description = 'Old description 1'
    
    task_mock2.task_id = 2
    task_mock2.description = 'Old description 2'
    
    task_mock3.task_id = 3
    task_mock3.description = 'Old description 3'
    task_mock3.status = Status.DONE

    tl = TaskList([task_mock1, task_mock2, task_mock3])

    completed = tl.get_completed()

    assert len(completed) == 1
    assert completed[0].task_id == 3

def test_list_not_completed(mocker):
    # Mock Task objects with task_id and description attributes
    task_mock1 = mocker.MagicMock()(spec=Task)
    task_mock2 = mocker.MagicMock()(spec=Task)
    task_mock3 = mocker.MagicMock()(spec=Task)
    
    task_mock1.task_id = 1
    task_mock1.description = 'Old description 1'
    
    task_mock2.task_id = 2
    task_mock2.description = 'Old description 2'
    
    task_mock3.task_id = 3
    task_mock3.description = 'Old description 3'
    task_mock3.status = Status.DONE

    tl = TaskList([task_mock1, task_mock2, task_mock3])

    completed = tl.get_not_completed()

    assert len(completed) == 2
    assert completed[0].task_id == 1
    assert completed[1].task_id == 2

def test_list_in_progress(mocker):
    # Mock Task objects with task_id and description attributes
    task_mock1 = mocker.MagicMock()(spec=Task)
    task_mock2 = mocker.MagicMock()(spec=Task)
    task_mock3 = mocker.MagicMock()(spec=Task)
    
    task_mock1.task_id = 1
    task_mock1.description = 'Old description 1'
    
    task_mock2.task_id = 2
    task_mock2.description = 'Old description 2'
    
    task_mock3.task_id = 3
    task_mock3.description = 'Old description 3'
    task_mock3.status = Status.IN_PROGRESS

    tl = TaskList([task_mock1, task_mock2, task_mock3])

    completed = tl.get_in_progress()

    assert len(completed) == 1
    assert completed[0].task_id == 3
    

