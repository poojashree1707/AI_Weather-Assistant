import streamlit as st
from weather_functions import get_weather


st.set_page_config(
    page_title="AI Weather Assistant",
    page_icon="🌤️",
    layout="centered"
)

st.title("AI Weather Assistant")
st.write("Weather application using Function Calling")


def weather_function_call(user_input):
    words = user_input.split()

    if "in" in words:
        index = words.index("in")

        if index + 1 < len(words):
            city = " ".join(words[index + 1:]).strip("?.!,")
            return get_weather(city)

    return {"error": "Please enter a city name."}


user_input = st.chat_input(
    "Example: What is the weather in Chennai?"
)


if user_input:

    st.chat_message("user").write(user_input)

    result = weather_function_call(user_input)

    if "error" in result:

        st.chat_message("assistant").write(
            result["error"]
        )

    else:

        weather_code = result["weather_code"]

        weather_description = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            95: "Thunderstorm"
        }

        description = weather_description.get(
            weather_code,
            "Unknown weather"
        )

        answer = f"""
### Weather in {result['city']}, {result['country']}

**Condition:** {description}

**Temperature:** {result['temperature']} °C

**Feels Like:** {result['feels_like']} °C

**Humidity:** {result['humidity']}%

**Wind Speed:** {result['wind_speed']} km/h

**Precipitation:** {result['precipitation']} mm
"""

        st.chat_message("assistant").markdown(answer)