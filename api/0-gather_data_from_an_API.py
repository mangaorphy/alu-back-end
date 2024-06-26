#!/usr/bin/python3
import sys
import requests
if __name__ == "__main__":
    '''main section'''

    BASE_URL = "https://jsonplaceholder.typicode.com/"

    # get the users
    employees = requests.get(
        BASE_URL + f"/users/{sys.argv[1]}/").json()

    EMPLOYEE_NAME = employees.get('name')

    EMPLOY_TODO = requests.get(BASE_URL + f"/users/{sys.argv[1]}/todos").json()

    # Initialise the todos list
    TOTAL_NUMBER_OF_TASKS = {}

    # get the title and the completion status
    for todo in EMPLOY_TODO:
        TOTAL_NUMBER_OF_TASKS.update({todo.get("title"): todo.get("completed")})

    NUMBER_OF_DONE_TASKS = len([k for k, v in TOTAL_NUMBER_OF_TASKS.items() if v is True])

    print("Employee {} is done with tasks({}/{}): ".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, len(TOTAL_NUMBER_OF_TASKS)))

    for key, val in TOTAL_NUMBER_OF_TASKS.items():
        if val is True:
            print("\t {}".format(key))
