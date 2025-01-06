import streamlit as st

# Importing pages
from pages import (
    physical_security,
    iot_monitoring,
    network_security,
    threat_detection,
    pipeline_monitoring,
    cloud_reports
)

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Select a Function", [
    "Introduction",
    "Physical Security",
    "IoT Device Monitoring",
    "Network Security",
    "Threat Detection and Response",
    "Pipeline Monitoring",
    "Cloud Integration & Reports"
])

# Main Content
if menu == "Introduction":
    st.title("IoT and EoT Security Framework Simulation")
    st.write("""
    Welcome to the IoT and EoT Security Framework Simulation.  
    Use the navigation on the left to explore different functions.
    Project by UTP TEAM 2025
    """)
elif menu == "Physical Security":
    physical_security.show()
elif menu == "IoT Device Monitoring":
    iot_monitoring.show()
elif menu == "Network Security":
    network_security.show()
elif menu == "Threat Detection and Response":
    threat_detection.show()
elif menu == "Pipeline Monitoring":
    pipeline_monitoring.show()
elif menu == "Cloud Integration & Reports":
    cloud_reports.show()
