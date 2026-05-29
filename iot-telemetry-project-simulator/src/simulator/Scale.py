import random
from datetime import datetime
import uuid


class Scale:
    _device_id = None
    _gross_weight = None
    _net_weight = None
    _timestamp = None

    # CONSTRUCTOR
    def __init__(self):
        self._device_id = str(uuid.uuid4())
        self.weigh_again()

    # GETTERS
    def get_gross_weight(self):
        return self._gross_weight

    def get_net_weight(self):
        return self._net_weight

    # PULSAR BOTON DE TARA
    def press_tare(self):
        self._gross_weight = 0
        self._net_weight = 0

        print("bascula reiniciada")

    # VOLVER A PESAR EN LA MISMA BASCULA
    def weigh_again(self):
        self._gross_weight = random.uniform(1.50, 10.50)
        self._net_weight = random.uniform(1.50, self._gross_weight)
        self._timestamp = str(self.timestamp_random())

    # GENERAR FECHA Y HORA ACTUAL
    def timestamp_random(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')