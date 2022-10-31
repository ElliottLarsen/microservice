from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Please enter prefix, project and ticket as query parameters to http://127.0.0.1:5000/data"

@app.route('/data')
def get_url():
    prefix = request.args.get('prefix')
    project = request.args.get('project')
    ticket = request.args.get('ticket')
    data_received = {'prefix': prefix, 'project': project, 'ticket': ticket}
    if None in [i for i in data_received.values()]:
        return "Invalid input", 400

    complete_url = f"https://{prefix}.atlassian.net/browse/{project}-{ticket}"
    return jsonify(data_received = data_received, complete_url = complete_url)