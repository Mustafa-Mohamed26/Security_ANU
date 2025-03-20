from flask import Flask, request, jsonify, abort

app = Flask(__name__)

items = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
    {'id': 3, 'name': 'Item 3'}
]

def generate_id():
    if items:
        return max(item['id'] for item in items) + 1
    return 1

# CRUD operations

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    retrieve_item = None
    for item in items:
        if item['id'] == item_id:
            retrieve_item = item
            
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    return jsonify(item)

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        abort(400)
    item = {
        'id': generate_id(),
        'name': request.json['name']
    }
    items.append(item)
    return jsonify(item), 201

# Update an existing item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    if not request.json:
        abort(400)
    item['name'] = request.json.get('name', item['name'])
    return jsonify(item)

# Delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)