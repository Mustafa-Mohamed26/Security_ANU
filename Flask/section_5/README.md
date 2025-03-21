# 🔐 Flask MySQL Login System

## 📌 Overview
This project is a simple Flask-based login system that connects to a MySQL database. It allows users to log in by providing their username and password.

## 📋 Requirements
To run this project, ensure you have the following installed:
- 🐍 Python 3
- 🔥 Flask
- 🗄️ MySQL database
- 🔗 MySQL Connector for Python

### 📦 Install Dependencies
Use the following command to install required dependencies:
```sh
pip install flask mysql-connector-python
```

## 🏛 Database Setup
Ensure you have a MySQL database named `information_system_security_section_5` and a table named `users` with at least the following structure:
```sql
-- 🛠️ Create the users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

-- 📥 Insert data into the users table
INSERT INTO users (username, password) VALUES
    ('admin', 'password'),
    ('user1', 'password1'),
    ('user2', 'password2'),
    ('user3', 'password3');

-- 🔍 Select all data from the users table
SELECT * FROM users;

-- 🔎 Select specific data from the users table
SELECT * FROM users WHERE username = 'admin' AND password = 'password';
```

## ⚠️ SQL Injection Discussion
### ❌ Security Issues
The current implementation of the login system is vulnerable to SQL injection due to the direct concatenation of user inputs into SQL queries. For example:
```sql
SELECT * FROM users WHERE username = 'admin'-- ' AND password = 'password';
SELECT * FROM users WHERE username = 'admin' OR 1=1-- ' AND password = 'password';
SELECT * FROM users WHERE username = '' OR 1=2-- ' AND password = 'password';
SELECT * FROM users WHERE username = '';
```
These queries demonstrate common SQL injection techniques:
1. **📝 Comment Injection (`--`)**: The attacker can bypass the password check by commenting out the rest of the SQL query.
2. **🔓 Always True Condition (`OR 1=1`)**: This allows unauthorized access by making the `WHERE` clause always true.
3. **📊 Boolean-Based Injection (`OR 1=2`)**: Attackers can manipulate conditions to extract data.

### ✅ How to Prevent SQL Injection
1. **🔄 Use Prepared Statements**: Instead of directly inserting user inputs into SQL queries, use parameterized queries.
2. **🔑 Hash Passwords**: Instead of storing plaintext passwords, use a hashing algorithm like bcrypt.
3. **🚨 Implement Proper Error Handling**: Avoid exposing database error messages to users.

### 🛡️ Example of a Secure Query
Instead of:
```python
q = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```
Use:
```python
cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
```

## ▶️ Running the Application
To start the Flask application, run:
```sh
python app.py
```
By default, the application runs on `http://127.0.0.1:5000/`.

## 🌐 API Endpoint

### 🔑 Login
**📍 Endpoint:** `POST /login`

**📤 Request Parameters (Form Data):**
```json
{
    "username": "user123",
    "password": "securepassword"
}
```

**✅ Response (Success - 200 OK):**
```json
{
    "id": 1,
    "username": "user123",
    "password": "securepassword"
}
```

**❌ Response (Invalid Credentials - 401 Unauthorized):**
```json
{
    "error": "Invalid username or password"
}
```

## 📜 License
This project is open-source and available for modification and improvement.

