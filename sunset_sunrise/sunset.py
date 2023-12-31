import requests
from datetime import datetime

my_lat = [Latitude]
my_lng = [Longitude]




parameters = {
    'lat': my_lat,
    'lng': my_lng,
    'formatted': 0,
}


response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)


