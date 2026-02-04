# Weather App CLI - Python

A simple command-line weather application built with Python that fetches real-time weather data from OpenWeather API.

## 📋 Features
- **Current Weather**: Get real-time weather conditions for any city
- **5-Day Forecast**: View weather predictions for the next 5 days
- **Multi-City Comparison**: Compare weather conditions across multiple cities
- **Natural Language Translation**: Weather descriptions translated to natural Indonesian terms
- **Search History**: Automatically saves your weather queries

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Internet connection
- OpenWeather API key (free)

### Installation
1. Clone or download this repository
2. Install required packages:
```bash
pip install requests
```

3. Get your free API key from [OpenWeather](https://home.openweathermap.org/users/sign_up)

4. Replace the API key in the code:
```python
api_key = "YOUR_ACTUAL_API_KEY_HERE"  # Line 6 in the code
```

## 📖 Usage
Run the application:
```bash
python weather_app.py
```

### Menu Options
1. **Check Current Weather** - Get real-time weather for a single city
2. **5-Day Forecast** - View weather predictions for the next 5 days
3. **Compare Multiple Cities** - See weather conditions for up to 6 cities at once
4. **Exit** - Close the application

### Example Usage
```
========================================
WEATHER APPLICATION PYTHON
========================================
1. Check City Weather (Current)
2. 5-Day Forecast
3. Compare Multiple Cities
4. Exit
========================================

Pilih menu (1-4): 1

[CHECK CURRENT WEATHER]
Enter city name: Jakarta

========================================
CURRENT WEATHER - JAKARTA
========================================
Condition   : Partly Cloudy
Temperature : 30.5°C
Feels Like  : 33.2°C
Humidity    : 75%
========================================
```

## 🔧 How It Works

### API Integration
The application uses OpenWeather's free API endpoints:
- Current weather: `api.openweathermap.org/data/2.5/weather`
- 5-day forecast: `api.openweathermap.org/data/2.5/forecast`

### Key Functions
- `get_weather_data()`: Fetches current weather data
- `get_5day_forecast()`: Retrieves 5-day weather forecast
- `translate_to_natural()`: Converts technical weather terms to natural Indonesian language
- `multi_city_weather()`: Compares weather across multiple cities

### Data Display
The application formats weather data with:
- Temperature in Celsius (°C)
- Humidity percentage
- "Feels like" temperature
- Translated weather conditions

## 📁 File Structure
```
weather_app.py          # Main application file
weather_history.txt     # Automatically created search history
README.md              # This documentation
```

## ⚠️ Important Notes

### For Educational Purposes Only
**This project is for learning purposes only.** It demonstrates:
- API integration with Python
- Error handling and user input validation
- String formatting and data presentation
- File I/O operations
- Modular programming with functions

### Rate Limits
The free OpenWeather API has limitations:
- 60 calls per minute
- 1,000,000 calls per month
- Weather data may be slightly delayed

### Accuracy
- Weather data accuracy depends on OpenWeather's sources
- Forecasts are predictions and may not be 100% accurate
- "Feels like" temperature considers humidity and wind

## 🛠️ Code Structure

### Main Components
1. **API Configuration** - API key and endpoint URLs
2. **Data Fetching Functions** - Request handling with error management
3. **Display Functions** - Formatted output for different weather views
4. **Translation Function** - Converts technical terms to natural language
5. **Menu System** - User-friendly command-line interface

### Error Handling
- Network connection errors
- Invalid city names
- API response errors
- User input validation

## 🔮 Future Enhancements
Potential improvements for this learning project:
- Add temperature unit conversion (Celsius/Fahrenheit)
- Implement location detection via IP
- Create graphical charts for temperature trends
- Add weather alerts and notifications
- Support for saving favorite cities

## 📚 Learning Outcomes
By studying this code, you'll learn about:
- Making HTTP requests with the `requests` library
- Parsing JSON responses from APIs
- String formatting and alignment in Python
- Building interactive CLI applications
- Error handling and user input validation
- File operations for data persistence

## 🤝 Contributing
This is a learning project. Feel free to:
- Fork and modify for your learning needs
- Experiment with different APIs or features
- Improve error handling or user interface
- Add documentation or comments

## 📄 License
This project is for educational purposes. Use it to learn Python programming concepts.

## ⚠️ Disclaimer
This application uses OpenWeather API. Please refer to their [terms of service](https://openweathermap.org/terms) for usage guidelines. The developer is not responsible for any misuse of the API or weather data inaccuracies.
