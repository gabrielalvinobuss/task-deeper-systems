from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# MongoDB credentials
username = 'dev_admin'
password = 'test'
cluster = 'cluster0'
dbname = 'task'
collection_name = 'user'

# MongoDB URL
url = f"mongodb+srv://{username}:{password}@{cluster}.i8ffi.mongodb.net/{dbname}?retryWrites=true&w=majority&appName={cluster}"

# MongoDB connection
client = MongoClient(url)
db = client[dbname]
users_collection = db["users"]

# Convert ObjectId to string
def convert_object_id(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, dict):
        return {k: convert_object_id(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert_object_id(i) for i in obj]
    return obj

# List all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(users_collection.find())
    users = convert_object_id(users)
    return jsonify(users)

# Create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.json
    result = users_collection.insert_one(user_data)
    user_data['_id'] = str(result.inserted_id)
    return jsonify(user_data), 201

# Edit a user
@app.route('/api/users/<username>', methods=['PUT'])
def update_user(username):
    user_data = request.json
    result = users_collection.update_one({"username": username}, {"$set": user_data})
    
    if result.matched_count == 0:
        return jsonify({"message": "User not found"}), 404

    return jsonify({"message": "User updated successfully"})

# Delete a user
@app.route('/api/users/<username>', methods=['DELETE'])
def delete_user(username):
    users_collection.delete_one({"username": username})
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug = True)
