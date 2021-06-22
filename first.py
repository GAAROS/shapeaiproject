import requests

from datetime import datetime
api_key='c63eb07784e4ba385b91ef3ecea0f226'
location=input('enter your city name ')

compl_api_link="http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(compl_api_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']

print("weather stats for  ",location.upper())
print("current temperature : ",temp_city)
print("current weather description : ",weather_desc)
print("current humidity : ",hmdt,'%')
print("current wind speed : ",wind_spd,'kmph')

with open('file.txt','w+') as f:
    f.write("weather stats for  "+location.upper()+"\n")
    f.write("Current temperature : "+str(temp_city)+"\n")
    f.write("Current weather description : "+str(weather_desc)+"\n")
    f.write("Current weather Humidity: "+str(hmdt)+"\n")
    f.write("Current wind speed : "+str(wind_spd))