#!/usr/bin/python3
"""Exports data to a csv file"""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = f"https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    name_url = f"{base_url}/users/{employee_id}/"
    todo_url = f"{base_url}/user/{employee_id}/todos"

    name_list = requests.get(name_url).json()
    todo = requests.get(todo_url).json()

    id, username = name_list['id'], name_list['username']
    user_dict = {id: []}

    for i in todo:
        task = {"task": i['title'],
                "completed": i['completed'], "username": username}
        user_dict[id].append(task)

    with (open(f"{id}.json", 'w')) as f:
        json_object = json.dumps(user_dict)
        f.write(json_object)
