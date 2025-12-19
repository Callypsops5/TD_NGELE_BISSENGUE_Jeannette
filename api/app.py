import sqlite3
import os
from flask import Flask, jsonify

app = Flask(__name__)
DB_FILE = os.getenv("DB_FILE", "/data/db/dailyhabits.db")

@app.route("/status")
def status():
    return jsonify({"status": "OK"})

@app.route("/items")
def items():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description FROM habits")
        rows = cursor.fetchall()
        conn.close()
        items = [{"id": r[0], "name": r[1], "description": r[2]} for r in rows]
        return jsonify(items)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    HTTP_PORT = int(os.getenv("API_PORT", 8080))
    app.run(host="0.0.0.0", port=HTTP_PORT)
