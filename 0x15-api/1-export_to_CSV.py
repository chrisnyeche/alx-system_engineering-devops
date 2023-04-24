#!/usr/bin/python3
""" Fetches Employee data from an API and displays on the page.
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employee_id)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': employee_id}).json()
    filename = '{}.csv'.format(employee_id)
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            data = (employee_id, employee.get('username'),
                    task.get('completed'), task.get('title'))
            writer.writerow(data)
