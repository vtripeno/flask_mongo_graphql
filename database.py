# flask_graphene_mongo/database.py
from mongoengine import connect

from models import Department, Employee, Role

# You can connect to a real mongo server instance by your own.
connect('graphene-mongo-example', host='mongodb://localhost:27017', alias='default')


def init_db():
    # Create the fixtures
    print("INICIANDO DB")
    # engineering = Department(name='Engineering')
    # engineering.save()
    #
    # hr = Department(name='Human Resources')
    # hr.save()
    #
    # manager = Role(name='manager')
    # manager.save()
    #
    # engineer = Role(name='engineer')
    # engineer.save()
    #
    # peter = Employee(name='Peter', department=engineering, role=engineer)
    # peter.save()
    #
    # roy = Employee(name='Roy', department=engineering, role=engineer)
    # roy.save()
    #
    # tracy = Employee(name='Tracy', department=hr, role=manager)
    # tracy.save()

def save_employee(employee):
    print("SALVANDO EMPLOYEE")
    employee = Employee(name=employee.name, department=employee.department, role=employee.role)
    employee.save()

def save_deparment(department):
    print("SALVANDO DEPARTMENT")
    department = Department(name=department.name)
    department.save()
    return department

def save_role(role):
    print("SALVANDO ROLE")
    role = Role(name=role.name)
    role.save()
    return role


def save_all(employee):
    employee.department = save_deparment(employee.department)
    employee.role = save_role(employee.role)
    save_employee(employee)

