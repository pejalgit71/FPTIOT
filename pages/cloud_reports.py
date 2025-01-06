import streamlit as st
import pandas as pd
import random

def show():
    st.subheader("Cloud Integration and Reporting")
    st.write("Visualize reports and system performance.")

    # System Performance Report
    # st.write("### System Performance")
    # performance_data = {
    #     "Metric": ["CPU Usage", "Memory Usage", "Network Latency"],
    #     "Value (%)": [round(random.uniform(10, 90), 2) for _ in range(3)]
    # }
    # st.table(pd.DataFrame(performance_data))

   
    # Performance Data
    performance_data = pd.read_csv('data/performance_data.csv')
    st.write("### System Performance Metrics")
    st.table(performance_data)

     # Generate Reports
    if st.button("Generate Report"):
        st.success("Report Generated Successfully!")
