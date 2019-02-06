# flask_graphene_mongo/schema.py
import graphene
import database
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Department as DepartmentModel
from models import Employee as EmployeeModel
from models import Role as RoleModel

class Department(MongoengineObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (Node,)


class Role(MongoengineObjectType):

    class Meta:
        model = RoleModel
        interfaces = (Node,)


class Employee(MongoengineObjectType):

    class Meta:
        model = EmployeeModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_employees = MongoengineConnectionField(Employee)
    all_role = MongoengineConnectionField(Role)
    role = graphene.Field(Role)

class CreateEmployee(graphene.Mutation):

    class Arguments:
        name = graphene.String()

    employee = graphene.Field(Employee)

    def mutate(self, info, name):
        employee = Employee(name=name)
        database.save_employee(name)
        return CreateEmployee(employee=employee)

class CreateAll(graphene.Mutation):

    employee = graphene.Field(Employee)
    department = graphene.Field(Department)
    role = graphene.Field(Role)

    class Arguments:
        employee_name = graphene.String()
        department_name = graphene.String()
        role_name = graphene.String()

    def mutate(self, info, **args):
        department = Department(name=args.get('department_name'))
        role = Role(name=args.get('role_name'))
        employee = Employee(
            name=args.get('employee_name'),
            department=department,
            role=role
        )

        database.save_all(employee=employee)
        return CreateAll(employee=employee)

class Mutations(graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    createAll = CreateAll.Field()

schema = graphene.Schema(query=Query, mutation=Mutations, types=[Department, Employee, Role])
