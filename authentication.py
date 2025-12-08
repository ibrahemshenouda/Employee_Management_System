import employee_data


def authenticate_user(emp_id, password):
    user = employee_data.get_employee_by_id(emp_id)

    if user and user["password"] == password:
        return user
    return None
