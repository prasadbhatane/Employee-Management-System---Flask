from flask import Flask
from flask_restful import Api
from resources import Employee_Login_Resource, Register_Resource, Admin_Login_Resource, Admin_Search_Resource, Browser_Search_Resource


app = Flask(__name__)
api = Api(app)

api.add_resource(Employee_Login_Resource, '/api/employee/<string:Email>')
api.add_resource(Admin_Login_Resource, '/api/admin/<string:Email>')
api.add_resource(Admin_Search_Resource, '/api/admin/search/<string:Email>')
api.add_resource(Register_Resource, '/api/register')

api.add_resource(Browser_Search_Resource, '/api/admin/browser_search')
# http://127.0.0.1:5000/api/admin/browser_search?FirstName=a

if __name__ == '__main__':
    app.run(debug=True, port=5000)
