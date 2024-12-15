DB_PATH = "_/secure_database_with_balances.db"

@anvil.server.callable
def secure_login(username, password):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT username, balance
            FROM users
            WHERE username = ? AND password = ?
        """, (username, password))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {"username": result[0], "balance": result[1]}
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
