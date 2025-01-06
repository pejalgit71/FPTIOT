import streamlit as st
import pandas as pd
import random

def show():
    st.subheader("Threat Detection and Response")
    st.write("Simulate threat detection and automated responses.")

    # Anomaly Detection Simulation
    st.write("### Anomaly Detection")
    # anomaly = random.choice(["No Anomaly", "Anomaly Detected"])
    anomaly_data = pd.read_csv('data/anomaly_data.csv')
    st.write("### Anomaly Detection Logs")
    st.table(anomaly_data)
    
    # if anomaly == "Anomaly Detected":
    #     st.error("Anomaly Detected: Unauthorized access attempt!")
    #     st.button("Activate Response")
    # else:
    #     st.success("System Operating Normally.")


    
