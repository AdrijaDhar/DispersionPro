from functools import wraps
from flask import request, jsonify

API_TOKEN = "YOUR_API_TOKEN"

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token != API_TOKEN:
            return jsonify({'message': 'Invalid API Token!'}), 403
        return f(*args, **kwargs)
    return decorated_function
