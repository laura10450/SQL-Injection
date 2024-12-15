from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Placeholder text für Benutzername und Passwort
    self.benutzereingabe.placeholder = "Benutzername eingeben"
    self.passwort.placeholder = "Passwort eingeben"
    self.ausgabe_label.text = ""

  def passwort_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in the password text box"""
    self.Login_click()

  def benutzereingabe_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in the username text box"""
    self.passwort.focus()  # Set focus to the password text box

  def Login_click(self, **event_args):
    """This method is called when the Login button is clicked"""
    # Eingaben aus den Textboxen
    username = self.benutzereingabe.text
    password = self.passwort.text
    
    # Server-Aufruf zur Authentifizierung
    result = anvil.server.call('secure_login', username, password)
    
    if result:
      # Erfolg: Benutzername und Kontostand anzeigen
      self.ausgabe_label.text = f"Willkommen, {username}!\nKontostand: {result['balance']} €"
      self.ausgabe_label.foreground = "green"
    else:
      # Fehler: Meldung anzeigen
      self.ausgabe_label.text = "Login fehlgeschlagen. Überprüfen Sie Ihre Eingaben."
      self.ausgabe_label.foreground = "red"
