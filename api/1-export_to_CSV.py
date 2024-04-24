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

    for todo in todo_data:
        if todo.get("userId") == user_data.get("id"):
            output_format = '"{}","{}","{}","{}"'.format(
                user_data.get("id"),
                user_data.get("username"),
                todo.get("completed"),
                todo.get("title")
            )
            with open("{}.csv".format(user_data.get('id')), "a") as f:
                f.write(output_format + "\n")


if __name__ == "__main__":
    fetchTodo()
