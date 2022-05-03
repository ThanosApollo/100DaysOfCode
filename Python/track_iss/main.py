
import requests
from datetime import datetime
import smtpd
import time

my_email = ''
my_password = ''


MY_LAT = 42.6978634 # Your latitude
MY_LONG = 23.3221789 # Your longitude


def is_issoverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = { 
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise :
        return True

while True : 
    time.sleep(60)
    if is_issoverhead() and is_night():
        connection = smtpd.SMTP("smt.gmail.com")
        connection.starttls()
        connection.login(user=my_email, passwd=my_password)
        connection.sendmail((my_email), my_email, 'look above!')


