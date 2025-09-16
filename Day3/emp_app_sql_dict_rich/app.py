"""Employee Management Console Application using SQL Dict Repo"""

from db import repo_sql_dict as repo

def create_view():
    emp_id = int(input('ID: '))
    name = input('Name: ')
    age = int(input('Age: '))
    salary = float(input('Salary: '))
    is_active = input('Active(y/n): ').upper() == 'Y'
    employee = {
        'id': emp_id,
        'name': name,
        'age': age,
        'salary': salary,
        'is_active': is_active
        }
    try:
        repo.create_employee(employee)
        print('Employee Created Successfully.')
    except repo.EmployeeAlreadyExistError as ex:
        print(f"{ex}")
    except repo.DatabaseError as ex:
        print(f"{ex}")

def read_all_view():
    print('List of Employees:')
    for employee in repo.read_all_employee():
        print(employee)

def read_by_id_view():
    emp_id = int(input('ID: '))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print('Employee not found.')
    else:
        print(employee)

def update_view():
    emp_id = int(input('ID: '))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print('Employee Not Found')
    else:
        print(employee)
        salary = float(input('New Salary: '))
        new_employee = {
            'id': employee['id'],
            'name': employee['name'],
            'age': employee['age'],
            'salary': salary,
            'is_active': employee['is_active']
        }
        repo.update(emp_id, new_employee)
        print('Employee updated successfully.')

def delete_view():
    emp_id = int(input('ID: '))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print('Employee Not Found')
    else:
        repo.delete_employee(emp_id)
        print('Employee Deleted Successfully.')

def menu():
    """Displays the main menu and handles user choices."""
    message = '''
    Options are:
    1 - Create Employee
    2 - List All Employees
    3 - Read Employee By Id
    4 - Update Employee
    5 - Delete Employee
    6 - Exit 
    Your Option:'''    
    choice = int(input(message))
    if choice == 1:
        create_view()
    elif choice == 2:
        read_all_view()
    elif choice == 3:
        read_by_id_view()
    elif choice == 4:
        update_view()
    elif choice == 5:
        delete_view()
    elif choice == 6:
        print('Thank you for using the application.')
    return choice


def menus():
    """Runs the menu loop until user exits."""
    choice = menu()
    while choice != 6:
        choice = menu()


if __name__ == "__main__":
    menus()
