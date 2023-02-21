#!/usr/bin/python3
"""
Retrieves data in CSV format.
"""
import csv
import requests
from sys import argv


def get_api():
    """
    Retrieves data from API.
    """
    url = 'https://jsonplaceholder.typicode.com/'
    uid = argv[1]

    # get a specific user from users in jsonplaceholder
    usr = requests.get(url + 'users/{}'.format(uid)).json()
    # makes a query string to get tasks based on user id
    todo = requests.get(url + 'todos', params={'userId': uid}).json()

    with open('{}.csv'.format(uid), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for employee in todo:
            user_id = uid
            username = usr.get('username')
            task_comp = employee.get('completed')
            task_title = employee.get('title')

            emp_record = [user_id, username, task_comp, task_title]
            writer.writerow(emp_record)


if __name__ == '__main__':
    get_api()
