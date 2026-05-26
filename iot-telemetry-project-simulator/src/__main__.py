from src.simulator.DataSender import DataSender
from src.simulator.Drying import Drying
from src.simulator.JsonConverter import JsonConverter
from src.simulator.Scale import Scale
import traceback

# PRIMERA PRUEBA BÁSCULA
scale = Scale()
print("id máquina: ", scale._device_id)
print("Peso bruto: ", scale._gross_weight)
print("Peso neto: ", scale._net_weight)
print("Fecha y hora: ", scale._timestamp)
    #print(scale.get_net_weight())
    #traceback.print_exc()

# REINICIAR BÁSCULA AL PULSAR TARA
scale.press_tare()

# VOLVER A PESAR
print("volver a pesar")
scale.weigh_again()
print("id máquina: ", scale._device_id)
print("Peso bruto: ", scale._gross_weight)
print("Peso neto: ", scale._net_weight)
print("Fecha y hora: ", scale._timestamp)

# SEGUNDA PRUEBA BÁSCULA
scale2 = Scale()
print("id máquina: ", scale._device_id)
print("Peso bruto: ", scale._gross_weight)
print("Peso neto: ", scale._net_weight)
print("Fecha y hora: ", scale._timestamp)

# SECADERO

drying = Drying()

# JSON
print("PRUEBA JSON")
scale_data = JsonConverter.json(scale2.__dict__)
drying_data = JsonConverter.json(drying.__dict__)

# DATASENDER

print("PRUEBA DATASENDER")
DataSender.send_data(scale_data)