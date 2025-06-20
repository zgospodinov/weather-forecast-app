import streamlit as st
import plotly.express as px
import backend
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

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

if place:
    filtered_data = backend.get_data(place, days)
    if filtered_data is None:
        st.error(f"Sorry, no weather data found for '{place}'. Please check the city name and try again.")
    else:
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (°C)'})
            st.plotly_chart(figure, use_container_width=True)

        if option == "Sky":
            imagesDic = {
                        "Clear": f"{SCRIPT_DIR}/images/clear.png",
                        "Clouds": f"{SCRIPT_DIR}/images/cloud.png",
                        "Rain": f"{SCRIPT_DIR}/images/rain.png",
                        "Snow": f"{SCRIPT_DIR}/images/snow.png"
                        }
            
            sky_condtitions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [imagesDic[condition] for condition in sky_condtitions]

            st.image(image_paths, width=100, caption=sky_condtitions)
