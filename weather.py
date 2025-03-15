import streamlit as st
import requests
import pandas as pd
import json
from dotenv import load_dotenv
import os

st.title("Ứng Dụng Kết Nối API")

# Ví dụ 1: Lấy thông tin thời tiết từ API
st.header("1. Thông Tin Thời Tiết")

city = st.text_input("Nhập tên thành phố (tiếng Anh):", "Hanoi")
load_dotenv()  # Load environment variables from .env file
api_key = os.getenv('WEATHER_APIKEY')  # Get API key from environment variable

if st.button("Xem Thời Tiết"):
    try:
        # Gửi request đến OpenWeatherMap API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        # Kiểm tra response
        if response.status_code == 200:
            data = response.json()
            
            # Hiển thị thông tin thời tiết
            st.subheader(f"Thời tiết tại {city}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Nhiệt độ", f"{data['main']['temp']}°C")
                st.metric("Độ ẩm", f"{data['main']['humidity']}%")
                
            with col2:
                st.metric("Gió", f"{data['wind']['speed']} m/s")
                st.metric("Mây", f"{data['clouds']['all']}%")
                
            st.write(f"Mô tả: {data['weather'][0]['description']}")
        else:
            st.error(f"Lỗi: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Đã xảy ra lỗi: {e}")