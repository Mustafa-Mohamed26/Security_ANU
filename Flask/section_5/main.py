from flask import Flask, request, jsonify, abort
import mysql.connector

# Create a Flask app
app = Flask(__name__)

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="information_system_security_section_5"
)

# Login
@app.route('/login', methods=['GET','POST'])
def login():
    # If the request method is POST
    if request.method == 'POST':
        # Get the username and password from the form
        username =request.form['username']
        password = request.form['password']
        
        # Query the database
        q = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        
        cursor = db.cursor() # Create a cursor
        cursor.execute(q) # Execute the query
        user = cursor.fetchone() # Fetch the first row
        
        # Return the result
        if user:
            return user
        else:
            return {'error': 'Invalid username or password'}
        
    #     if user:
    #         return f'<h1 style="text-align: center; color: green">Welcome {username}</h1>'
    #     else:
    #         return f'<h1 style="text-align: center; color: red">Invalid username or password</h1>'
    # else:
    #     return'''
    #     <form method="POST">
    #         <label for="username">Username:</label>
    #         <input type="text" id="username" name="username" required>

    #         <label for="password">Password:</label>
    #         <input type="password" id="password" name="password" required>

    #         <button type="submit">Login</button>
    #     </form>
    #     '''
    
# Run the app
if __name__ == '__main__':
    app.run(debug=True)