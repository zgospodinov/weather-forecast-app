import streamlit as st
import plotly.express as px


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


def get_data(days):
    dates = ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05"]
    temperatures = [20, 22, 19, 21, 23]

    return (dates, temperatures)

d,t = get_data(days)

figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (°C)'})

st.plotly_chart(figure, use_container_width=True)