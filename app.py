from config import Configuration
import binascii
import hashlib
import json
import os

from flask import Flask
import binascii
import datetime
import hashlib
import json
import os
from config import Configuration
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
app.config.from_object(Configuration)

def to_hash(password):
    """
    Password hash
    :param password: password
    :return: hex-password
    """
    salt = hashlib.sha256(os.urandom(70)).hexdigest().encode('ascii')
    my_hash = binascii.hexlify(hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 80000))
    return (salt + my_hash).decode('ascii')






