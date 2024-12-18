import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import sqlite3
import anvil.server

@anvil.server.callable
def secure_login(username, password):
    """
    Sichere Login-Funktion, die die SQLite-Datenbank verwendet.
    """
    try:
        # Lokalen Pfad zur hochgeladenen Datei verwenden
        db_path = "/_/secure_database_with_balances.db"


        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # SQL-Abfrage ausführen
        cursor.execute("""
            SELECT username, balance
            FROM users
            WHERE username = ? AND password = ?
        """, (username, password))

        result = cursor.fetchone()
        conn.close()

        if result:
            print(f"Login erfolgreich für Benutzer: {result[0]}")
            return {"username": result[0], "balance": result[1]}
        else:
            print("Login fehlgeschlagen: Ungültige Anmeldedaten.")
            return None

    except sqlite3.Error as e:
        print(f"SQLite-Fehler: {e}")
        return None
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        return None
