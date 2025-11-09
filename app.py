app.py
import streamlit as st

st.title("🏠 Real Estate Price Predictor")

st.write("Enter details to estimate house price")

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
area = st.number_input("Area (in sq ft)", min_value=300, max_value=10000, value=1200)

if st.button("Predict Price"):
    price = (area * 5000) + (bedrooms * 100000) + (bathrooms * 50000)
    st.success(f"Estimated Price: {price:,}")
