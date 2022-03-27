import requests
import uuid
from flask import Flask, request


LOGGING_SERVICE_URL = "http://127.0.0.1:8081/log"
MESSAGES_SERVICE_URL = "http://127.0.0.1:8082/message"

app = Flask(__name__)


@app.route('/facade_service', methods=['POST', 'GET'])
def facade_service():
    if request.method == 'POST':
        rand_uuid = uuid.uuid4()
        msg = request.get_data()
        res = requests.post(LOGGING_SERVICE_URL, {rand_uuid: msg})
        return res.text, res.status_code, res.headers.items()
    else:
        log_service_res = requests.get(LOGGING_SERVICE_URL)
        msg_service_res = requests.get(MESSAGES_SERVICE_URL)
        return log_service_res.text + msg_service_res.text


if __name__ == '__main__':
    app.run(port=8080)
