# # from flask import Flask, render_template, request, redirect, url_for
# # import sqlite3
# # from werkzeug.security import generate_password_hash, check_password_hash

# # app = Flask(__name__)

# # # SQLite database connection function
# # def get_db_connection():
# #     conn = sqlite3.connect('users.db')-
# #     conn.row_factory = sqlite3.Row  # allows us to access columns by name
# #     return conn

# # # Create the users table if not exists
# # def create_table():
# #     conn = get_db_connection()
# #     c = conn.cursor()
# #     c.execute('''CREATE TABLE IF NOT EXISTS users (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 username TEXT NOT NULL,
# #                 password TEXT NOT NULL)''')
# #     conn.commit()
# #     conn.close()

# # # Home route (renders the login page)
# # @app.route('/')
# # def login():
# #     return render_template('login.html')

# # # Route to handle the login form submission
# # @app.route('/login', methods=['POST'])
# # def authenticate():
# #     username = request.form['username']
# #     password = request.form['password']
    
# #     # Query the database for user details
# #     conn = get_db_connection()
# #     c = conn.cursor()
# #     c.execute('SELECT * FROM users WHERE username = ?', (username,))
# #     user = c.fetchone()
# #     conn.close()

# #     if user and check_password_hash(user['password'], password):
# #         # Redirect to dashboard on successful login
# #         return redirect(url_for('dashboard'))
# #     else:
# #         # Return an error message on failed login
# #         return render_template('login.html', error="Invalid username or password")

# # # Route for the dashboard after a successful login
# # @app.route('/dashboard')
# # def dashboard():
# #     return render_template('dashboard.html')

# # # Create a new user (for testing purposes)
# # @app.route('/create_user', methods=['POST'])
# # def create_user():
# #     username = request.form['username']
# #     password = request.form['password']
# #     hashed_password = generate_password_hash(password)  # Hash the password for security
    
# #     conn = get_db_connection()
# #     c = conn.cursor()
# #     c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
# #     conn.commit()
# #     conn.close()
# #     return redirect(url_for('login'))

# # if __name__ == '_main_':
# #     create_table()  # Create the database and table if they don't exist
# #     app.run(debug=True)







# import sqlite3

# # Function to set up the database and create the table
# def setup_database():
#     conn = sqlite3.connect('user_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE NOT NULL,
#         password TEXT NOT NULL
#     )
#     ''')
#     conn.commit()
#     conn.close()

# # Function to sign up a new user
# def signup(username, password):
#     conn = sqlite3.connect('user_data.db')
#     cursor = conn.cursor()
#     try:
#         cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
#         conn.commit()
#         print('Signup successful!')
#     except sqlite3.IntegrityError:
#         print('Username already exists!')
#     finally:
#         conn.close()

# # Function to log in an existing user
# def login(username, password):
#     conn = sqlite3.connect('user_data.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#     user = cursor.fetchone()
#     if user:
#         print('Login successful!')
#     else:
#         print('Invalid username or password.')
#     conn.close()

# # Example usage
# setup_database()

# # Signup example
# signup('new_user', 'secure_password')

# # Login example
# login('new_user', 'secure_password')
# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)

# def get_db_connection():
#     conn = sqlite3.connect('user_data.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# def setup_database():
#     conn = sqlite3.connect('user_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE NOT NULL,
#         password TEXT NOT NULL
#     )
#     ''')
#     conn.commit()
#     conn.close()

# @app.route('/')
# def login():
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def authenticate():
#     username = request.form['username']
#     password = request.form['password']

#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
#     user = cursor.fetchone()
#     conn.close()

#     if user and check_password_hash(user['password'], password):
#         return redirect(url_for('dashboard'))
#     else:
#         return render_template('login.html', error="Invalid username or password")

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_password = generate_password_hash(password)

#         conn = get_db_connection()
#         cursor = conn.cursor()
#         try:
#             cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
#             conn.commit()
#         except sqlite3.IntegrityError:
#             return render_template('signup.html', error="Username already exists")
#         finally:
#             conn.close()

#         return redirect(url_for('login'))
#     return render_template('signup.html')

# if __name__ == '__main__':
#     setup_database()
#     app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySQL Database connection function
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='raza12',
            database='rajak'
        )
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            return redirect(url_for('dashboard'))
    return render_template('login.html', error="Invalid username or password")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
                conn.commit()
                cursor.close()
            except mysql.connector.IntegrityError:
                return render_template('signup.html', error="Username already exists")
            finally:
                conn.close()

        return redirect(url_for('login'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
