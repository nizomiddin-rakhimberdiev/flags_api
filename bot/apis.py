import requests

peoples = requests.get('https://randomuser.me/api/?results=9').json()
print(peoples)