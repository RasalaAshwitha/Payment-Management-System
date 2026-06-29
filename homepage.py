from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Welcome To Home Page....!!!"}


class Payment(BaseModel):
    Transaction_id: str
    Customer_name: str
    Product_name: str
    Quantity: int
    Unit_price: float
    Payment_method: str
    Payment_status: str
    Transaction_date: str
    Order_id: str
    Merchant_name: str
    Currency: str
    Remarks: str
    Total_amount: float


payments = []


# ----------------- CREATE -----------------
@app.post("/payments/")
def create_payment(payment: Payment):
    payments.append(payment.dict())
    return {
        "message": "Payment Successfully Added..!!",
        "data": payment
    }


# ----------------- READ ALL -----------------
@app.get("/payments/")
def read_payments():
    return payments


# ----------------- READ SINGLE -----------------
@app.get("/payments/{transaction_id}")
def read_single_payment(transaction_id: str):
    for payment in payments:
        if payment["Transaction_id"] == transaction_id:
            return payment

    return {"message": "Payment not found"}


# ----------------- UPDATE -----------------
@app.put("/payments/{transaction_id}")
def update_payment(transaction_id: str, payment: Payment):

    for p in payments:
        if p["Transaction_id"] == transaction_id:

            p["Transaction_id"] = payment.Transaction_id
            p["Customer_name"] = payment.Customer_name
            p["Product_name"] = payment.Product_name
            p["Quantity"] = payment.Quantity
            p["Unit_price"] = payment.Unit_price
            p["Payment_method"] = payment.Payment_method
            p["Payment_status"] = payment.Payment_status
            p["Transaction_date"] = payment.Transaction_date
            p["Order_id"] = payment.Order_id
            p["Merchant_name"] = payment.Merchant_name
            p["Currency"] = payment.Currency
            p["Remarks"] = payment.Remarks
            p["Total_amount"] = payment.Total_amount

            return {
                "message": "Payment Updated Successfully",
                "data": p
            }

    return {"message": "Payment not found"}


# ----------------- DELETE -----------------
@app.delete("/payments/{transaction_id}")
def delete_payment(transaction_id: str):

    for p in payments:
        if p["Transaction_id"] == transaction_id:
            payments.remove(p)

            return {
                "message": "Payment Deleted Successfully",
                "data": p
            }

    return {"message": "Payment not found"}