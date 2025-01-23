import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# OpenWeatherMap API Key
API_KEY = 'your_api_key'  # Replace with your actual OpenWeatherMap API key

# Function to fetch weather data from the OpenWeatherMap API
def fetch_weather_data(city, days=7):
    # Coordinates for the city (use any reliable method to get coordinates of the city)
    city_coords = {
        'Dubai': (25.276987, 55.296249),
        'London': (51.5074, -0.1278),
        'New York': (40.7128, -74.0060)
    }

    lat, lon = city_coords.get(city, (25.276987, 55.296249))  # Default to Dubai if city not found
    
    # OpenWeatherMap OneCall API endpoint
    url = f'https://api.openweathermap.org/data/2.5/onecall'
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': 'current,minutely,alerts',  # We are only interested in hourly data for the next days
        'units': 'metric',  # Metric system (Celsius, m/s, etc.)
        'appid': API_KEY
    }
    
    # Fetch weather data
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Parse weather data into a pandas DataFrame
def parse_weather_data(weather_data, days=7):
    hourly_data = weather_data['hourly']
    
    # Collect data for the next 'days' worth of hourly data
    timestamps, temperatures, humidities, rainfalls = [], [], [], []
    
    for entry in hourly_data[:days * 24]:  # 24 hours per day
        timestamps.append(datetime.fromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S'))
        temperatures.append(entry['temp'])
        humidities.append(entry['humidity'])
        rainfalls.append(entry.get('rain', {}).get('1h', 0))  # Rain in last hour
    
    # Creating a DataFrame
    weather_df = pd.DataFrame({
        'Timestamp': pd.to_datetime(timestamps),
        'Temperature (°C)': temperatures,
        'Humidity (%)': humidities,
        'Rainfall (mm)': rainfalls
    })
    
    return weather_df

# Function to plot weather data with better UI
def plot_weather_data(weather_df, city):
    # Plotting multiple graphs in subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

    # Temperature plot
    axs[0].plot(weather_df['Timestamp'], weather_df['Temperature (°C)'], color='tab:red')
    axs[0].set_title(f'Temperature in {city} Over Time')
    axs[0].set_ylabel('Temperature (°C)', color='tab:red')
    axs[0].tick_params(axis='y', labelcolor='tab:red')
    axs[0].grid(True)

    # Humidity plot
    axs[1].plot(weather_df['Timestamp'], weather_df['Humidity (%)'], color='tab:blue')
    axs[1].set_title(f'Humidity in {city} Over Time')
    axs[1].set_ylabel('Humidity (%)', color='tab:blue')
    axs[1].tick_params(axis='y', labelcolor='tab:blue')
    axs[1].grid(True)

    # Rainfall plot
    axs[2].bar(weather_df['Timestamp'], weather_df['Rainfall (mm)'], color='tab:green', alpha=0.6)
    axs[2].set_title(f'Rainfall in {city} Over Time')
    axs[2].set_ylabel('Rainfall (mm)', color='tab:green')
    axs[2].tick_params(axis='y', labelcolor='tab:green')
    axs[2].grid(True)

    # Format the x-axis to display readable date/time
    axs[2].xaxis.set_major_locator(mdates.HourLocator(interval=6))
    axs[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.xticks(rotation=45)

    # Display the plot
    plt.tight_layout()
    plt.show()

# Main function to run the program
def main():
    print("Welcome to the Weather Prediction Visualizer!")
    
    # User inputs
    city = input("Enter city (e.g., Dubai, London, New York): ").capitalize()
    days = int(input("Enter number of days of forecast data to visualize (1-7): "))
    
    # Fetch data
    weather_data = fetch_weather_data(city, days)
    
    if weather_data:
        # Parse and visualize data
        weather_df = parse_weather_data(weather_data, days)
        plot_weather_data(weather_df, city)
    else:
        print("Failed to fetch weather data. Please try again later.")

if __name__ == "__main__":
    main()
