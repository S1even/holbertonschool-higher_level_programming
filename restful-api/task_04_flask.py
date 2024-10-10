#!/usr/bin/python3

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API"


@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():

    rq = request.get_json()

    username = rq.get("username")

    if username:
        name = rq.get("name")
        age = rq.get("age")
        city = rq.get("city")

        users[username] = {"username": username, "name": name, "age": age, "city": city}

        return jsonify({"message": "User added", "user": users[username]}), 201

    else:
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()
