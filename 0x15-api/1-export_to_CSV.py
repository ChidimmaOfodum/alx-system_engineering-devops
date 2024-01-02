#!/usr/bin/python3
"""Exports data to a csv file"""
import csv
import requests
import sys

if __name__ == "__main__":
    base_url = f"https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    name_url = f"{base_url}/users/{employee_id}/"
    todo_url = f"{base_url}/user/{employee_id}/todos"

    name_lis = requests.get(name_url).json()
    todo = requests.get(todo_url).json()

    id, username = name_list['id'], name_list['username']

    with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=',')

        for i in todo:
            my_writer.writerow([id, username, i['completed'], i['title']])
