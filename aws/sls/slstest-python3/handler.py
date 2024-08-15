import requests


def hello(event, context):
    response = requests.get("https://httpbin.org/get", params={"param1": "value1"})
    return response.json()
