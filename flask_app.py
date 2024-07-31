
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, render_template
#from flask_cors import CORS
import os
import subprocess

app = Flask(__name__)
#CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send_notification', methods=['POST'])
def send_notification():
    message = request.form.get('message')
    topic = request.form.get('topic')

    if message and topic:
        # Replace the API_URL below with the actual API URL of ntfy.sh
        API_URL = "https://ntfy.sh"

        curl_command = f"curl -X POST -d \"{message}\" {API_URL}/{topic}"
        subprocess.run(curl_command, shell=True, check=True)

        return {'status': 'success', 'message': 'Notification sent successfully.'}, 200
    else:
        return {'status': 'error', 'message': 'Message and topic are required.'}, 400

if __name__ == '__main__':
    app.run()

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')
