Task Manager is a web application that helps users efficiently manage their tasks. The application allows users to sign up, log in, and perform various task-related actions, such as adding, updating, deleting, and setting priorities. Users can also track the progress of their tasks by marking them as pending, in progress, or completed. The backend is developed using Flask, while MySQL is used for storing data. The frontend is built with HTML, CSS, and JavaScript.

To set up the project, ensure you have Python 3.x and XAMPP installed. First, clone the repository using git clone https://github.com/your-username/task-manager.git and navigate to the project folder. It is recommended to set up a virtual environment using python -m venv venv and activate it. Next, install the required dependencies by running pip install -r requirements.txt.

Before running the backend, set up the MySQL database. Open XAMPP and start the MySQL service. Then, go to phpMyAdmin (http://localhost/phpmyadmin), create a database named task_manager, and set up the necessary tables. The database credentials should be configured in a .env file, where you define the host, user, password, and database name. Once the database is ready, start the Flask server by running python app.py, and the API will be accessible at http://127.0.0.1:5000/.

The API includes authentication endpoints such as /signup for user registration and /login for authentication, which returns a JWT token. All task-related operations, including fetching tasks (GET /tasks), creating new tasks (POST /tasks), updating (PUT /tasks/<task_id>), and deleting (DELETE /tasks/<task_id>), require authentication via the JWT token. If you encounter a "Missing Authorization Header" error, ensure you include the token in the request headers.

For the frontend, open the index.html file in a browser. Before making API requests, confirm that the backend is running correctly. JavaScript files inside static/js/ handle API calls, and you can modify them as needed. If MySQL connection issues arise, verify that XAMPP is running and the database credentials are correct. Any "404 Not Found" errors may indicate incorrect API routes in JavaScript files.

Future improvements to the Task Manager include real-time updates using WebSockets, mobile app integration with React Native, and push notifications for task reminders.

This project was developed by Harshini, a full-stack developer. If you need assistance or have suggestions for improvements, feel free to contribute or reach out.







