import sqlite3

# Initialize database connection
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    service TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL)""")
conn.commit()

def add_password(service, username, encrypted_password):
    """Add a password to the database."""
    cursor.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
                   (service, username, encrypted_password))
    conn.commit()

def get_password(service):
    """Retrieve a password from the database."""
    cursor.execute("SELECT username, password FROM passwords WHERE service = ?", (service,))
    return cursor.fetchone()
