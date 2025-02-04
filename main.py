from tkinter import *
from tkinter import ttk
import requests
import emoji
from weather_data import weather_emoji, places_list
from dotenv import load_dotenv
import os

load_dotenv()

def get_data():
    city = city_name.get()
    API_KEY = os.getenv("API_KEY")
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
    data = response.json()
    
    if response.status_code == 200:
        # Accessing the data from json file using indexing and storing in variables
        weather_main = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = f"{data['main']['temp'] - 273:.2f}°C"
        pressure = data['main']['pressure']
        country = data['sys']['country']
        timezone_offset = data['timezone'] // 3600
        timezone = f"UTC {'+' if timezone_offset >= 0 else ''}{timezone_offset}"
        
        # Emojis added in another py file as dictionary

        # Displaying the data in the GUI using labels and config method & data stored in variables above
        weather_l_ans.config(text=f"{weather_main} {weather_emoji.get(weather_main, '')}")
        # weather_l_ans.config(text=data['weather'][0]['main']) ....This method can also be used to get weather
        w_description_ans.config(text=f"{description.capitalize()} 🌍")
        temp_ans.config(text=f"{temperature} 🌡")
        pres_ans.config(text=f"{pressure} hPa 🎈")
        country_ans.config(text=f"{country} 🏳️")
        timezone_ans.config(text=f"{timezone} ⏳")

    else:
        # If city is not found then it will show invalid city
        weather_l_ans.config(text="Invalid city")
        # If city is not found then it will show blank
        w_description_ans.config(text="")
        temp_ans.config(text="")
        pres_ans.config(text="")
        country_ans.config(text="")
        timezone_ans.config(text="")


win = Tk()
win.title("Weather App 🌤️")
win.config(bg="#87CEEB")
win.geometry("500x500")

# Places list added in another py file as list (for combobox)

name_heading = Label(win, text="Weather GUI", font=("Times New Roman", 20, "bold"), bg="#87CEEB")
name_heading.place(relx=0.5, y=50, anchor=CENTER)

city_name = StringVar()
combo = ttk.Combobox(win,values=places_list, font=("Times New Roman", 12), width=30, textvariable=city_name)
combo.place(relx=0.5, y=150, anchor=CENTER)
# This (combobox) is used for search bas and places are added in another py file as list

weather_l = Label(win, text="Weather: ", font=("Times New Roman", 15), bg="#87CEEB")
weather_l.place(relx=0.3, y=250, anchor=CENTER)
weather_l_ans = Label(win, text="", font=("Times New Roman", 15), bg="#87CEEB")
weather_l_ans.place(relx=0.65, y=250, anchor=CENTER)
# This (weather_l) is used for 1st weather output i mean heading

w_description = Label(win, text="Description: ", font=("Times New Roman", 15), bg="#87CEEB")
w_description.place(relx=0.3, y=290, anchor=CENTER)
w_description_ans = Label(win, text="", font=("Times New Roman", 15), bg="#87CEEB")
w_description_ans.place(relx=0.65, y=290, anchor=CENTER)
# This (w_description) is used for 2nd weather output {description}

temp = Label(win, text="Temperature: ", font=("Times New Roman", 15), bg="#87CEEB")
temp.place(relx=0.3, y=330, anchor=CENTER)
temp_ans = Label(win, text="", font=("Times New Roman", 15), bg="#87CEEB")
temp_ans.place(relx=0.65, y=330, anchor=CENTER)
# This (temp) is used for 3rd weather output {temperature}

pres = Label(win, text="Pressure: ", font=("Times New Roman", 15), bg="#87CEEB")
pres.place(relx=0.3, y=370, anchor=CENTER)
pres_ans = Label(win, text="", font=("Times New Roman", 15), bg="#87CEEB")
pres_ans.place(relx=0.65, y=370, anchor=CENTER)
# This (pres) is used for 4th weather output {pressure}

country = Label(win, text="Country: ", font=("Times New Roman", 15), bg="#87CEEB")
country.place(relx=0.3, y=410, anchor=CENTER)
country_ans = Label(win, text="", font=("Times New Roman", 15), bg="#87CEEB")
country_ans.place(relx=0.65, y=410, anchor=CENTER)
# This (country) is used for 5th weather output {country}

timezone = Label(win, text="Timezone: ", font=("Times New Roman", 15), bg="#87CEEB")
timezone.place(relx=0.3, y=450, anchor=CENTER)
timezone_ans = Label(win, text="", font=("Times New Roman", 15), bg="#87CEEB")
timezone_ans.place(relx=0.65, y=450, anchor=CENTER)
# This (timezone) is used for 6th weather output {timezone}

click_btn = Button(win, text="Get Weather", font=("Times New Roman", 12, "bold"), width=15, command=get_data)
click_btn.place(relx=0.5, y=200, anchor=CENTER)
# This (click_btn) is used for search button

win.mainloop()
