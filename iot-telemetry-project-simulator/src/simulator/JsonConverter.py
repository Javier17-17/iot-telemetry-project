import json

class JsonConverter:

    @staticmethod
    def json(data):
        print(json.dumps(data, indent=4))


