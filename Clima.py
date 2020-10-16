import requests
from pprint import pprint #so para imprimir o jason de forma mais legível

#Coordenadas desejadas
lat = input("Digite a latitude desejada: ")
lon = input("Digite a longitude desejada: ")
linguagem = 'pt'

#api
url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&lang={}&appid=0700d5b772b06c3fc81ae8c2c0773c9c'.format(lat,lon, linguagem)
res = requests.get(url)
print(res) #testando se as coordenadas para ver se retornam algum erro

#dados que API retorna
data = res.json()
#pprint(data)

#Variável que vai guardar resultado da string
clima = data['weather'][0]['description']
print(clima)