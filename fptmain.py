import streamlit as st

# Importing pages
from pagess import (
    physical_security,
    iot_monitoring,
    network_security,
    threat_detection,
    pipeline_monitoring,
    cloud_reports,
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
    st.title("IoT and EoT Security Framework Simulation FPT-UTP")

    html_content = """
    <!DOCTYPE html>
    <html>
    <title>W3.CSS</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lobster">
    <style>
    .w3-lobster {
      font-family: "Lobster", serif;
    }
    </style>
    <body>
    
    <div class="w3-container w3-lobster">
     <!-- <p class="w3-xlarge font-effect-shadow-multiple">Making the Web!</p> -->
      <p class="w3-xxlarge">FPT IOT Project 2025</p>
      <p class="w3-xlarge">Project Manager: Dr. Norashikin Bt Yahya</p>
      <p class="w3-xlarge">Member: Dr. Nasreen Bt Badruddin</p>
      <p class="w3-xlarge">Member: Ts Faizal Ahmad Fadzil</p>
      
     <!-- <p class="w3-xxxlarge font-effect-shadow-multiple">Making the Web!</p> -->
    </div>
    
    </body>
    </html>
    """
    
    # Embed the HTML in Streamlit
    st.components.v1.html(html_content, height=300)

elif menu == "Physical Security":
    physical_security.show()  # Ensure no st.sidebar logic here
elif menu == "IoT Device Monitoring":
    iot_monitoring.show()  # Ensure no st.sidebar logic here
elif menu == "Network Security":
    network_security.show()  # Ensure no st.sidebar logic here
elif menu == "Threat Detection and Response":
    threat_detection.show()  # Ensure no st.sidebar logic here
elif menu == "Pipeline Monitoring":
    pipeline_monitoring.show()  # Ensure no st.sidebar logic here
elif menu == "Cloud Integration & Reports":
    cloud_reports.show()  # Ensure no st.sidebar logic here
