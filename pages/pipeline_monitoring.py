import streamlit as st
import pandas as pd
import random

def show():
    st.subheader("Pipeline Monitoring")
    st.write("Simulate real-time monitoring for pipelines.")

    # Pipeline Integrity Simulation
    st.write("### Pipeline Status")
    pipeline_status = random.choice(["Normal", "Leak Detected", "Pressure Drop"])
    if pipeline_status == "Normal":
        st.success("Pipeline operating normally.")
    else:
        st.error(f"Pipeline Alert: {pipeline_status} detected!")

    # Pipeline Sensor Data
    # st.write("### Pipeline Sensor Data")
    # pipeline_data = {
    #     "Sensor": ["Pressure", "Temperature", "Vibration"],
    #     "Value": [round(random.uniform(50, 150), 2) for _ in range(3)],
    #     "Status": ["OK", "OK", "OK"]
    # }
    # st.table(pd.DataFrame(pipeline_data))


    # Pipeline Data
    pipeline_data = pd.read_csv('data/pipeline_data.csv')
    st.write("### Pipeline Status")
    st.table(pipeline_data)