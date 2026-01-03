import streamlit as st
import numpy as np

st.title("Demand Prediction App")

st.write("Enter inputs to predict demand")

price = st.number_input("Price", min_value=0.0)
discount = st.number_input("Discount", min_value=0.0)
inventory = st.number_input("Inventory Level", min_value=0)
units_ordered = st.number_input("Units Ordered", min_value=0)

def predict_demand(price, discount, inventory, units_ordered):
    demand = (units_ordered * 0.6) + (inventory * 0.2) - (price * 0.1) + (discount * 0.3)
    return max(0, int(demand))

if st.button("Predict Demand"):
    result = predict_demand(price, discount, inventory, units_ordered)
    st.success(f"Predicted Demand: {result}")
