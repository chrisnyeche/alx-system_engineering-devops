#!/usr/bin/python3
""" Fetches Employee data from an API and displays on the page.
"""
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employee_id)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': employee_id}).json()
    completed = [task for task in tasks if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'
          .format(employee.get('name'), len(completed), len(tasks)))
    for task in completed:
        print('\t {}'.format(task.get('title')))
