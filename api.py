# http://ws.audioscrobbler.com/2.0/?method=user.getTopTracks&user=USERNAME&api_key=API_KEY&format=json&limit=3
# https://lastfm-docs.github.io/api-docs/user/getTopTracks/

""" config.py
API_KEY = 'your_api_key'
USERNAME = 'your_username' """

import requests
import json

import config

API_KEY = config.API_KEY
USERNAME = config.USERNAME

response = requests.get(f'http://ws.audioscrobbler.com/2.0/?method=user.getTopTracks&user={USERNAME}&api_key={API_KEY}&format=json&limit=10')
data = json.loads(response.text)

for i in data['toptracks']['track']:
    print(i['name'] + ' | ' + i['artist']['name'] + ': ' + i['playcount'])