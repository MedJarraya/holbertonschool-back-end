#!/usr/bin/python3
"""
Retrieves data in JSON format.
"""
import json
import requests
from sys import argv


def get_api():
    """
    Retrieves data from API.
    """
    url = 'https://jsonplaceholder.typicode.com/'
    uid = argv[1]

    usr = requests.get(url + 'users/{}'.format(uid)).json()
    todo = requests.get(url + 'todos', params={'userId': uid}).json()

    with open('{}.json'.format(uid), 'w') as file:
        obj = {uid: []}
        for employee in todo:
            tmp_obj = {
                    'task': employee.get('title'),
                    'completed': employee.get('completed'),
                    'username': usr.get('username')
                    }
            obj[uid].append(tmp_obj)
        json.dump(obj, file)


if __name__ == '__main__':
    get_api()
