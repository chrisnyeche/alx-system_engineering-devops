#!/usr/bin/python3
""" Fetches Employee data from an API and displays on the page.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employee_id)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': employee_id}).json()
    filename = '{}.json'.format(employee_id)
    data = []
    for task in tasks:
        data.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': employee.get('username')
        })
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        json.dump({employee_id: data}, file)
