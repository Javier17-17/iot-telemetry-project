class JsonConverter:

    @staticmethod
    def drying_to_telemetry(drying):
        return {
            "device_id": 1,
            "temperature": drying._temperature,
            "humidity": drying._humidity,
            "timestamp": drying._timestamp.replace(" ", "T")
        }

    @staticmethod
    def scale_to_event(scale):
        return {
            "weight": scale._net_weight,
            "truck_plate": "1234ABC",
            "timestamp": scale._timestamp.replace(" ", "T")
        }