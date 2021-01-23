from flask import Flask, render_template, request, redirect, url_for, flash
from system import System

app = Flask(__name__)
app.secret_key = 'what is the secret key used for?'
system_instance = System()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = system_instance.client_login_details(
            Email_inp=request.form['Email'],
            Password_inp=request.form['Password']
        )
        if 'message' in user:
            flash("Invalid Credentials !")
            return render_template('login.html')
        flash('Login Successful !!')
        return render_template(
            'my_details.html',
            FirstName=user['FirstName'],
            LastName=user['LastName'],
            Email=user['Email'],
            DateOfBirth=user['DateOfBirth'],
            Mobile=user['Mobile'],
            Address=user['Address']
        )
    return render_template('login.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        employees = system_instance.client_admin_details(
            Email_inp=request.form['Email'],
            Password_inp=request.form['Password']
        )
        if 'message' in employees:
            flash("Invalid Credentials !")
            return render_template('admin.html')
        flash('Login Successful !!')
        return render_template(
            'all_details.html',
            employees=employees,
            admin_email=request.form['Email'],
            admin_password=request.form['Password']
        )
    return render_template('admin.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = system_instance.client_register(
            FirstName=request.form['FirstName'],
            LastName=request.form['LastName'],
            Email=request.form['Email'],
            DateOfBirth=request.form['DateOfBirth'],
            Mobile=request.form['Mobile'],
            Address=request.form['Address'],
            Password=request.form['Password'],
            Role_type=request.form['Role']
        )
        if 'message' in user:
            flash("Something Went Wrong !")
            return render_template('register.html')
        flash('Registered Successfully !!')
        return redirect(url_for('home'))
    return render_template('register.html')


@app.route('/my_details')
def my_details():
    return render_template('my_details.html')


@app.route('/all_details', methods=['GET', 'POST'])
def all_details():
    if request.method == 'POST':
        employees = system_instance.client_admin_search(
            Email_inp=request.form['admin_email'],
            Password_inp=request.form['admin_password'],
            FirstName=request.form['FirstName'],
            LastName=request.form['LastName'],
            Address=request.form['Address']
        )
        return render_template(
            'all_details.html',
            employees=employees,
            admin_email=request.form['admin_email'],
            admin_password=request.form['admin_password']
        )
    return render_template('all_details.html')


@app.route('/edit/<Email>/<FirstName>/<LastName>/<DateOfBirth>/<int:Mobile>/<Address>', methods=['GET', 'POST'])
def edit(Email, FirstName, LastName, DateOfBirth, Mobile, Address):
    if request.method == 'POST':
        user = system_instance.client_edit_user(
            FirstName=request.form['FirstName'],
            LastName=request.form['LastName'],
            Email=request.form['Email'],
            DateOfBirth=request.form['DateOfBirth'],
            Mobile=request.form['Mobile'],
            Address=request.form['Address'],
            Password="BY_PASSED_PASSWORD",
        )
        return render_template(
            'my_details.html',
            FirstName=user['FirstName'],
            LastName=user['LastName'],
            Email=user['Email'],
            DateOfBirth=user['DateOfBirth'],
            Mobile=user['Mobile'],
            Address=user['Address']
        )
    print(FirstName, LastName, DateOfBirth, Mobile, Address)
    return render_template(
        'edit.html',
        Email=Email,
        FirstName=FirstName,
        LastName=LastName,
        DateOfBirth=DateOfBirth,
        Mobile=Mobile,
        Address=Address
    )


@app.route('/view/<Email>/<FirstName>/<LastName>/<DateOfBirth>/<int:Mobile>/<Address>')
def view(Email, FirstName, LastName, DateOfBirth, Mobile, Address):
    return render_template(
        'my_details.html',
        FirstName=FirstName,
        LastName=LastName,
        Email=Email,
        DateOfBirth=DateOfBirth,
        Mobile=Mobile,
        Address=Address
    )


@app.route('/delete/<Email>/<admin_email>/<admin_password>', methods=['GET', 'POST'])
def delete(Email, admin_email, admin_password):
    response = system_instance.client_delete_user(
        Email_inp=Email,
        Password_inp=admin_password
    )
    employees = system_instance.client_admin_search(
        Email_inp=admin_email,
        Password_inp=admin_password,
        FirstName='',
        LastName='',
        Address=''
    )
    return render_template(
        'all_details.html',
        employees=employees,
        admin_email=admin_email,
        admin_password=admin_password
    )


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5500)
