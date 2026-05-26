import random
from datetime import datetime, timedelta
import uuid

class Drying:
    _device_id= None
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
        print(self._humidity,"%")
        print(self._timestamp)

    # GETTERS
    def get_temperature(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity

    def get_date_time_drying(self):
        return self._timestamp

    # GENERAR FECHA Y HORA RANDOM

    def timestamp_random(self):
        initial_date = datetime(2010, 1, 1)
        end_date = datetime.now()
        delta = end_date - initial_date

        date_random = random.randint(0,delta.days)
        hour_random = random.randint(0,86400)

        final = initial_date + timedelta(days = date_random, hours = hour_random)
        return final.strftime('%Y-%m-%d %H:%M:%S')



