import requests
from api_key import *
from twilio.rest import Client 


OWM = 'https://api.openweathermap.org/data/2.5/onecall'

weather_params = {
    "lat" : 43.615849,
    "lon" : 13.518740,
    'appid' : api,
    "exclude" : "current,minute,daily"
}





request = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=weather_params)
request.raise_for_status()
data = request.json()

hourly_weather = []


client = Client(account_sid,auth_token)
will_rain = False

for hour in range(0,12):
    weather = data['hourly'][hour]['weather'][0]['id']
    hourly_weather.append(weather)
    if weather < 700 : 
        will_rain = True

if will_rain:
    message = client.messages.create(  
                              messaging_service_sid='MG19f49ef4624c8b66ec8c16d7fddd8e54', 
                              body='It\'s going to rain!',      
                              to='+359879151441' 
                          ) 




 

