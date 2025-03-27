# ORM -> object relational mapper

# dotnet core => efcore
# python => sqlalchemy
# laravel => eloquent
# node js => sequelize

# database has tables and every table has items
# we need to deal with the database without using query only by code
# load the table and mapping it to an object

# ex: Items table ----- Class Items
# Item1, Item2, ... Instance form the Class Items

# no query to be used only work py programming 

# pip install flask
# pip install flask_sqlalchemy pymysql

# ----------------------------------------------------------------------

# token jwt 

# any one can access the api so i want a solution to deal with this problem
# so we need to token to make only authorized people see the data
# token -> hash code within a time frame 
# we want to secure the api

# pip install pyJWT

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import jwt, datetime

app = Flask(__name__)
# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Lec2_API_Course'

db = SQLAlchemy(app)

# Secret key for JWT authentication
SECRET_KEY = "Mohamed"

# Define Items model
class Items(db.Model):
    __tablename__ = 'Items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    # Convert object to dictionary for JSON response
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
# Route for user login and JWT generation
@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    # Simple username-password authentication
    if auth['username'] == 'mostafa' and auth['password'] == 'ziad':
        # Generate JWT token valid for 1 minute
        token = jwt.encode({
            'user': auth['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Unauthorized'}), 401
    
# Route to get all items (JWT authentication required)
@app.route('/items', methods=['GET'])
def get_items():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        items = Items.query.all()
        return jsonify([item.to_dict() for item in items])
    except:
        return jsonify({'error': 'Invalid or expired token'}), 401 

# Route to get a single item by ID (JWT authentication required)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        item = Items.query.get(item_id)
        if item is None:
            return abort(404)
        else:
            return jsonify(item.to_dict())
    except:
        return jsonify({'error': 'Invalid or expired token'}), 401 
    
# Route to create a new item (JWT authentication required)
@app.route('/items', methods=['POST'])
def create_item():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if not request.json or 'name' not in request.json:
            abort(404)
        name = request.json['name']
        new_item = Items(name=name)
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.to_dict())
    except:
        return jsonify({'error': 'Invalid or expired token'}), 401 

# Route to update an existing item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if not request.json or 'name' not in request.json:
        abort(404)
    item = Items.query.get(item_id)
    if item is None:
        abort(404)
    name = request.json['name']
    item.name = name
    db.session.commit()
    return jsonify(item.to_dict())

# Route to delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Items.query.get(item_id)
    if item is None:
        abort(404)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'result': True})

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)


    
