from db import my_session
from models import Details, Credentials, Role

from flask_restful import Resource, marshal_with, reqparse, abort
from settings import DETAILS_FIELD

parser = reqparse.RequestParser()
parser.add_argument('FirstName', type=str)
parser.add_argument('LastName', type=str)
parser.add_argument('Email', type=str)
parser.add_argument('Mobile', type=int)
parser.add_argument('DateOfBirth', type=str)
parser.add_argument('Address', type=str)
parser.add_argument('Password', type=str)
parser.add_argument('Is_Admin', type=int)


def is_valid(Email_inp, Password_inp, Is_Admin_inp, by_pass=False):
    if Is_Admin_inp == 1:
        auth_result = my_session.query(Role).filter(Role.Email == Email_inp,
                                                    Role.Is_Admin == 1).all()
    else:
        auth_result = my_session.query(Role).filter(Role.Email == Email_inp).all()

    if auth_result:
        if by_pass:
            return True
        cred_result = my_session.query(Credentials).filter(Credentials.Email == Email_inp,
                                                           Credentials.Password == Password_inp).all()
        if cred_result:
            return True
        else:
            return False
    else:
        return False


class Employee_Login_Resource(Resource):
    @marshal_with(DETAILS_FIELD)
    def get(self, Email):

        # parsing arguments
        args = parser.parse_args()
        Password = args['Password']
        Is_Admin = args['Is_Admin']

        # checking validity
        if not is_valid(Email, Password, Is_Admin):
            abort(404, message='Invalid Credentials or Role')

        employee = my_session.query(Details).filter(Details.Email == Email).first()
        return employee

    @marshal_with(DETAILS_FIELD)
    def put(self, Email):

        # parsing arguments
        args = parser.parse_args()
        Password = args['Password']
        Is_Admin = 0

        # checking validity
        if not is_valid(Email, Password, Is_Admin, by_pass=True):
            abort(404, message='Invalid Credentials or Role')

        employee = my_session.query(Details).filter(Details.Email == Email).first()

        if args['FirstName']:
            employee.FirstName = args['FirstName']

        if args['LastName']:
            employee.LastName = args['LastName']

        if args['Mobile']:
            employee.Mobile = args['Mobile']

        if args['Address']:
            employee.Address = args['Address']

        if args['DateOfBirth']:
            employee.DateOfBirth = args['DateOfBirth']

        my_session.commit()
        return employee, 201

    def delete(self, Email):

        # parsing arguments
        args = parser.parse_args()
        Password = args['Password']
        Is_Admin = args['Is_Admin']

        # checking validity
        if not is_valid(Email, Password, Is_Admin, by_pass=True):
            abort(404, message='Invalid Credentials or Role')

        employee_details = my_session.query(Details).filter(Details.Email == Email).first()
        employee_role = my_session.query(Role).filter(Role.Email == Email).first()
        employee_credentials = my_session.query(Credentials).filter(Credentials.Email == Email).first()
        my_session.delete(employee_role)
        my_session.commit()
        my_session.delete(employee_credentials)
        my_session.commit()
        my_session.delete(employee_details)
        my_session.commit()
        return '', 204


class Register_Resource(Resource):
    @marshal_with(DETAILS_FIELD)
    def post(self):
        # parsing arguments
        args = parser.parse_args()
        FirstName = args['FirstName']
        LastName = args['LastName']
        Email = args['Email']
        Password = args['Password']
        Mobile = args['Mobile']
        DateOfBirth = args['DateOfBirth']
        Address = args['Address']
        Is_Admin = args['Is_Admin']

        user_details = Details(
            FirstName=FirstName,
            LastName=LastName,
            Email=Email,
            DateOfBirth=DateOfBirth,
            Mobile=Mobile,
            Address=Address
        )

        user_credentials = Credentials(
            Email=Email,
            Password=Password
        )

        user_Role = Role(
            Email=Email,
            Is_Admin=Is_Admin
        )

        my_session.add(user_details)
        my_session.commit()
        my_session.add(user_credentials)
        my_session.commit()
        my_session.add(user_Role)
        my_session.commit()
        employee = my_session.query(Details).filter(Details.Email == Email).first()
        return employee, 201


class Admin_Login_Resource(Resource):
    @marshal_with(DETAILS_FIELD)
    def get(self, Email):
        # parsing arguments
        args = parser.parse_args()
        Password = args['Password']
        Is_Admin = args['Is_Admin']

        # checking validity
        if not is_valid(Email, Password, Is_Admin):
            abort(404, message='Invalid Credentials or Role')

        employees = my_session.query(Details).all()
        return employees


class Admin_Search_Resource(Resource):
    @marshal_with(DETAILS_FIELD)
    def get(self, Email):

        # parsing arguments
        args = parser.parse_args()
        Password = args['Password']
        Is_Admin = args['Is_Admin']
        FirstName = args['FirstName']
        LastName = args['LastName']
        Address = args['Address']

        # checking validity
        if not is_valid(Email, Password, Is_Admin):
            abort(404, message='Invalid Credentials or Role')

        if not args['FirstName']:
            FirstName = ''
        if not args['LastName']:
            LastName = ''
        if not args['Address']:
            Address = ''

        employees = my_session.query(Details).filter(
            Details.FirstName.like('%{}%'.format(FirstName)),
            Details.LastName.like('%{}%'.format(LastName)),
            Details.Address.like('%{}%'.format(Address))
        ).all()
        return employees


class Browser_Search_Resource(Resource):
    @marshal_with(DETAILS_FIELD)
    def get(self):
        args = parser.parse_args()
        FirstName = args['FirstName']
        LastName = args['LastName']
        Address = args['Address']

        if not FirstName:
            FirstName = ''
        if not LastName:
            LastName = ''
        if not Address:
            Address = ''

        employees = my_session.query(Details).filter(
            Details.FirstName.like('%{}%'.format(FirstName)),
            Details.LastName.like('%{}%'.format(LastName)),
            Details.Address.like('%{}%'.format(Address))
        ).all()
        return employees
