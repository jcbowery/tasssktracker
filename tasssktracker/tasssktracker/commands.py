import click
from tasssktracker.tasssktracker.json_wrapper import JSON
from tasssktracker.tasssktracker.tasklist import TaskList, create_task_list
from tasssktracker.tasssktracker.task import Task, map_json_dict_to_task, Status

@click.command()
@click.argument("desc", type=click.STRING)
def add(desc):
    json = JSON()
    json_dict = json.load('Tasks/tasks.json')
    task_list = create_task_list(json_dict)
    task_list.add(desc)
    json.dump(task_list.get_dict_list(), 'Tasks/tasks.json')

@click.command()
@click.argument("task_id", type=click.INT)
@click.argument("desc", type=click.STRING)
def update_description(task_id, desc):
    json = JSON()
    json_dict = json.load('Tasks/tasks.json')
    task_list = create_task_list(json_dict)
    task_list.update(task_id, 'description', desc)
    json.dump(task_list.get_dict_list(), 'Tasks/tasks.json')

@click.command()
@click.argument("task_id", type=click.INT)
@click.argument("status", type=click.STRING)
def update_status(task_id, status):
    # Convert the status string to its corresponding Status Enum value
    try:
        status = Status[status.upper()]  # Convert to uppercase to match Enum naming convention
    except KeyError:
        raise click.BadParameter(f"Invalid status '{status}'. Valid statuses are: {', '.join([s.name for s in Status])}.")

    json = JSON()
    json_dict = json.load('Tasks/tasks.json')
    task_list = create_task_list(json_dict)
    task_list.update(task_id, 'status', status)
    json.dump(task_list.get_dict_list(), 'Tasks/tasks.json')

@click.command()
@click.argument("task_id", type=click.INT)
def delete(task_id):
    json = JSON()
    json_dict = json.load('Tasks/tasks.json')
    task_list = create_task_list(json_dict)
    task_list.delete(task_id)
    json.dump(task_list.get_dict_list(), 'Tasks/tasks.json')

@click.command()
def list_all():
    json = JSON()
    json_dict = json.load('Tasks/tasks.json')
    task_list = create_task_list(json_dict)
    click.echo(task_list)

@click.command()
def list_completed():
    json = JSON()
    json_dict = json.load('Tasks/tasks.json')
    task_list = create_task_list(json_dict)
    click.echo(task_list.get_completed())

@click.command()
def list_not_completed():
    json = JSON()
    json_dict = json.load('Tasks/tasks.json')
    task_list = create_task_list(json_dict)
    click.echo(task_list.get_not_completed())

@click.command()
def list_in_progress():
    json = JSON()
    json_dict = json.load('Tasks/tasks.json')
    task_list = create_task_list(json_dict)
    click.echo(task_list.get_in_progress())
    
