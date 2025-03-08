from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Default XAMPP username
app.config['MYSQL_PASSWORD'] = ''  # Keep empty if no password set in XAMPP
app.config['MYSQL_DB'] = 'taskmanager'

mysql = MySQL(app)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# User Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "User registered successfully!"})

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()

    if user:
        access_token = create_access_token(identity=username)
        return jsonify({"token": access_token})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Add a New Task
@app.route('/tasks', methods=['GET','POST'])
#@jwt_required()
def add_task():
    data = request.json
    title = data['title']
    description = data['description']
    due_date = data['due_date']
    priority = data['priority']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tasks (title, description, due_date, priority, status) VALUES (%s, %s, %s, %s, 'pending')", 
                (title, description, due_date, priority))
    mysql.connection.commit()
    cur.close()
    if request.method == 'GET':
        return jsonify({"message": "Fetching all tasks..."})  # Temporary response

    if request.method == 'POST':
        return jsonify({"message": "Task added successfully"})
    return jsonify({"message": "Task added successfully!"})
@app.route('/')

def get_tasks():
    auth_header = request.headers.get("Authorization")
    
    if not auth_header:
        return jsonify({"msg": "Missing Authorization Header"}), 401  # 401: Unauthorized

    tasks = [
        {"id": 1, "title": "Task 1", "status": "Pending"},
        {"id": 2, "title": "Task 2", "status": "Completed"}
    ]
    return jsonify(tasks), 200 
    return "Welcome to the Task Manager API!"


if __name__ == '__main__':
    app.run(debug=True)
