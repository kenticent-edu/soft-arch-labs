import json
from flask import Flask, request

app = Flask(__name__)

messages = dict()


@app.route('/log', methods=['POST', 'GET'])
def log():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(list(data.values())[0])
        messages.update(data)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return str(messages.values())


if __name__ == '__main__':
    app.run(port=8081)
