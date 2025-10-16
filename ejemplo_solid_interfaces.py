"""
Crea un gestor de impresoras.

 Requisitos:
 1. Algunas impresoras sólo imprimen en blanco y negro.
 2. Otras sólo a color.
 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.

 Instrucciones:
 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 2. Aplica el ISP a la implementación.
 3. Desarrolla un código que compruebe que se cumple el principio.
 """

# ISP--> este principio dice que las clases no deben depender de métodos que no utilizan.

# Creamos las diferentes interfaces para los distintos tipos de impresoras, que no tengas que modificarlas, 
# y si necesitas alguna mas, se añaden, y asi tambien se cumple el principio abierto-cerrado

class scan_interface:
    def escanear(self, documento):
        print(f"Escaneando documento: {documento}")

class imprimir_color_interface:
    def imprimir_color(self, documento):
        print(f"Imprimiendo a color: {documento}")

class imprimir_blanco_negro_interface:
    def imprimir_blanco_negro(self, documento):
        print(f"Imprimiendo en blanco y negro: {documento}")

class fax_interface:
    def enviar_fax(self, documento, numero_fax):
        print(f"Enviando fax a {numero_fax}: {documento}")

# Creamos las diferentes clases de impresoras que cumplen con el principio isp
class impresora_blanco_negro(imprimir_blanco_negro_interface):
    def imprimir_blanco_negro(self, documento):
        print(f"Imprimiendo en blanco y negro: {documento}")

class impresora_color(imprimir_color_interface):
    def imprimir_color(self, documento):
        print(f"Imprimiendo a color: {documento}")

class impresora_multifuncion(scan_interface,imprimir_color_interface, imprimir_blanco_negro_interface, fax_interface):
    def escanear(self, documento):
        print(f"Escaneando documento: {documento}")

    def imprimir_color(self, documento):
        print(f"Imprimiendo a color: {documento}")

    def imprimir_blanco_negro(self, documento):
        print(f"Imprimiendo en blanco y negro: {documento}")

    def enviar_fax(self, documento, numero_fax):
        print(f"Enviando fax a {numero_fax}: {documento}")

"""
Si ahora te pidieran una que solo tuviera Fax y Imprimir a color, te creas una clase impresora_fax_color que implemente solo esas dos interfaces.
"""

# Probamos las diferentes clases de impresoras que cumplen con el principio isp
impresora_blanco_negro = impresora_blanco_negro()
impresora_blanco_negro.imprimir_blanco_negro("Documento 1")

impresora_color = impresora_color()
impresora_color.imprimir_color("Documento 2")

impresora_multifuncion = impresora_multifuncion()
impresora_multifuncion.escanear("Documento 3")
impresora_multifuncion.imprimir_color("Documento 4")
impresora_multifuncion.imprimir_blanco_negro("Documento 5")
impresora_multifuncion.enviar_fax("Documento 6", "412")
