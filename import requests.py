import requests
from tkinter import *

# OpenWeatherMap API key (replace with your own key)
API_KEY = 'df71abbdc42517b11de330c7629c4a74'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == '404':
        return None  # City not found
    else:
        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return f'{city_name}, {country}\nTemperature: {temperature}°C\nWeather: {weather_description}'

def search():
    city = city_entry.get()
    weather_info = get_weather(city)

    if weather_info:
        result_label.config(text=weather_info)
    else:
        result_label.config(text='City not found. Please try again.')

# GUI setup
app = Tk()
app.title('Weather App')

# Widgets
city_label = Label(app, text='Enter City:')
city_entry = Entry(app)
search_button = Button(app, text='Search Weather', command=search)
result_label = Label(app, text='Weather Information Will Appear Here', wraplength=300, justify='left')

# Layout
city_label.grid(row=0, column=0, padx=5, pady=5)
city_entry.grid(row=0, column=1, padx=5, pady=5)
search_button.grid(row=0, column=2, padx=5, pady=5)
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Run the application
app.mainloop()