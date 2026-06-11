# 📄 AI Receipt Scanner

An AI-powered receipt scanner that uses OCR and Machine Learning to automatically extract and categorize receipt items, store purchase history, and generate monthly analytics.

---

## 🚀 Features

### Receipt Scanning

* Upload receipt images
* Extract text using EasyOCR
* Automatically detect purchased items
* Categorize items using Machine Learning

### Purchase History

* Store scanned items in SQLite
* Track merchants
* Maintain scan dates

### Monthly Analytics

* View monthly purchase trends
* Identify most purchased items
* Track purchases by merchant

### Category Insights

* Interactive Pie Chart
* Category-wise purchase breakdown
* Food vs Shopping analysis

---

## 🛠 Tech Stack

### Backend

* Python
* Flask
* SQLite
* EasyOCR
* Scikit-Learn

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Database

* SQLite

---

## 📸 Screenshots

Add screenshots of:

1. Upload Screen
2. Receipt Results
3. Monthly Analytics
4. Pie Chart Dashboard

Example:

![Dashboard](screenshots/dashboard.png)

---

## 📂 Project Structure

receipt-scanner/

├── app.py

├── receipt.db

├── receipt_model.pkl

├── vectorizer.pkl

├── index.html

├── requirements.txt

└── README.md

---

## ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/Uttkarsh-10/receipt-scanner.git
cd receipt-scanner
```

Create environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📊 Example Analytics

| Merchant    | Item    | Total |
| ----------- | ------- | ----- |
| Burger King | Whopper | 12    |
| Burger King | Fries   | 8     |
| Starbucks   | Latte   | 5     |

---

## 🔮 Future Improvements

* Receipt image storage
* User authentication
* Spending analytics
* Monthly spending reports
* Merchant ranking
* Expense prediction
* Cloud deployment

---

## 👨‍💻 Author

Uttkarsh Arya

GitHub:
https://github.com/Uttkarsh-10
