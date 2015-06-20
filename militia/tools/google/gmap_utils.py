import json
import os

class Gmap:
	def __init__(self):
		with open('../config.json', 'r') as file:
			config = json.load(file)
		_api = config['gmaps-api-key']

	def get_GPS(self, city, key):
		city = city.replace(' ', '')
		#try:
		url ='https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false&key=%s' % (city, key)
		response = urllib2.urlopen(url)
		geoCode = json.load(response)
		#latitude = geoCode['results']['geometry']['bounds']['northeast']['lat'] 
		#longitude = geoCode['results']['geometry']['bounds']['northeast']['lng'] 
		#pprint(geoCode)
		lat = geoCode['results'][0]['geometry']['bounds']['northeast']['lat']
		lng = geoCode['results'][0]['geometry']['bounds']['northeast']['lng']
		return lat,lng
