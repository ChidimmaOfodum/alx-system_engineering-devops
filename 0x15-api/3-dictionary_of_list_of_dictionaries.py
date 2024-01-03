#!/usr/bin/python3
"""Exports data to a json file"""
import json
import requests

if __name__ == "__main__":
    base_url = f"https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos"

    todo = requests.get(todo_url).json()
    print(len(todo))
    user_dict = {}

    for i in todo:
        user_id = i['userId']
        if not user_dict.get(user_id, None):
            user_dict[user_id] = []
            name = requests.get(f"{base_url}/users/{user_id}").json()['username']
            print(name)
        else:
            name = user_dict[user_id][0]['username']
        
        task = {"username": name,
                "task": i['title'], "completed": i['completed']}
        user_dict[user_id].append(task)

    with (open("todo_all_employees.json", 'w')) as f:
        json_object = json.dumps(user_dict)
        f.write(json_object)
