# AI Weather Assistant

## Project Overview

AI Weather Assistant is a Streamlit-based weather application that allows users to ask weather-related questions for different cities.

The application understands questions such as:

* What is the weather in Chennai?
* What is the temperature in Mumbai?
* Is it raining in Bangalore?
* Tell me the weather in Delhi.
* What's the humidity in Coimbatore?

The application uses the Open-Meteo Geocoding API to find the location and the Open-Meteo Weather API to retrieve current weather information.

## Features

* Simple and interactive Streamlit chat interface
* Accepts natural-language weather questions
* Supports weather information for different cities
* Displays current temperature
* Shows feels-like temperature
* Displays humidity
* Shows wind speed
* Displays precipitation
* Shows weather conditions
* Uses free Open-Meteo APIs
* No OpenAI API key or paid API required

## Technologies Used

* Python
* Streamlit
* Requests
* Python-dotenv
* Open-Meteo API

## Project Structure

```text
AI-Weather-Assistant/
│
├── app.py
├── weather_functions.py
├── requirements.txt
└── README.md
```

## How It Works

```text
User enters a weather question
              ↓
        Streamlit Chat UI
              ↓
      Question Processing
              ↓
       Extract City Name
              ↓
      Open-Meteo Geocoding
              ↓
      Get Latitude & Longitude
              ↓
       Weather API Request
              ↓
       Current Weather Data
              ↓
       Display Result
```

## Weather Information

The application displays:

* City and Country
* Weather Condition
* Temperature
* Feels Like Temperature
* Humidity
* Wind Speed
* Precipitation



## Requirements

The project uses the following Python packages:

```text
streamlit
requests
python-dotenv
```


## Working Demo

### Example 1: Chennai Weather

**Question:**

```text
What is the weather in Chennai?
```
<img width="846" height="833" alt="Screenshot 2026-09-14 001649" src="https://github.com/user-attachments/assets/bac7ebed-0bb1-4fdf-984f-a8ae82ca9d36" />

### Example 2: Hydrabad Weather

**Question:**

```text
How windy is it in Hydrabad?
```

<img width="803" height="836" alt="Screenshot 2026-09-14 211125" src="https://github.com/user-attachments/assets/89785d5c-870c-4446-93c6-1d504304ef7f" />

The application retrieves the current weather information for Mumbai and displays the result in the chat interface.

## API Used

This project uses **Open-Meteo**, a free weather API that provides weather and geocoding data without requiring a paid API key.


## Conclusion

AI Weather Assistant provides a simple way to obtain current weather information by asking questions in natural language. The project combines Python, Streamlit, and free weather APIs to create an interactive and user-friendly weather application.
