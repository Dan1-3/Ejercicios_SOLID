"""
Ejemplo del principio de Abierto/Cerrado (OCP) de SOLID, 
con una calculadora para sumar, restar, multiplicar, dividir

Necesito que el codigo sea sin tocar nada, para que no tenga que pasar los parametros, para ello usamos los diccionarios
"""
from abc import ABC, abstractmethod

class Operacion(ABC):
  @abstractmethod
  def calcular(self, a, b):
    pass

class Suma(Operacion):
  def calcular(self, a, b):
    return a + b

class Resta(Operacion):
  def calcular(self, a, b):
    return a - b

class Multiplicacion(Operacion):
  def calcular(self, a, b):
    return a * b

class Division(Operacion):
  def calcular(self, a, b):
    return a / b

# Tiene que seguir el principio de abierto/cerrado, sin modificar la calse Calculadora
# Si quiero añadir una nueva operación, no tengo que tocar la clase Calculadora
class Calculadora:
  def __init__(self):
    self.operaciones = {}
  
# Metodo de agreagar operaciones
  def añadir_operacion(self, nombre, operacion):
    self.operaciones[nombre] = operacion
  
  def calcular(self, nombre, a, b):
    if nombre not in self.operaciones:
      print("Operación no soportada")

    return self.operaciones[nombre].calcular(a, b)

# Probamos la calculadora
calculadora = Calculadora()
calculadora.añadir_operacion("suma", Suma())
calculadora.añadir_operacion("resta", Resta())
calculadora.añadir_operacion("multiplicacion", Multiplicacion())
calculadora.añadir_operacion("division", Division())

print("Suma: ", calculadora.calcular("suma", 5, 3))
print("Resta: ", calculadora.calcular("resta", 5, 3))
print("Multiplicación: ", calculadora.calcular("multiplicacion", 5, 3))
print("División: ", calculadora.calcular("division", 5, 3)) 

# Intentamos añadir una nueva operación sin modificar la clase Calculadora, de potencias
class Potencia(Operacion):
  def calcular(self, a, b):
    return a ** b

calculadora.añadir_operacion("potencia", Potencia())