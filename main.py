import requests
import datetime as dt

MY_LAT = 52.321008
MY_LNG = 20.949528
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise = sunrise.split('T')[1].split('+')[0]
sunset = sunset.split('T')[1].split('+')[0]


print(sunrise)
print(sunset)
time_now = dt.datetime.now()
