#!/usr/bin/python3
"""Documendation for module"""

import json
import requests
import sys


def fetchData():
    """Document for todo"""
    url = "https://jsonplaceholder.typicode.com/users/{}/".format(sys.argv[1])
    user_res = requests.get(url)
    todo_res = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_data = user_res.json()
    todo_data = todo_res.json()

    with open("{}.json".format(user_data.get("id")), "w") as f:
        json.dump({
            user_data.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user_data.get("username")
            }for todo in todo_data if todo.get("userId") == user_data.get("id")
            ]
        }, f)


if __name__ == ("__main__"):
    fetchData()
