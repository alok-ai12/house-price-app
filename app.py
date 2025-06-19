import streamlit as st
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Title
st.title("🏡 Real Estate Price Predictor")

# Inputs
area = st.slider("📐 Area (in sq ft)", 500, 5000, step=100)
bedrooms = st.slider("🛏️ Bedrooms", 1, 10)
bathrooms = st.slider("🛁 Bathrooms", 1, 10)

# Train dummy model (example)
X = np.array([
    [1000, 2, 1],
    [1500, 3, 2],
    [1800, 4, 3],
    [2500, 4, 2],
    [3000, 5, 4],
])
y = [50, 75, 90, 120, 150]

model = RandomForestRegressor()
model.fit(X, y)

# Predict
if st.button("📉 Predict Price"):
    input_data = [[area, bedrooms, bathrooms]]
    pred = model.predict(input_data)
    st.success(f"💰 Estimated Price: ₹{round(pred[0], 2)} lakhs")
