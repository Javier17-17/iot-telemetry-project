import random

class Scale:
    _grossWeight = None
    _netWeight = None
    _defect = None
    _ticket = None

# CONSTRUCTOR
def _init_(self, grossWeight, netWeight, defect, ticket):
    self._grossWeight = grossWeight
    self._netWeight = netWeight
    self._defect = defect
    self._ticket = ticket

# GETTERS
def getGrossWeight(self):
    return self._grossWeightproducto

def getNetWeight(self):
    return self._netWeight

def getDefect(self):
    return self._defect

def getTicket(self):
    return self._ticket

# OTRAS FUNCIONES Y/O MÉTODOS
def showAll(self, grossWeight, netWeight, defect, ticket):
    return f"Peso bruto: {self._grossWeight}"
    return f"Peso neto: {self._netWeight}"
    return f"Tara: {self._defect}"
    return f"Ticket: {self._ticket}"

def randomValueGenerator (self, grossWeight, netWeight, defect, ticket):
    grossWeightValue = random.uniform(1.5, 10.5)
    netWeightValue = random.uniform(1.5, 10.5)
    defectValue = random.randint(1, 4)
    ticketValue = random.uniform(1.5, 10.5)

def browseDefectsList():
    defectList = [1, 2, 3, 4]
    # 1 abollado= dented, 2 rayado= scratched, 3 abierto= open packaging, 4 otros= others
    #defectLis1=
