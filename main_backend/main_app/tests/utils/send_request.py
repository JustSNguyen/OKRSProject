import json
import requests


class RequestInfo:
    def __init__(self, url, method="GET", data={}, headers={}):
        self.url = url
        self.method = method
        self.data = data
        self.headers = headers


def send_json_request(client, request_info):
    json_data = {}
    if request_info.data:
        json_data = json.dumps(request_info.data)

    headers = {
        "Content-Type": "application/json"
    }

    for key in request_info.headers:
        headers[key] = request_info.headers[key]

    response = client.generic(
        request_info.method, request_info.url, data=json_data, headers=headers, follow=False)

    return response
