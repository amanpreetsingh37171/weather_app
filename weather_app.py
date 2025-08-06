import streamlit as st
import requests
from datetime import datetime

API_KEY = st.secreets["API_KEY"]



cities_name = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai",
    "Kolkata", "Surat", "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur",
    "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad",
    "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik",
    "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivali", "Vasai-Virar",
    "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar",
    "Navi Mumbai", "Allahabad", "Ranchi", "Howrah", "Coimbatore",
    "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur", "Madurai", "Raipur",
    "Kota", "Guwahati", "Chandigarh", "Solapur", "Hubballi-Dharwad",
    "Bareilly", "Moradabad", "Mysore", "Gurgaon", "Aligarh",
    "Jalandhar", "Tiruchirappalli", "Bhubaneswar", "Salem",
    "Mira-Bhayandar", "Thiruvananthapuram", "Bhiwandi", "Saharanpur",
    "Gorakhpur", "Guntur", "Bikaner", "Amravati", "Noida", "Jamshdpur",
    "Bhilai", "Warangal", "Mangalore", "Cuttack", "Firozabad", "Kochi",
    "Bhavnagar", "Dehradun", "Durgapur", "Asansol", "Nanded", "Kolhapur",
    "Ajmer", "Gulbarga", "Jamnagar", "Ujjain", "Loni", "Siliguri",
    "Jhansi", "Ulhasnagar", "Nellore", "Jammu", "Sangli", "Belgaum","Mohali", "Chandigarh"
]

st.set_page_config(page_title="Weather App", page_icon="🌤", layout="centered")

st.markdown("""
<style>
.main-title {
    background: linear-gradient(135deg, #56CCF2, #2F80ED);
    color: white;
    text-align: center;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    font-size: 28px;
}
.weather-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    text-align: center;
}
.metric {
    font-size: 18px;
    margin: 8px 0;
}
.footer {
    text-align: center;
    font-size: 13px;
    color: gray;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌤 My Beautiful Weather App</div>', unsafe_allow_html=True)

city = st.selectbox("🎯 Choose Your City", cities_name)

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    return requests.get(url).json()

if city:
    data = get_weather(city)

    if data.get("cod") == 200:
        weather = data["weather"][0]
        main = data["main"]
        wind = data["wind"]
        sys = data["sys"]
        visibility = data.get('visibility', 'N/A')
        clouds = data.get('clouds', {}).get('all', 'N/A')
        pressure = main.get('pressure', 'N/A')
        sea_level = main.get('sea_level', 'N/A')
        ground_level = main.get('grnd_level', 'N/A')
        
        sunrise = datetime.fromtimestamp(sys['sunrise']).strftime("%H:%M:%S")
        sunset = datetime.fromtimestamp(sys['sunset']).strftime("%H:%M:%S")

        st.markdown(f'<div class="weather-card">', unsafe_allow_html=True)
        st.markdown(f"<h2>{city}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p>{weather['description'].title()}</p>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"<p class='metric'>🌡 Temperature: <b>{main['temp']-273.15}°C</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>🌡 Feels like: <b>{main['feels_like']-273.15}°C</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>💧 Humidity: <b>{main['humidity']}%</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>💨 Wind Speed: <b>{wind['speed']} m/s</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>🧭 Wind Degree: <b>{wind['deg']}°</b></p>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<p class='metric'> pressão: <b>{pressure} hPa</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>🌊 Sea level: <b>{sea_level} hPa</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>⛰ Ground Level: <b>{ground_level} hPa</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>🌅 Sunrise: <b>{sunrise}</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>🌇 Sunset: <b>{sunset}</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>🌫 Visibility: <b>{visibility} m</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='metric'>☁️ Cloudiness: <b>{clouds}%</b></p>", unsafe_allow_html=True)
