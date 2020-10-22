import requests

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
        pass

    def get_date(self, latitude, longitude):
        pass
    
    def get_time_from_timezone(self, latitude, longitude):
        pass

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
