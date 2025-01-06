import streamlit as st
import pandas as pd
import random
from datetime import datetime

def show():
    st.subheader("IoT Device Monitoring")
    st.write("View real-time data from IoT sensors.")

    # Simulated IoT Sensor Data
    # st.write("### Sensor Data")
    # sensors = ["Temperature", "Pressure", "Vibration", "Humidity"]
    # sensor_data = {sensor: [round(random.uniform(20, 100), 2) for _ in range(5)] for sensor in sensors}
    # sensor_data["Timestamp"] = [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(5)]
    # st.table(pd.DataFrame(sensor_data))


    # Sensor Data
    sensor_data = pd.read_csv('data/sensor_data.csv')
    st.write("### IoT Sensor Data")
    st.table(sensor_data)