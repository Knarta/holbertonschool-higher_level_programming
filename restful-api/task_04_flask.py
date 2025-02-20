#!/usr/bin/python3

"""Task 4: Create a RESTful API with Flask"""

from flask import Flask, jsonify, request


app = Flask(__name__)*
users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def list_users():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Username is required"}), 400
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    users[data['username']] = data
    return jsonify(data), 201


if __name__ == "__main__":
    app.run()
