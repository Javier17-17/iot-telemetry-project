from src.simulator.Drying import Drying
from src.simulator.Scale import Scale
import traceback

# PRIMERA PRUEBA BÁSCULA
scale = Scale()
print("Peso bruto: ", scale._gross_weight)
print("Peso neto: ", scale._net_weight)
    #print(scale.get_net_weight())
    #traceback.print_exc()

# REINICIAR BÁSCULA AL PULSAR TARA
scale.press_tare()

# SEGUNDA PRUEBA BÁSCULA
print("Peso bruto: ", scale._gross_weight)
print("Peso neto: ", scale._net_weight)

# GENERAR NUEVA BÁSCULA CON DATOS RANDOM
scale2 = Scale()
scale2.generate_ticket()

print("Peso bruto: ", scale2._gross_weight)
print("Peso neto: ", scale2._net_weight)

# SECADERO

drying = Drying()

"""
print("Temperatura: ", drying._temperature)
print("Humedad: ", drying._humidity)
print("fecha y hora: ", drying._date_time_drying)
"""