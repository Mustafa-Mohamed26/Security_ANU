# 💻 Flask JWT Items API

## ✨ Overview
This project is a RESTful API built using Flask and SQLAlchemy, implementing JWT-based authentication for secure access. The API allows users to perform CRUD operations on an `Items` table while ensuring only authenticated users can interact with the data.

## 🛠️ What is ORM?
**ORM (Object-Relational Mapping)** is a programming technique that allows developers to interact with a database using objects instead of raw SQL queries. It simplifies database operations by mapping database tables to programming language classes.

### 🔹 Common ORMs by Language
- **.NET Core** → Entity Framework Core
- **Python** → SQLAlchemy
- **Laravel** → Eloquent
- **Node.js** → Sequelize

### 🔹 Why Use ORM?
- Interact with databases without writing raw SQL queries
- Maps tables directly to objects
- Makes database operations structured and secure

Example in SQLAlchemy:
```python
class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
```
This maps the `Items` table directly to a Python class, making it easy to interact with.

## 🔐 What is JWT (JSON Web Token)?
JWT is a security standard used to create access tokens that authenticate users. Instead of sending passwords with each request, the API generates a **signed token** upon login. This token must be included in subsequent API requests to verify the user’s identity.

### 🔹 How JWT Works
- **Token Generation**: When a user logs in, a token is created and signed.
- **Token Storage**: The token is stored client-side (e.g., local storage, cookies).
- **Token Usage**: The token must be sent with every request for authentication.
- **Token Expiry**: Tokens expire after a set time and must be refreshed.

### 🔹 Installation
```sh
pip install pyjwt
```

Example of a JWT token:
```json
{
  "user": "mostafa",
  "exp": 1712000000
}
```

## 🚀 Features
- 🔒 Secure authentication with JWT
- 📂 CRUD operations on the `Items` table
- 🔑 Token-based access control
- 💻 SQLAlchemy as ORM
- 🐞 Error handling for token validation, data validation, and database operations
- ⏰ Configurable token expiration time
- 🏦 Secure and scalable database setup using MySQL

## 📚 Installation
### ♻️ Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/). Additionally, install MySQL.

### 📦 Install Dependencies
Run the following command to install dependencies:
```sh
pip install flask flask_sqlalchemy pymysql pyjwt
```

## 🗄 Database Setup
Update the database URI in `app.config`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Lec2_API_Course'
```
Create the database manually:
```sql
CREATE DATABASE Lec2_API_Course;
```
Then, initialize it:
```sh
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

## 🚀 Running the Application
Start the Flask application by running:
```sh
python app.py
```
The API will be available at `http://127.0.0.1:5000/`.

## 📱 API Endpoints
### 🔐 Authentication
#### 1. 👤 User Login
**Endpoint:** `/login`
**Method:** `POST`
**Payload:**
```json
{
  "username": "mostafa",
  "password": "ziad"
}
```
**Response:**
```json
{
  "token": "<jwt_token>"
}
```
The token should be included in the `Authorization` header for all subsequent requests.

### 📂 Items CRUD Operations (JWT Required)
Include the JWT token in the `Authorization` header for all requests.

#### 2. 🔎 Get All Items
**Endpoint:** `/items`
**Method:** `GET`
**Headers:**
```sh
Authorization: Bearer <jwt_token>
```
**Response:**
```json
[
  { "id": 1, "name": "Item1" },
  { "id": 2, "name": "Item2" }
]
```

#### 3. 🔍 Get Single Item by ID
**Endpoint:** `/items/<int:item_id>`
**Method:** `GET`
**Headers:**
```sh
Authorization: Bearer <jwt_token>
```
**Response:**
```json
{ "id": 1, "name": "Item1" }
```

#### 4. 📝 Create a New Item
**Endpoint:** `/items`
**Method:** `POST`
**Headers:**
```sh
Authorization: Bearer <jwt_token>
```
**Payload:**
```json
{
  "name": "NewItem"
}
```
**Response:**
```json
{ "id": 3, "name": "NewItem" }
```

#### 5. ✏️ Update an Item
**Endpoint:** `/items/<int:item_id>`
**Method:** `PUT`
**Headers:**
```sh
Authorization: Bearer <jwt_token>
```
**Payload:**
```json
{
  "name": "UpdatedItem"
}
```
**Response:**
```json
{ "id": 1, "name": "UpdatedItem" }
```

#### 6. 🗑️ Delete an Item
**Endpoint:** `/items/<int:item_id>`
**Method:** `DELETE`
**Headers:**
```sh
Authorization: Bearer <jwt_token>
```
**Response:**
```json
{ "message": "Item deleted successfully" }
```

## ⚠️ Error Handling
- **🚫 401 Unauthorized:** Missing or invalid JWT token.
- **⚠️ 400 Bad Request:** Missing required fields or incorrect data format.
- **🔍 404 Not Found:** Item does not exist.
- **🔥 500 Internal Server Error:** Database or server-related issues.
- **🚷 403 Forbidden:** Unauthorized access attempt detected.

## 🔒 Security Considerations
- Modify `SECRET_KEY` for better security.
- Use environment variables instead of hardcoding sensitive data.
- Implement HTTPS for secure API communication.
- Restrict access based on user roles if necessary.

## 💡 Future Enhancements
- Implement user registration and role-based authentication.
- Add password hashing for better security.
- Enable refresh tokens for longer authentication periods.
- Improve logging and monitoring for API requests.
- Add rate limiting to prevent abuse.

## 📖 License
This project is open-source and available under the MIT License.

