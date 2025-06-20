import streamlit as st
import plotly.express as px
import backend

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


data = backend.get_data(place, days, option)

# figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (°C)'})

# st.plotly_chart(figure, use_container_width=True)