"""Fetches data from an api"""
#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    base_url = f"https://jsonplaceholder.typicode.com/users"
    employee_id = sys.argv[1]
    name_url = f"{base_url}/{employee_id}/"
    todo_url = f"{base_url}/{employee_id}/todos"

    name = requests.get(name_url).json()
    todo = requests.get(todo_url).json()

    len = len(todo)
    completed = 0

    for i in todo:
        if i['completed']:
            completed += 1

    print(f"Employee {name['name']} is done with tasks ({completed} / {len})")

    for i in todo:
        print(f"\t {i['title']}") if i['completed'] else None
    
    print(__doc__)
