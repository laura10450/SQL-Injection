import sqlite3
import anvil.server

@anvil.server.callable
def secure_login(username, password):
    """
    Sichere Login-Funktion, die die SQLite-Datenbank im Arbeitsspeicher verwendet.
    """
    try:
        # Datei aus dem Assets-Bereich laden
        with open("_/secure_database_with_balances_fixed.db", "rb") as db_file:
            db_bytes = db_file.read()

        # Verbindung zur In-Memory-Datenbank herstellen
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()

        # Datenbank in den Arbeitsspeicher laden
        conn.executescript(db_bytes.decode("utf-8"))

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
