#!/usr/bin/python3
"""Documendation for module"""


import requests
import sys


def fetchTodo():
    """Document for todo"""
    url = "https://jsonplaceholder.typicode.com/users/{}/".format(sys.argv[1])
    req_user = requests.get(url)
    req_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_data = req_user.json()
    todo_data = req_todo.json()
    done_tasks = []
    total_tasks = 0
    for todo in todo_data:
        if todo.get("userId") == user_data.get("id"):
            total_tasks += 1
            if todo.get("completed") is True:
                done_tasks.append(todo)
    print("Employee {} is done with tasks({}/{}):"
          .format(user_data.get("name"), len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    fetchTodo()
