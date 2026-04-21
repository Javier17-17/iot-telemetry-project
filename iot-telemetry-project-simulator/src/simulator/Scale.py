import random
from re import fullmatch


class Scale:
    _gross_weight = None
    _net_weight = None
    #_ticket = None
    #_random_value_generator()

    # CONSTRUCTOR

    def __init__(self):
        #print("aaa")
        self._gross_weight = random.uniform(1.50, 10.50)
        self._net_weight = random.uniform(1.50, self._gross_weight)

# GETTERS
    def get_gross_weight(self):
        return self._gross_weight

    def get_net_weight(self):
        return self._net_weight

    def get_ticket(self):
        return self._ticket

# OTRAS FUNCIONES Y/O MÉTODOS

    def press_tare(self):
        _gross_weight = 0
        _net_weight = 0





