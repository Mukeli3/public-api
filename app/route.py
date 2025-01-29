#!/usr/bin/python3
import pytz
from flask import request, Blueprint, Response
from datetime import datetime
import json
from dotenv import load_dotenv
import os


load_dotenv()

main = Blueprint('main',  __name__)

@main.route('/api/info', methods=['GET'])
def get_info():
    data = {
            "email": os.getenv('EMAIL', 'your-email@example.com'),
            "current_datetime": datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "github_url": os.getenv('GITHUB_URL', 'https://github.com/yourusername/your-repo')
            }
    response = Response(
        json.dumps(data, sort_keys=False),
        mimetype='application/json'
    )
    return response
