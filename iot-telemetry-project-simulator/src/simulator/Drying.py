import random
from datetime import datetime


class Drying:
    _temperature = None
    _humidity = None
    _date_time_drying = None


    # CONSTRUCTOR

    def __init__(self):

        self._temperature = random.randint(1, 25)
        self.humidity = random.randint(7, 40)
        self._date_time_drying = datetime.now()

        print(self._temperature, "º")
        print(self._humidity,"%")
        print(self._date_time_drying)

    # GETTERS
    def get_temperature(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity

    def get_date_time_drying(self):
        return self._date_time_drying



