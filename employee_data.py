#!/usr/bin/python3
import json
import os

FILE_NAME = "employees.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        default_account = [{"id": "101", "name": "Ahmed Ali", "dept": "Software", "salary": 15000, "password": "123", "absence": 2},
                           {"id": "102", "name": "Sarah Ezzat", "dept": "HR",
                               "salary": 12000, "password": "456", "absence": 5}
                           ]
        save_data(default_account)
        return default_account
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


employee_db = load_data()


def get_employee_by_id(emp_id):
    global employee_db
    employee_db = load_data()

    for emp in employee_db:
        if emp["id"] == emp_id:
            return emp
    else:
        return None


def add_employee(new_emp):
    if get_employee_by_id(new_emp["id"]):
        return False

    employee_db.append(new_emp)
    save_data(employee_db)
    return True


def delete_employee(emp_id):
    for index, emp in enumerate(employee_db):
        if emp["id"] == emp_id:
            del employee_db[index]
            save_data(employee_db)
            return True
    return False
