import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("📊 Real Estate Price Predictor")

area = st.slider("🏡 Area (in sq ft)", 500, 5000, step=100)
bedrooms = st.slider("🛏️ Bedrooms", 1, 10)
bathrooms = st.slider("🛁 Bathrooms", 1, 10)

if st.button("📈 Predict Price"):
    pred = model.predict([[area, bedrooms, bathrooms]])
    st.success(f"💰 Estimated Price: ₹{round(pred[0], 2)}")
