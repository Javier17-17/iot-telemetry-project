import random
from datetime import datetime


class Scale:
    _gross_weight = None
    _net_weight = None
    _ticket = None
    _date_time_scale = None

    # CONSTRUCTOR

    def __init__(self):

        self._gross_weight = random.uniform(1.50, 10.50)
        self._net_weight = random.uniform(1.50, self._gross_weight)

# GETTERS
    def get_gross_weight(self):
        return self._gross_weight

    def get_net_weight(self):
        return self._net_weight

    def get_ticket(self):
        return self._ticket

# PULSAR BOTÓN DE TARA

    def press_tare(self):
        self._gross_weight = 0
        self._net_weight = 0

        print("báscula reiniciada")

# GENERAR UN TICKET
    def generate_ticket(self):
        gross_weight = self._gross_weight
        net_weight = self._net_weight
        _date_time_scale= datetime.now()
        print("TICKET")
        print("fecha y hora: ",_date_time_scale)




