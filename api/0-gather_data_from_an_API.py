#!/usr/bin/python3
import requests
import sys

employee_id = sys.argv[1]
base_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

response = requests.get(base_url)

if response.status_code == 404:
    print("Invalid Employee ID!")
    sys.exit(1)

tasks = response.json()
total_tasks = len(tasks)
completed_tasks = [task for task in tasks if task["completed"]]
num_completed_tasks = len(completed_tasks)
employee_name = tasks[0]["userId"]
employee_info_url = f"https://jsonplaceholder.typicode.com/users/{employee_name}"
employee_response = requests.get(employee_info_url)
employee_info = employee_response.json()
employee_name = employee_info["name"]

print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

for task in completed_tasks:
    print(f"\t- {task['title']}")
