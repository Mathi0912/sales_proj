import streamlit as st
import numpy as np
import joblib

st.title("Demand Prediction App")

st.write("Enter inputs to predict demand")

# ---- USER INPUTS ----
price = st.number_input("Price", min_value=0.0)
discount = st.number_input("Discount", min_value=0.0)
inventory = st.number_input("Inventory_Level", min_value=0)
units_ordered = st.number_input("Units_Ordered", min_value=0)

# ---- DUMMY MODEL (TEMPORARY) ----
def predict_demand(price, discount, inventory, units_ordered):
    demand = (units_ordered * 0.6) + (inventory * 0.2) - (price * 0.1) + (discount * 0.3)
    return max(0, int(demand))

# ---- BUTTON ----
if st.button("Predict Demand"):
    result = predict_demand(price, discount, inventory, units_ordered)
    st.success(f"Predicted Demand: {result}")
