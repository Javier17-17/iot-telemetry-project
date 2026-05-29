import random
from datetime import datetime
import uuid


class Drying:
    _device_id = None
    _temperature = None
    _humidity = None
    _timestamp = None

    # CONSTRUCTOR
    def __init__(self):
        self._device_id = str(uuid.uuid4())
        self._temperature = random.randint(1, 25)
        self._humidity = random.randint(7, 40)
        self._timestamp = str(self.timestamp_random())

        print(self._device_id)
        print(self._temperature, "º")
        print(self._humidity, "%")
        print(self._timestamp)

    # GETTERS
    def get_temperature(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity

    def get_date_time_drying(self):
        return self._timestamp

    # GENERAR FECHA Y HORA ACTUAL
    def timestamp_random(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')