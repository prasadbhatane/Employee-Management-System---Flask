from requests import put, get, post, delete


class System:
    def client_register(self, FirstName, LastName, Email, DateOfBirth, Mobile, Address, Password, Role_type):
        Is_Admin = 0
        if Role_type == 'Admin':
            Is_Admin = 1
        new_user = post('http://127.0.0.1:5000/api/register', data={
            'FirstName': FirstName,
            'LastName': LastName,
            'Email': Email,
            'DateOfBirth': DateOfBirth,
            'Mobile': Mobile,
            'Address': Address,
            'Password': Password,
            'Is_Admin': Is_Admin
        }).json()
        print(new_user)
        return new_user

    def client_login_details(self, Email_inp, Password_inp):
        user = get('http://127.0.0.1:5000/api/employee/{}'.format(Email_inp), data={
            'Password': Password_inp,
            'Is_Admin': 0
        }).json()
        return user

    def client_admin_details(self, Email_inp, Password_inp):
        all_users = get('http://127.0.0.1:5000/api/admin/{}'.format(Email_inp), data={
            'Password': Password_inp,
            'Is_Admin': 1
        }).json()
        return all_users

    def client_admin_search(self, Email_inp, Password_inp, FirstName, LastName, Address):
        all_users = get('http://127.0.0.1:5000/api/admin/search/{}'.format(Email_inp), data={
            'FirstName': FirstName,
            'LastName': LastName,
            'Address': Address,
            'Password': Password_inp,
            'Is_Admin': 1
        }).json()
        return all_users

    def client_delete_user(self, Email_inp, Password_inp):
        user = delete('http://127.0.0.1:5000/api/employee/{}'.format(Email_inp), data={
            'Password': Password_inp,
            'Is_Admin': 0
        })
        return user

    def client_edit_user(self, FirstName, LastName, Email, DateOfBirth, Mobile, Address, Password):
        user = put('http://127.0.0.1:5000/api/employee/{}'.format(Email), data={
            'FirstName': FirstName,
            'LastName': LastName,
            'Email': Email,
            'DateOfBirth': DateOfBirth,
            'Mobile': Mobile,
            'Address': Address,
            'Password': Password
        }).json()
        return user
