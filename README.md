# 💳 Payment Management System

A full-stack **Payment Management System** built using **FastAPI** and **Streamlit**. This application allows users to manage payment transactions by performing CRUD (Create, Read, Update, Delete) operations through a simple and interactive web interface.

> **Note:** This project stores data in memory (Python list) and does not use a database.

---

## 📌 Features

- ➕ Add new payment transactions
- 📄 View all payment records
- 🔍 View a single payment by Transaction ID
- ✏️ Update existing payment details
- 🗑️ Delete payment records
- 💰 Automatic total amount calculation
- 📱 Interactive Streamlit user interface
- ✅ FastAPI REST API with data validation using Pydantic

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- Pydantic
- Uvicorn

### Frontend
- Streamlit
- Requests

---

## 📂 Project Structure

```
Payment-Management-System/
│
├── backend.py
├── frontend.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/payment-management-system.git
```

```bash
cd payment-management-system
```

---

### 2. Create a Virtual Environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Backend

Start the FastAPI server using:

```bash
uvicorn backend:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Running the Frontend

```bash
streamlit run frontend.py
```

The Streamlit application will open automatically in your browser.

---

## 📋 Payment Details

The application stores the following information:

- Transaction ID
- Customer Name
- Product Name
- Quantity
- Unit Price
- Payment Method
- Payment Status
- Transaction Date
- Order ID
- Merchant Name
- Currency
- Remarks
- Total Amount

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home Page |
| POST | `/payments/` | Create a Payment |
| GET | `/payments/` | View All Payments |
| GET | `/payments/{transaction_id}` | View Single Payment |
| PUT | `/payments/{transaction_id}` | Update Payment |
| DELETE | `/payments/{transaction_id}` | Delete Payment |

---

## 📷 Application Screenshots

### Home Page

_Add screenshot here_

### Transaction Entry Form

_Add screenshot here_

### Payment Details

_Add screenshot here_

---

## 📚 What I Learned

During this project, I learned:

- Building REST APIs with FastAPI
- Creating data models using Pydantic
- Implementing CRUD operations
- Connecting FastAPI with Streamlit
- Sending HTTP requests using the Requests library
- Working with JSON data
- Building beginner-level full-stack Python applications

---

## 🚀 Future Enhancements

- Store data using SQLite/MySQL
- User Login & Authentication
- Search and Filter Transactions
- Export Payments to CSV/PDF
- Dashboard with Payment Analytics
- Pagination for Payment Records
- Payment History Reports

---

## 👩‍💻 Author

**Ashwitha Rasala**

Aspiring Python Full-Stack Developer

- Python
- FastAPI
- Streamlit
- REST API Development

---

## 📄 License

This project is developed for educational and learning purposes.
