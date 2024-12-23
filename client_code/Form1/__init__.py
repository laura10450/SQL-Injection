from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):

    self.init_components(**properties)


    self.benutzereingabe.placeholder = "Benutzername eingeben"
    self.passwort.placeholder = "Passwort eingeben"
    self.ausgabe_label.text = ""

  def passwort_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in the password text box"""
    self.Login_click()

  def benutzereingabe_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in the username text box"""
    self.passwort.focus() 

  def Login_click(self, **event_args):
    """This method is called when the Login button is clicked"""

    username = self.benutzereingabe.text
    password = self.passwort.text
    

    try:
      result = anvil.server.call('secure_login', username, password)
      
      if result:

        self.ausgabe_label.text = f"Willkommen, {result['username']}!\nKontostand: {result['balance']} €"
        self.ausgabe_label.foreground = "green"
      else:

        self.ausgabe_label.text = "Login fehlgeschlagen. Überprüfen Sie Ihre Eingaben."
        self.ausgabe_label.foreground = "red"
    
    except anvil.server.AnvilError as e:
      alert(f"Server Error: {e}")
