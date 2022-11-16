import json
import string
import random
from js import XMLHttpRequest, Blob

url = "http://localhost:8000/api/send-command"


def get_random_id():
    size = 12
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def send_data(cid, typ, data):
    if typ != "Shell2":
        data = json.dumps(data)
    body = {"id": cid, "type": typ, "data": data}

    # https://stackoverflow.com/a/64789621/1087890
    req = XMLHttpRequest.new()
    req.open("POST", url, False)
    blob = Blob.new([json.dumps(body)], {type: 'application/json'})
    req.send(blob)
    response_json = json.loads(req.response)
    return response_json["status"], response_json["msg"], response_json["data"]


def send_file_command(action, key, value):
    data = {"action": action, "key": key, "value": value}
    return send_data("", "File", data)


def send_redis_command(cid, *args):
    data = {"action": "Command", "args": list(args)}
    return send_data(cid, "Redis", data)


def send_shell_command(command):
    return send_data("", "Shell2", command)



