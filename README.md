# Employee Management System 🏢

A simple desktop application built with **Python** and **Tkinter** to manage employee records. The system uses a local **JSON file** database to store and retrieve data persistently.

## Features

### 1. User Authentication 🔒
* Secure login system.
* **Security Feature:** The system locks automatically after **3 failed login attempts**.

### 2. Employee Dashboard 📊
* View personal details (ID, Name, Department, Job Title, Salary).
* **Salary Operations:** Calculate Bonus (10%) and Discount (5%) with one click.
* **Attendance:** Check remaining legal holidays based on absence days.

### 3. Admin Controls 🛠️
* **Add Employee:** Register new employees with dynamic data entry.
* **Delete Employee:** Remove records from the database permanently.
* **Data Persistence:** All changes (Add/Delete) are instantly saved to `employees.json`.

---

## 📂 Project Structure

The project follows a modular architecture:

* `main.py`: The entry point to run the application.
* `gui.py`: Handles the Graphical User Interface (Windows, Buttons, Labels).
* `employee_data.py`: Manages the JSON database (Load, Save, Add, Delete).
* `operations.py`: Contains business logic (Calculations for bonus/holidays).
* `authentication.py`: Handles user validation logic.
* `employees.json`: The database file (Auto-generated if not found).

---

## 🛠️ How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ibrahemshenouda/Employee_Management_System.git
    ```

2.  **Navigate to the project folder:**
    ```bash
    cd Employee_Management_System
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

---

## 🔑 Default Credentials (For Testing)

You can use the following default accounts to test the system:

| Employee ID | Password | Role |
| :--- | :--- | :--- |
| **101** | `123` | Software Dept |
| **102** | `456` | HR Dept |

---



### 📝 Author
**Ibrahem Shenouda**
