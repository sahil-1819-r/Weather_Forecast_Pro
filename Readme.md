# 🌦 Weather Forecast Pro

A modern and responsive weather dashboard built using **Python, Flask, HTML, CSS, and JavaScript**. The application allows users to search weather information for any city, detect their current location, view a 5-day forecast, and explore live weather conditions of major Indian cities.

---

## 🚀 Features

- 🔍 Search weather by city name
- 📍 Get weather using your current location
- 🌡 Current weather information
- 📅 5-Day weather forecast
- 💧 Weather highlights
  - Humidity
  - Wind Speed
  - Feels Like Temperature
  - Visibility
  - Pressure
  - UV Index
- 🏙 Live weather for major Indian cities
- 📱 Fully responsive dashboard
- ⚡ Clean and modern UI

---

## 🛠 Tech Stack

### Backend

- Python
- Flask

### Frontend

- HTML5
- CSS3
- JavaScript

### API

- WeatherAPI

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```
Weather-Forecast-Pro/
│
├── app.py
├── .env
├── requirements.txt
├── .gitignore
│
├── services/
│   └── weather_service.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── templates/
    └── index.html
```

---

## ⚙ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sahil-1819-r/Weather-Forecast-Pro.git
```

### 2️⃣ Move into the project folder

```bash
cd Weather-Forecast-Pro
```

### 3️⃣ Create a virtual environment

Windows

```bash
python -m venv venv
```

Linux / macOS

```bash
python3 -m venv venv
```

---

### 4️⃣ Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### 5️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 6️⃣ Create a `.env` file

```env
API_KEY=YOUR_WEATHERAPI_KEY
```

---

### 7️⃣ Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🌐 API Used

**WeatherAPI**

Used for:

- Current Weather
- Current Location Weather
- 5-Day Forecast
- Weather Icons
- Weather Highlights

---

## 📚 What I Learned

Through this project, I learned:

- Flask Routing
- REST API Integration
- JSON Handling
- Environment Variables
- Fetch API
- Browser Geolocation API
- Jinja2 Templates
- Responsive Web Design
- DOM Manipulation
- Error Handling
- Git & GitHub Workflow

---

## 🚧 Future Improvements

- ⭐ Favorite Cities
- 🕒 Recent Searches
- 🌙 Dark / Light Mode
- 🌅 Sunrise & Sunset
- 🌫 Air Quality Index (AQI)
- ⏰ Hourly Forecast
- 📍 Exact Location using Reverse Geocoding
- 🌡 Temperature Unit Toggle (°C / °F)
---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.