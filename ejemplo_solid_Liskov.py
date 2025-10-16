# Principio de Liskov
""" 
Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como cumplir el LSP.
 Instrucciones:
 1. Crea la clase Vehículo.
 2. Añade tres subclases de Vehículo.
 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 4. Desarrolla un código que compruebe que se cumple el LSP.
 """

class Vehiculo:
  def __init__(self, velocidad=0):
    self.velocidad = velocidad

  def acelerar(self, incremento):
    self.velocidad += incremento
    print(f"El vehiculo acelera a una velocidad de {self.velocidad} km/h")

  def frenar(self, decremento):
    self.velocidad -= decremento
    print(f"El vehiculo frena a una velocidad de {self.velocidad} km/h")

# Las subclases de Vehiculo
class Coche(Vehiculo):
  def acelerar(self, incremento):
    print("El coche acelera")
    super().acelerar(incremento)

  def frenar(self, decremento):
    print("El coche frena")
    super().frenar(decremento)

class Camion(Vehiculo):
  def acelerar(self, incremento):
    print("El camión acelera")
    super().acelerar(incremento)

  def frenar(self, decremento):
    print("El camión frena")
    super().frenar(decremento)

class Moto(Vehiculo):
  def acelerar(self, incremento):
    print("La moto acelera")
    super().acelerar(incremento)

  def frenar(self, decremento):
    print("La moto frena") 
    super().frenar(decremento)

# Comprobacion del LSP, todas las clases pueden ser usadas indistintamente
def probar_vehiculo(vehiculo):
  vehiculo.acelerar(20)
  vehiculo.frenar(10)

vehiculo = Vehiculo()
coche = Coche()
camion = Camion()
moto = Moto()

# Entre estos, podemos cambiarlos ya que todos cumplen el LSP y pueden funcionar igualmente
probar_vehiculo(vehiculo)
probar_vehiculo(coche)
probar_vehiculo(camion)
probar_vehiculo(moto)
