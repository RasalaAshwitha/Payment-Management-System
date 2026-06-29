import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.markdown("# 🛒 Welcome Payment Management System 🛍️")
st.header("Transaction Entry Form")

Transaction_id = st.text_input("Transaction ID")
Customer_name = st.text_input("Customer Name")
Product_name = st.text_input("Product Name")

Quantity = st.number_input("Quantity", min_value=1, step=1)
Unit_price = st.number_input("Unit Price", min_value=0.0)

Payment_method = st.selectbox(
    "Payment Method",
    ["Select", "📱UPI", "💳Credit Card", "💳Debit Card", "🏦Net Banking", "💸Cash"]
)

Payment_status = st.selectbox(
    "Payment Status",
    ["Select", "✅Success", "⏳Pending", "❌Failed"]
)

Transaction_date = st.date_input("Transaction Date")

Order_id = st.text_input("Order ID")

Merchant_name = st.text_input("Merchant Name")

Currency = st.selectbox(
    "Currency",
    ["INR", "USD", "EUR"]
)

Remarks = st.text_area("📝 Remarks", "Optional")

Total_amount = Quantity * Unit_price

st.write(f"### 💰 Total Amount: ₹{Total_amount}")

if st.button("Submit Payment"):

    if Payment_method == "Select" or Payment_status == "Select":
        st.warning("Please select Payment Method and Payment Status.")

    else:

        data = {
            "Transaction_id": Transaction_id,
            "Customer_name": Customer_name,
            "Product_name": Product_name,
            "Quantity": Quantity,
            "Unit_price": Unit_price,
            "Payment_method": Payment_method,
            "Payment_status": Payment_status,
            "Transaction_date": str(Transaction_date),
            "Order_id": Order_id,
            "Merchant_name": Merchant_name,
            "Currency": Currency,
            "Remarks": Remarks,
            "Total_amount": Total_amount
        }

        response = requests.post(
            f"{API}/payments/",
            json=data
        )

        if response.status_code == 200:

            if Payment_status == "✅Success":
                st.success("Transaction Submitted Successfully!")

            elif Payment_status == "⏳Pending":
                st.warning("Transaction is Pending!")

            elif Payment_status == "❌Failed":
                st.error("Transaction Failed!")

            st.subheader("Submitted Transaction Details")
            st.json(data)

        else:
            st.error("Failed to send data to FastAPI.")