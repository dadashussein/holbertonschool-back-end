#!/usr/bin/python3
"""Documendation for module"""

import json
import requests


def fetchData():
    """Document for todo"""
    url = "https://jsonplaceholder.typicode.com/users/"
    user_res = requests.get(url)
    todo_res = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_data = user_res.json()
    todo_data = todo_res.json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            user.get("id"): [{
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }for todo in todo_data if todo.get("userId") == user.get("id")
            ]for user in user_data
        }, f)


if __name__ == ("__main__"):
    fetchData()
