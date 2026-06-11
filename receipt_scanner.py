import easyocr
import pickle

# Load OCR
reader = easyocr.Reader(['en'])

# Load ML model
model = pickle.load(open("receipt_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Read receipt
result = reader.readtext("sample_receipt.jpg")

for item in result:

    text = item[1]

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)

    print(f"{text} --> {prediction[0]}")