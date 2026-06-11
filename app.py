from flask import Flask, request, jsonify
from flask_cors import CORS
import easyocr
import pickle
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

print("CURRENT DIRECTORY:", os.getcwd())
print("DB PATH:", os.path.abspath("receipt.db"))

print("RECEIPT SCANNER STARTED")

# OCR Reader
reader = easyocr.Reader(['en'])

# Load ML Model
model = pickle.load(open("receipt_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Words to ignore
ignore_words = [
    "phone",
    "tax",
    "total",
    "subtotal",
    "survey",
    "visa",
    "auth",
    "host",
    "order",
    "check",
    "code",
    "payment",
    "balance"
]


@app.route("/")
def home():
    return "Receipt Scanner API Running"


@app.route("/scan", methods=["POST"])
def scan_receipt():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]

    image_path = image.filename
    image.save(image_path)

    result = reader.readtext(image_path)

    merchant = "Unknown"

    for r in result:
        candidate = r[1].strip()

        if len(candidate) > 4:
            merchant = candidate
            break

    predictions = []

    conn = sqlite3.connect("receipt.db")
    cursor = conn.cursor()

    for r in result:

        text = r[1].strip()
        text = " ".join(text.split())

        if not text:
            continue

        # Skip merchant itself
        if text == merchant:
            continue

        text_lower = text.lower()

        if len(text) < 4:
            continue

        if any(word in text_lower for word in ignore_words):
            continue

        if any(char.isdigit() for char in text) and len(text) > 6:
            continue

        vector = vectorizer.transform([text])

        prediction = model.predict(vector)[0]

        confidence = float(
            model.predict_proba(vector).max()
        )

        if confidence < 0.35:
            continue

        print("SAVING:", merchant, text, prediction)

        cursor.execute("""
        INSERT INTO receipt_items
        (merchant, item, category, scan_date)
        VALUES (?, ?, ?, ?)
        """,
        (
            merchant,
            text,
            prediction,
            datetime.now().strftime("%Y-%m-%d")
        ))

        predictions.append({
            "text": text,
            "category": prediction,
            "confidence": round(confidence, 2)
        })

    conn.commit()
    conn.close()

    if os.path.exists(image_path):
        os.remove(image_path)

    return jsonify(predictions)


@app.route("/top-items")
def top_items():

    conn = sqlite3.connect("receipt.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT merchant,
           item,
           COUNT(*) as total
    FROM receipt_items
    GROUP BY merchant, item
    ORDER BY total DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return jsonify(results)


@app.route("/monthly")
def monthly():

    conn = sqlite3.connect("receipt.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        strftime('%Y-%m', scan_date) as month,
        merchant,
        item,
        COUNT(*) as total
    FROM receipt_items
    GROUP BY month, merchant, item
    ORDER BY total DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return jsonify(results)

@app.route("/category-summary")
def category_summary():

    conn = sqlite3.connect("receipt.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category,
           COUNT(*) as total
    FROM receipt_items
    GROUP BY category
    """)

    results = cursor.fetchall()

    conn.close()

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)