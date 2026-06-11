import sqlite3

conn = sqlite3.connect("receipt.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS receipt_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    merchant TEXT,
    item TEXT,
    category TEXT,
    scan_date TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")