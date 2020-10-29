import requests
import datetime
import pytz

class Extrapolation():
    """
    This class has the purpose of extrapolating data
    using API or any form of preprocessing so we can
    have more that to feed the neural network with
    """

    def __init__(self):
        pass

    def get_climate(self, latitude, longitude):
        # increase coordinate precision
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        location = data['loc'].split(',')
        language = 'pt'

        # connect to climate api
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&lang={}&appid=0700d5b772b06c3fc81ae8c2c0773c9c'.format(latitude, longitude, language)
        res = requests.get(url)

        # api data
        data = res.json()
        print(data)
        climate = data['weather'][0]['description']
        
        print('Climate from API is:', climate)

        return climate

    def get_day_of_week(self, latitude, longitude):
        unix_time = data['dt'] #stores unixtime given from API
        timestamp = datetime.datetime.utcfromtimestamp(unix_time) 
        
        day_of_week_index = timestamp.weekday() #return index, with 0 being Monday...

        #days in language that match with the dataset
        all_days = [
            "segunda-feira",
            "terça-feira",
            "quarta-feira",
            "quinta-feira",
            "sexta-feira",
            "sábado",
            "domingo"
        ]

        day_of_week = all_days[day_of_week_index]

        return day_of_week

    def get_date(self, latitude, longitude):
        unix_time = data['dt'] #stores unixtime given from API
        timestamp = datetime.datetime.utcfromtimestamp(unix_time) 
        date = timestamp.strftime('%d/%m/%Y')

        return date
    
    def get_time_from_timezone(self, latitude, longitude):
        unix_time_seconds = data['dt'] #stores unixtime given from API
        offsets_seconds = data['timezone'] #stores offset valor given from API

        time = unix_time_seconds + offsets_seconds #stores time with current timezone in UnixTime
        timestamp = datetime.datetime.utcfromtimestamp(time) #readble date
        hour = timestamp.strftime('%X')

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
