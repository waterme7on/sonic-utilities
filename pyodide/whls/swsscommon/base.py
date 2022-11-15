import json
from pyodide.http import pyfetch

url = "http://localhost:8080/api/send-command"


async def send_command(typ, action, key, value):
    data = {"action": action, "key": key, "value": value}
    body = {"id": "", "type": typ, "data": json.dumps(data)}
    response = await pyfetch(url=url, method="POST", body=json.dumps(body))
    response_json = await response.json()
    return response_json["status"], response_json["msg"], response_json["data"]


async def send_redis_command(*args):
    typ = "Redis"
    action = "Command"
    data = {"action": action, "args": list(args)}
    body = {"id": "", "type": typ, "data": json.dumps(data)}
    response = await pyfetch(url=url, method="POST", body=json.dumps(body))
    response_json = await response.json()
    return response_json["status"], response_json["msg"], response_json["data"]
