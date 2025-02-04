import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
model_filename = "linear_regression_model.pkl"

try:
    with open(model_filename, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("❌ Model file not found. Please upload 'linear_regression_model.pkl' to the GitHub repo.")

# Streamlit UI
st.title("🔍 SYN Attack CPU Usage Predictor")
st.write("Adjust the sliders to predict CPU usage based on SYN attack parameters.")

# User Inputs via Sidebar
incoming_syn_rate = st.sidebar.slider("📊 Incoming SYN Rate (packets/sec)", min_value=0, max_value=5000, value=1000, step=10)
network_traffic = st.sidebar.slider("📡 Network Traffic (KB/s)", min_value=0, max_value=5000, value=1500, step=10)

# ✅ Fix: Convert input into a DataFrame with column names
input_features = pd.DataFrame([[incoming_syn_rate, network_traffic]], columns=['incoming_syn_rate', 'network_traffic'])

# Predict CPU usage
if 'model' in locals():
    predicted_cpu_usage = model.predict(input_features)[0]
    st.subheader("🖥️ Predicted CPU Usage")
    st.write(f"**{predicted_cpu_usage:.2f}%**")
else:
    st.error("❌ Model not loaded. Check if 'linear_regression_model.pkl' exists.")

# Footer
st.markdown("Developed for SYN Attack Analysis 🚀")
