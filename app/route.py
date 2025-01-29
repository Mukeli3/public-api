import pytz
from flask import jsonify, request, Blueprint
from datetime import datetime

main = Blueprint('main',  __name__)

@main.route('/api/info', methods=['GET'])
def get_info():
    email = request.args.get('email', 'your-email@example.com')
    github_url = request.args.get('github_url', 'https://github.com/yourusername/your-repo')

    response = {
            "email": email,
            #"current_datetime": datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "github_url": github_url
            }
    return jsonify(response), 200
