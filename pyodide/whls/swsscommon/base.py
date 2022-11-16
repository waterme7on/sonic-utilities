import json
from js import XMLHttpRequest, Blob

url = "http://localhost:8000/api/send-command"


def send_data(typ, data):
    if typ != "Shell2":
        data = json.dumps(data)
    body = {"id": "", "type": typ, "data": data}

    # https://stackoverflow.com/a/64789621/1087890
    req = XMLHttpRequest.new()
    req.open("POST", url, False)
    blob = Blob.new([json.dumps(body)], {type: 'application/json'})
    req.send(blob)
    response_json = json.loads(req.response)
    return response_json["status"], response_json["msg"], response_json["data"]


def send_file_command(action, key, value):
    data = {"action": action, "key": key, "value": value}
    return send_data("File", data)


def send_redis_command(*args):
    data = {"action": "Command", "args": list(args)}
    return send_data("Redis", data)


def send_shell_command(command):
    return send_data("Shell2", command)



