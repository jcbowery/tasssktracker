"""Module for wrappoing json import"""

import json
from sys import stderr
import sys


class JSON:
    """Wraps json import"""
    def __init__(self):
        self.json = json

    def load(self, path):
        """load data from file 

        Args:
            path (str): file location

        Returns:
            Union[List, Dict]: json info from file
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return self.json.load(file)
        except FileNotFoundError as e:
            print(f'Error: Failure to load file: {e}', file=stderr)
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format: {e}", file=stderr)
            sys.exit(1)

    def dump(self, obj, path):
        """Dumps json data into file

        Args:
            obj (Union[List, Dict]): json data
            path (str): path to file
        """
        try:
            with open(path, 'w', encoding='utf-8') as file:
                self.json.dump(obj, file)
        except Exception as e:
            print(f'Error: unknown error: {e}', file=stderr)
            sys.exit(1)
