#!/usr/bin/python3
""" Fetches Employee data from an API and displays on the page.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    data = {}
    filename = 'todo_all_employees.json'
    employees = requests.get('https://jsonplaceholder.typicode.com/users')\
        .json()

    for employee in employees:
        tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={'userId': employee.get('id')}).json()
        employee_data = []
        for task in tasks:
            employee_data.append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': employee.get('username')
            })
        data.update({employee.get('id'): employee_data})

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        json.dump(data, file)
