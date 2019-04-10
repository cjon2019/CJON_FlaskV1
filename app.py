from flask import Flask, request, render_template
import pyodbc

app = Flask(__name__)
@app.route("/", methods =['GET', 'POST'])
def httpMethods():
    if request.method == 'POST':
        return 'You are using a POST request'
    elif request.method == 'GET':
        return 'You are using a GET request'

# Connect to MSSQL and print all users from database
@app.route("/users")
def users():
    conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=RION;'
    'Database=TestDatabase;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM [TestDatabase].[dbo].[Users]')
    data = cursor.fetchall()

    return render_template('users_template.html', data = data)

# Database Get by Id
@app.route("/users/<int:id>")
def user_by_Id(id):
    conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=RION;'
    'Database=TestDatabase;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT * FROM [TestDatabase].[dbo].[Users]
        WHERE Id = {id}""")
    data = cursor.fetchall()

    return render_template('users_template.html', data = data)

# Database Create Route
@app.route("/users/create", methods =['POST'])
def user_create():
    conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=RION;'
    'Database=TestDatabase;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    # Get data from POST request
    req_data = request.get_json()
    new_username = req_data.get('username')
    cursor.execute(f'''
    INSERT INTO Users (Username)
    VALUES ('{new_username}')
    ''')
    cursor.commit()
    return f'Successful added {new_username}'

# Database Update Route
@app.route("/users/update/<int:id>", methods = ['PUT'])
def user_update(id):
    conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=RION;'
    'Database=TestDatabase;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    # Get data from PUT request
    req_data = request.get_json()
    new_username = req_data.get('username')
    cursor.execute(f'''
    UPDATE [Users]
    SET Username = '{new_username}'
    WHERE Id = {id}
    ''')
    cursor.commit()
    return f'Updated User Id:{id} \nNew Username: {new_username}'

# Database Delete Route
@app.route("/users/delete/<int:id>", methods = ['DELETE'])
def user_delete(id):
    conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=RION;'
    'Database=TestDatabase;'
    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    # Delete User by Id
    cursor.execute(f'''
    DELETE FROM Users
    WHERE Id = {id}
    ''')
    cursor.commit()
    return f'Deleted User Id:{id}'

if __name__ == "__main__":
    app.run()
