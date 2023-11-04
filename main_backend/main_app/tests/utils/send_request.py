import json
import requests


class RequestInfo:
    def __init__(self, url, method="GET", data={}):
        self.url = url
        self.method = method
        self.data = data


def send_json_request(client, request_info):
    json_data = {}
    if request_info.data:
        json_data = json.dumps(request_info.data)

    headers = {
        "Content-Type": "application/json"
    }

    response = client.generic(
        request_info.method, request_info.url, data=json_data, headers=headers)

    return response
