import requests
import datetime
import pytz
from geopy.geocoders import Nominatim

class Extrapolation():
    """
    This class has the purpose of extrapolating data
    using API or any form of preprocessing so we can
    have more that to feed the neural network with
    """

    def __init__(self):
        pass

    def get_api(self, latitude, longitude):
        # increase coordinate precision
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        location = data['loc'].split(',')
        # connect to climate api
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=0700d5b772b06c3fc81ae8c2c0773c9c'.format(latitude, longitude)
        res = requests.get(url)
        # api data
        data = res.json()
        return data

    def get_climate(self, latitude, longitude):
           
        data = self.get_api(latitude, longitude) #data from API
        climate = data['weather'][0]['description']
        
        # print('Climate from API is:', climate)

        climate = data['weather'][0]['main']
        #Dict to match with current dataset
        climate_updated = {'Thunderstorm': 'Chuvoso',
                    'Drizzle': 'Chuvoso',
                    'Rain': 'Chuvoso',
                    'Snow': 'Neve',
                    'Atmosphere': 'Nevoeiro',
                    'Clear': 'Sol',
                    'Clouds': 'Nublado'}


        return climate_updated[climate] 

    def get_state(self, latitude, longitude):
        geolocator = Nominatim(user_agent="Carisk")
        coord = latitude, longitude
        location = geolocator.reverse(coord)
        address = location.raw['address']
        state = address.get('state', '')
    
        return state
    
    def get_city(self, latitude, longitude):
        data = self.get_api(latitude, longitude) #data from API
        city = data['name'] #storing city name
        return city

    def get_day_of_week(self, latitude, longitude):
        
        data = self.get_api(latitude, longitude) #data from API

        unix_time = data['dt'] #stores unixtime given from API
        timestamp = datetime.datetime.utcfromtimestamp(unix_time) 
        
        day_of_week_index = timestamp.weekday() #return index, with 0 being Monday...

        #days in language that match with the dataset
        all_days = [
            "SEG",
            "TER",
            "QUA",
            "QUI",
            "SEX",
            "SAB",
            "DOM"
        ]

        day_of_week = all_days[day_of_week_index]

        return day_of_week

    def get_date(self, latitude, longitude):        
        
        data = self.get_api(latitude, longitude) #data from API
        
        unix_time = data['dt'] #stores unixtime given from API
        timestamp = datetime.datetime.utcfromtimestamp(unix_time) 
        date = timestamp.strftime('%d/%m/%Y') #convert to readble Date, according to Dataset format

        return date
    
    def get_time_from_timezone(self, latitude, longitude):
        
        data = self.get_api(latitude, longitude) #data from API
        
        unix_time_seconds = data['dt'] #stores unixtime given from API
        offsets_seconds = data['timezone'] #stores offset valor given from API

        time = unix_time_seconds + offsets_seconds #stores time with current timezone in UnixTime
        timestamp = datetime.datetime.utcfromtimestamp(time) #readble date
        hour = timestamp.strftime('%H:%M')

        return hour

    def get_geolocation(self, location_name):
        googleurl = 'https://www.google.com.br/maps/search/'
        url = googleurl + '+'.join(location_name.split(' '))
        response = requests.get(url).text
        id = response.find('center=')
        response = response[id+7:]
        end = response.find('&')
        end = response[:end].split('%2C')
        return {
            'latitude': end[0],
            'longitude': end[1]
        }
