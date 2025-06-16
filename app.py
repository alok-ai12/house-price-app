import streamlit as st
import pickle
import numpy as np

# 🔹 1. Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# 🔹 2. Streamlit App title
st.title("🏠 House Price Prediction App")

# 🔹 3. User input fields
area = st.number_input("📏 Enter Area (in sqft):")
bedrooms = st.slider("🛏️ Number of Bedrooms:", 1, 5)
age = st.number_input("📅 Age of House (in years):")

# 🔹 4. Predict button
if st.button("📊 Predict Price"):
    # Convert input into array
    features = np.array([[area, bedrooms, age]])
    prediction = model.predict(features)
    st.success(f"💰 Estimated Price: ₹ {int(prediction[0])}")
