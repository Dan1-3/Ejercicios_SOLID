"""
Crea un sistema de notificaciones.
 Requisitos:
 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 2. El sistema de notificaciones no puede depender de las implementaciones específicas.

 Instrucciones:
 1. Crea la interfaz o clase abstracta.
 2. Desarrolla las implementaciones específicas.
 3. Crea el sistema de notificaciones usando el DIP.
 4. Desarrolla un código que compruebe que se cumple el principio.
 """
from abc import ABC, abstractmethod

class AbstractNotificar(ABC):
  @abstractmethod
  def enviar_mensaje():
    pass

class NotificarEmail(AbstractNotificar):
  def enviar_mensaje(self, mensaje, destinatario):
    print(f"Enviando Email a {destinatario}: {mensaje}")

class NotificarPush(AbstractNotificar):
  def enviar_mensaje(self, mensaje, destinatario):
    print(f"Enviando notificación PUSH a {destinatario}: {mensaje}")

class NotificarSMS(AbstractNotificar):
  def enviar_mensaje(self, mensaje, destinatario):
    print(f"Enviando SMS a {destinatario}: {mensaje}")


class Email:
  def __init__(self, notificador: AbstractNotificar) -> None:
    self.notificador = notificador

  def notificar(self, mensaje, destinatario):
    self.notificador.enviar_mensaje(mensaje, destinatario)

class Push:
  def __init__(self, notificador: AbstractNotificar) -> None:
    self.notificador = notificador

  def notificar(self, mensaje, destinatario):
    self.notificador.enviar_mensaje(mensaje, destinatario)

class SMS:
  def __init__(self, notificador: AbstractNotificar) -> None:
    self.notificador = notificador

  def notificar(self, mensaje, destinatario):
    self.notificador.enviar_mensaje(mensaje, destinatario)

email_notificador = Email(NotificarEmail())
email_notificador.notificar("Notificacion en Email", "usuario1@gmail.com")

push_notificador = Push(NotificarPush())
push_notificador.notificar("Notificacion en Push", "UsuarioApp")

sms_notificador = SMS(NotificarSMS())
sms_notificador.notificar("Notificacion en SMS", "+1234567890")