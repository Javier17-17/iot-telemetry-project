import json

class JsonConverter:

    @staticmethod
    def json(data):
        #return json.dump()
        print(json.dumps(data, indent=4))


