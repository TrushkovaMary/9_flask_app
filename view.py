from flask import render_template, jsonify, abort, request
import datetime
import json
from app import app, to_hash

try:
    with open('users.json', 'r') as f:
        users = json.load(f)
except FileNotFoundError:
    users = []
    with open('users.json', 'w') as f:
        json.dump(users, f)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user by id
    :param user_id: user id
    :return: json
    """
    user = list(filter(lambda x: x['id'] == user_id, users))
    if len(user) == 0:
        abort(404)
    return jsonify({'users': user[0]})


@app.route('/users/<string:user_login>', methods=['GET'])
def get_user_by_login(user_login):
    """
    Get usr by login
    :param user_login:
    :return: json
    """
    user = list(filter(lambda x: x['login'] == user_login, users))
    if len(user) == 0:
        abort(404)
    return jsonify({'users': user[0]})


@app.route('/user', methods=['POST'])
def reg_user():
    """
    User registration
    :return: json
    """
    try:
        user_new = {
            'id': users[-1]['id'] + 1,
            'login': request.json['login'],
            'password': to_hash(str(request.json['password'])),
            'regDate': datetime.datetime.now().isoformat()
        }
        users.append(user_new)
        with open('users.json', 'w') as file:
            json.dump(users, file)
        return jsonify({'user': user_new}), 201
    except IndexError:
        user_new = {
            'id': 1,
            'login': request.json['login'],
            'password': to_hash(request.json['password']),
            'regDate': datetime.datetime.now().isoformat()

        }
        users.append(user_new)
        with open('users.json', 'w') as file:
            json.dump(users, file)
        return jsonify({'user': user_new}), 201
    except:
        abort(400)


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})


