import urllib2
import json

class Find_Gender:

	def __init__(self, name):

		result = urllib2.urlopen('https://api.genderize.io/?name='+ name)
		self.data = json.load(result)
		try:
			self.gender = self.data["gender"]
			self.prob = self.data["probability"]
			self.count = self.data["count"]
		except Exception:
			self.gender = 'None'
			self.prob = 0.0
			self.count = 0.0			
	def get_Gender(self):
		return self.gender

if __name__ == '__main__':
	x = Find_Gender('brian')
	print x.get_Gender()
