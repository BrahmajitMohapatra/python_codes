import json
import requests
Player_BIOGRAPHY = {"weather":"Temperature is 27 degree Celcius  Humidity is 57 percent.",

"temperature":"Temperature is 27 degree Celcius.",

"humidity":"Humidity is 57 percent.",

"soil moisture":"soil moisture is 20 %"}

soil_m="https://api.thingspeak.com/channels/703460/field/field1/last.html"
temp_rt="https://api.thingspeak.com/channels/703460/field/field3/last.html"
humid="https://api.thingspeak.com/channels/703460/field/field4/last.html"

response_S = requests.get(soil_m)
response_T = requests.get(temp_rt)
response_H = requests.get(humid)

t=response_T.text
sm=response_S.text
h=response_H.text
t_diag= "Temperature is " + t + " Degree celcius."
sm_diag= "Soil moisture is " + sm + " percent. "
hm_diag = "  Humidity is "+ h + " percent "

Player_BIOGRAPHY["weather"]= t_diag + hm_diag
Player_BIOGRAPHY["temperature"]= t_diag
Player_BIOGRAPHY["humidity"]= hm_diag 
Player_BIOGRAPHY["soil moisture"]= sm_diag 



print(Player_BIOGRAPHY["weather"])
print(Player_BIOGRAPHY["temperature"])
print(Player_BIOGRAPHY["soil moisture"])
print(Player_BIOGRAPHY["humidity"])

