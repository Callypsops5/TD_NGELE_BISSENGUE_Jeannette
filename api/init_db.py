import sqlite3
import os

DB_FILE = os.getenv("DB_FILE", "/data/db/dailyhabits.db")

# Créer le dossier data si nécessaire
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

conn = sqlite3.connect(DB_FILE)

conn.execute("""
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
)
""")
# Ajouter une habitude test si la table est vide
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM habits")
if cursor.fetchone()[0] == 0:
    cursor.execute(
        "INSERT INTO habits (name, description) VALUES (?, ?)",
        ("Boire 2L d’eau", "Hydratation quotidienne")
    )
conn.commit()
conn.close()
