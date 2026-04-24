import random
from datetime import datetime, timedelta
import uuid



class Scale:
    _device_id = None
    _gross_weight = None
    _net_weight = None
    _timestamp = None


# CONSTRUCTOR

    def __init__(self):

        self._device_id = str(uuid.uuid4())
        #self._gross_weight = random.uniform(1.50, 10.50)
        #self._net_weight = random.uniform(1.50, self._gross_weight)
        #self._timestamp = str(self.timestamp_random())
        self.weigh_again(self)


# GETTERS
    def get_gross_weight(self):
        return self._gross_weight

    def get_net_weight(self):
        return self._net_weight

    #def get_ticket(self):
        #return self._ticket

# PULSAR BOTÓN DE TARA

    def press_tare(self):
        self._gross_weight = 0
        self._net_weight = 0

        print("báscula reiniciada")

# VOLVER A PESAR EN LA MISMA BÁSCULA

    def weigh_again(self):

        self._gross_weight = random.uniform(1.50, 10.50)
        self._net_weight = random.uniform(1.50, self._gross_weight)
        self._timestamp = str(self.timestamp_random())


# GENERAR FECHA Y HORA RANDOM

    def timestamp_random(self):
        initial_date = datetime(2010, 1, 1)
        end_date = datetime.now()
        delta = end_date - initial_date

        date_random = random.randint(0,delta.days)
        hour_random = random.randint(0,86400)

        final = initial_date + timedelta(days = date_random, hours = hour_random)
        return final.strftime('%Y-%m-%d %H:%M:%S')