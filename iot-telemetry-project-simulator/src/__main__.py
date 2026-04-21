from src.simulator.Scale import Scale
import traceback

# PRIMERA PRUEBA BÁSCULA
scale = Scale()
print("Peso bruto: ", scale._gross_weight)
print("Peso neto: ", scale._net_weight)
    #print(scale.get_net_weight())
    #traceback.print_exc()

# REINICIAR BÁSCULA AL PULSAR TARA
print (scale.press_tare())

# SEGUNDA PRUEBA BÁSCULA
print("Peso bruto: ", scale._gross_weight)
print("Peso neto: ", scale._net_weight)