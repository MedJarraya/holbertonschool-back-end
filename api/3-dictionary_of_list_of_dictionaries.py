#!/usr/bin/python3
"""
retrieve data in JSON format.
"""
import json
import requests as r


def get_api():
    """
    retrieve data from API
    """
    url = "https://jsonplaceholder.typicode.com/"
    user = r.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({usr.get("id"): [{
            "username": usr.get("username"),
            "task": e.get("title"),
            "completed": e.get("completed")
        } for e in r.get(url + "todos",
                         params={"userId": usr.get("id")}).json()]
            for usr in user}, jsonfile)


if __name__ == '__main__':
    get_api()
