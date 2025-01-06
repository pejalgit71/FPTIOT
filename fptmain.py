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
    st.title("IoT and EoT Security Framework Simulation")

    html_content = """
    <!DOCTYPE html>
    <html>
    <title>W3.CSS</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Tangerine">
    <style>
    .w3-tangerine {
      font-family: "Tangerine", serif;
    }
    </style>
    <body>
    
    <div class="w3-container w3-tangerine">
      // <p class="w3-xxlarge">Making the Web Beautiful!</p>
      <p class="w3-xxxlarge">Making the Web Beautiful!</p>
      // <p class="w3-jumbo">Making the Web Beautiful!</p>
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
