# 🚀 Flask CRUD API

## 📌 Overview
This project is a simple RESTful API built with Flask that provides CRUD (Create, Read, Update, Delete) operations on a list of items. The API allows users to retrieve, add, update, and delete items.

## 🛠 Requirements
To run this project, you need to have Python installed. You also need to install Flask, which can be done using:

```sh
pip install flask
```

## ▶ Running the Application
To start the Flask application, run:

```sh
python app.py
```

By default, the application runs on `http://127.0.0.1:5000/`.

## 🌐 API Endpoints

### 1️⃣ Get all items
**Endpoint:** `GET /items`

**Response:**
```json
[
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]
```

### 2️⃣ Get an item by ID
**Endpoint:** `GET /items/<item_id>`

**Response (Success - ✅ 200 OK):**
```json
{"id": 1, "name": "Item 1"}
```

**Response (Not Found - ❌ 404):**
```json
{"error": "Not Found"}
```

### 3️⃣ Create a new item
**Endpoint:** `POST /items`

**Request Body:**
```json
{"name": "New Item"}
```

**Response (Success - ✅ 200 OK):**
```json
{"id": 4, "name": "New Item"}
```

### 4️⃣ Update an item by ID
**Endpoint:** `PUT /items/<item_id>`

**Request Body:**
```json
{"name": "Updated Item"}
```

**Response (Success - ✅ 200 OK):**
```json
{"id": 1, "name": "Updated Item"}
```

**Response (Not Found - ❌ 404):**
```json
{"error": "Not Found"}
```

### 5️⃣ Delete an item by ID
**Endpoint:** `DELETE /items/<item_id>`

**Response (Success - ✅ 200 OK):**
```json
{"result": true}
```

## 📝 Code Explanation

1. **⚙ Flask Initialization**: The `Flask` instance is created with `app = Flask(__name__)`.
2. **📂 Data Storage**: Items are stored in a list named `items`.
3. **🆔 ID Generation**: The `generate_id()` function generates unique IDs for new items.
4. **🔄 CRUD Operations**:
   - `GET /items`: Returns all items.
   - `GET /items/<item_id>`: Retrieves a specific item by ID.
   - `POST /items`: Creates a new item if `name` is provided.
   - `PUT /items/<item_id>`: Updates an existing item's name.
   - `DELETE /items/<item_id>`: Removes an item by ID.
5. **🚨 Error Handling**: Uses `abort(400)` for bad requests and `abort(404)` for missing items.

## 📌 Notes
- The application runs in debug mode (`debug=True`) for easier development.
- The code includes an unused variable `retrieve_item` in `get_item()`, which should be removed.

## 🚀 Future Improvements
- Store data in a database instead of a list.
- Implement user authentication.
- Improve error messages.

## 📜 License
This project is open-source and available for use and modification.

