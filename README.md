# Python-Based Weather Prediction Visualizer

## Overview

The **Weather Prediction Visualizer** is a Python-based application that allows users to visualize weather data for different cities over a custom time range. Using OpenWeatherMap's API, this tool fetches weather information, including temperature, humidity, and rainfall, and displays them in an interactive, easy-to-read graph.

The application helps users track weather patterns and understand trends across multiple days through advanced visualizations in the form of line charts and bar plots.

## Features

- **City Selection:** Users can input a city of their choice (e.g., Dubai, London, New York) to visualize weather data.
- **Custom Time Range:** Users can select the number of days (1 to 7) for which they wish to retrieve weather data.
- **Interactive Visualizations:** The app generates multiple graphs, including:
  - Temperature (°C)
  - Humidity (%)
  - Rainfall (mm)
- **Advanced Plotting:** The app uses `matplotlib` to display these data points clearly, with improved graph aesthetics, grid lines, and customizable x-axis time formatting.
- **Error Handling:** The app gracefully handles errors like missing or incorrect city names and API failures.
  
## Technologies Used

- **Python 3.x**
- **Libraries:**
  - `requests` – For making HTTP requests to fetch weather data from the OpenWeatherMap API.
  - `pandas` – For managing and organizing the fetched weather data.
  - `matplotlib` – For plotting data in the form of graphs and charts.
  - `datetime` – For handling time-related operations in the fetched data.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/youssof20/PythonBasedWeatherPrediction.git
   cd PythonBasedWeatherPrediction
