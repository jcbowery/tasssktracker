import click
from tasssktracker.tasssktracker.commands import add, update_description, update_status, delete, list_all, list_completed, list_not_completed, list_in_progress
from tasssktracker.tasssktracker.json_wrapper import JSON
from pathlib import Path

@click.group()
def cli():
    # Ensure the "Tasks" directory exists
    p = Path('Tasks')
    p.mkdir(exist_ok=True)

    # Path to the tasks.json file
    tasks_file = p / 'tasks.json'

    # If tasks.json doesn't exist, create it with an empty array
    json = JSON()
    if not tasks_file.exists():
        with tasks_file.open('w') as f:
            f.write("[]")


cli.add_command(add)
cli.add_command(update_description)
cli.add_command(update_status)
cli.add_command(delete)
cli.add_command(list_all)
cli.add_command(list_completed)
cli.add_command(list_not_completed)
cli.add_command(list_in_progress)

if __name__ == '__main__':
    cli()
