# importing the required Modules
import requests
import pyttsx3
import json

print("WHEATHER API".center(100))
# Audio 1
Robo=pyttsx3.init()
Robo.setProperty('rate',125)
Robo.say("Hi Sir my name is WheatherAI and I can give you a real time heather of city,state or country")
Robo.runAndWait()

# # #
print("Hi Sir my name is WheatherAI and I can give you a real time Wheather of city,state or country")
# # #

while True:

# Using the request Module for getting the wheatherAPI url
 city=input("Enter your City: ")
 url=f"https://api.weatherapi.com/v1/current.json?key=a8f71a17e1eb4558bf7114547232205&q={city}"
 wheather=requests.get(url)
 a=json.loads(wheather.text)

# Audio 2
 Robo.say(f"you have typed {city} ")
 Robo.runAndWait()

# it tells the details of the city
 print("Name of the City is",a["location"]["name"])
 print("Name of the Region is",a["location"]["region"])
 print("Name of the Country is",a["location"]["country"])
 print("Date and Time is",a["location"]["localtime"])

# it tells the wheather details of the city
 print("Temperture in Celsius Unit is" ,a["current"]["temp_c"])
 print("Temperture in Fahrenheit Unit is",a["current"]["temp_f"])
 print("Humidity is",a["current"]["humidity"])

# using pyttsx3 Module to allow Text to Speech


