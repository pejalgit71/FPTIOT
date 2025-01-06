import streamlit as st
from datetime import datetime
import pandas as pd
import random
import streamlit.components.v1 as components

def show():
    st.subheader("Physical Security")
    st.write("Simulating physical security measures such as surveillance and access control.")

    # Simulate Surveillance Camera
    st.write("### Surveillance Camera Feed")
    # st.image("https://via.placeholder.com/640x360", caption="Live Camera Feed Simulation")
    # st.image("https://elephants.hls.camzonecdn.com/CamzoneStreams/elephants/Playlist.m3u8", caption="Live Animal Camera Feed Simulation")
    st.title("Live Feed Example")
    st.write("Below is the live feed of Jackson Wyoming Town Square:")
    
    # Embed the iframe with autoplay enabled
    iframe_code = """
    <iframe width="675" height="379" src="https://www.youtube.com/embed/DoUOrTJbIu4?autoplay=1" 
    title="Jackson Wyoming Town Square Live Webcam - SeeJH.com" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    referrerpolicy="strict-origin-when-cross-origin" 
    allowfullscreen>
    </iframe>
    """

    # Render the iframe in Streamlit
    components.html(iframe_code, height=400)

    # Access Control Logs
    # st.write("### Access Control Logs")
    # access_data = {
    #     "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(5)],
    #     "User": [f"User_{i}" for i in range(1, 6)],
    #     "Access": [random.choice(["Granted", "Denied"]) for _ in range(5)]
    # }
    # st.table(pd.DataFrame(access_data))
    st.subheader("Physical Security")
    st.write("Access control logs and surveillance simulation.")

    # Access Logs
    access_logs = pd.read_csv('data/access_logs.csv')
    st.write("### Access Control Logs")
    st.table(access_logs)

    