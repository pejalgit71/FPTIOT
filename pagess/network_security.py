import streamlit as st
import pandas as pd
import random
from datetime import datetime

def show():
    st.subheader("Network Security")
    st.write("Monitor network activity and simulate firewall configurations.")

    # Simulate Network Traffic
    # st.write("### Network Traffic Overview")
    # traffic_data = {
    #     "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(10)],
    #     "Source IP": [f"192.168.1.{random.randint(1, 255)}" for _ in range(10)],
    #     "Destination IP": [f"10.0.0.{random.randint(1, 255)}" for _ in range(10)],
    #     "Status": [random.choice(["Allowed", "Blocked"]) for _ in range(10)]
    # }
    # st.table(pd.DataFrame(traffic_data))


    # Network Traffic
    network_traffic = pd.read_csv('data/network_traffic.csv')
    st.write("### Network Traffic")
    st.table(network_traffic)

    # Firewall Rule Simulation
    st.write("### Firewall Rules")
    if st.button("Add Rule"):
        st.write("New firewall rule added!")
