import streamlit as st

st.title("Weather :green[_Forecast_] App for the next days", anchor=False)

place = st.text_input("" \
    "Enter a place to get the weather forecast",
    help="Enter a city name to get the weather forecast")

days = st.slider(
    "Select number of days", 
    min_value=1, 
    max_value=5, 
    value=1,
    help="Select the number of days for the weather forecast")

option = st.selectbox(
    "Select data to show",
      ["Temperature", "Sky"],
      help="Select the type of weather data to display")

st.subheader(f"{option} for {place} for the next {days} days")