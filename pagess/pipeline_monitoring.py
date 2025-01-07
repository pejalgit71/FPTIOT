import streamlit as st
import pandas as pd
import random
import requests

# ThingSpeak Configuration
channel_id = "2803064"
write_api_key = "52BPO25GBLU17N3V"
read_api_key = "JNGZJMEIKR8PY2AD"
read_url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}&results=10"

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


    # # Pipeline Data
    # pipeline_data = pd.read_csv('data/pipeline_data.csv')
    # st.write("### Pipeline Status")
    # st.table(pipeline_data)

    # Section to Read Data
    # Fetch Data
   
    response = requests.get(read_url)
    if response.status_code == 200:
        data = response.json()
        feeds = data.get("feeds", [])
        if feeds:
            st.write("Latest Data from ThingSpeak:")
            for feed in feeds:
                entry_id = feed.get("entry_id")
                field1 = feed.get("field1")  #Temperature
                field2 = feed.get("field2")  # Humidity
                field3 = feed.get("field3")  # Pipe Pressure
                st.write(f"Entry ID: {entry_id}, Temperature: {field1}, Humidity: {field2}, Pipe Pressure: {field3}")
        else:
            st.warning("No data available.")
    else:
        st.error("Failed to fetch data. Please check your API key and channel ID.")
    normal = 76.0
    pipelinevalue=field3
    if pipelinevalue > normal:
        pipeline_status = "Leak"
        st.error(f"Pipeline Alert: {pipeline_status} detected!")
    elif pipelinevalue < normal:
        pipeline_status = "Preasure Drop"
        st.error(f"Pipeline Alert: {pipeline_status} detected!")
    else:
        st.success("Pipeline operating normally.")
   
