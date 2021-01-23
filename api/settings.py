from flask_restful import fields

MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_HOST = 'localhost:3306'
MYSQL_DATABASE_NAME = 'employee_v2'

MYSQL_CONNECTION_STRING = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST,
                                                                          MYSQL_DATABASE_NAME)
DETAILS_FIELD = {
    'FirstName': fields.String,
    'LastName': fields.String,
    'DateOfBirth': fields.String,
    'Email': fields.String,
    'Mobile': fields.Integer,
    'Address': fields.String
}

ROLES_FIELD = {
    'Email': fields.String,
    'Is_Admin': fields.Boolean
}

CREDENTIALS_FIELD = {
    'Email': fields.String,
    'Password': fields.String
}