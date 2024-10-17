import json


class Response:
    def __init__(self, response: dict):
        self.response = response

    def to_json(self):
        return json.dumps(self.response)

    def __str__(self):
        return self.to_json()
    