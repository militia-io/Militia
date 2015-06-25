#!/usr/bin/python

import json
import mechanize
from militia.tools.facebook import Load_FB
from militia.tools.genderize import Find_Gender
from bs4 import BeautifulSoup
import urllib2
import time


class Identity:

	def __init__(self, browser, filename):

		dataIn = open(filename, 'rU')
		self.browser = browser
		self.filename = filename
		phoneBook = []
		self.phoneBook = phoneBook
		self.failedCounter = 0
		for row in dataIn:
			cells = row.split(',')
			if 'phone' in row:
				self.phoneBook.append(cells[2].rstrip())		
		print '*** Reading CSV ****'

	def mechRead(self,url):

		browser = self.browser
		sitetest = browser.open(url)
		site = sitetest.read()
		return site

	def open_File(self, number):

		self.number = number
		url = 'https://www.facebook.com/search/str/%%20%s/keywords_top' % str(number)
		site = self.mechRead(url)
		return site

	def site_Test(self, number = 8102934256):
		username = self.open_File(number)
		try:
			nameSplit1 = username.split('<div class="_5d-5">')[1]
			nameSplit2 = nameSplit1.split('<div class="_glm">')[0]
			fullName = nameSplit2.split('</div>')[0]
			return 'Successfully connected, reverse search works'
		except Exception:
			return 'FAILED'

	def get_Name(self, number):

		username = self.open_File(number)
		try:
			nameSplit1 = username.split('<div class="_5d-5">')[1]
			nameSplit2 = nameSplit1.split('<div class="_glm">')[0]
			fullName = nameSplit2.split('</div>')[0]
			return fullName
		except Exception:
			return 'None'

	def get_URL(self, number):

		username = self.open_File(number)
		try:
			nameSplit1 = username.split('<div class="_gll"><a href="')[1]
			nameSplit2 = nameSplit1.split('<div class="_6a _6b _5d-4">')[0]
			fullURL = nameSplit2.split('?ref=br_rs">')[0]
			return fullURL
		except Exception:
			return 'None'

	def get_City(self, url):

		site = self.mechRead(url)
		try:
			nameSplit1 = site.split('hovercard="/ajax/hovercard/page.php?id=112222822122196">')[2]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
			nameSplit2 = nameSplit1.split('</a></div>')[0]
			soup = BeautifulSoup(nameSplit2)
			city = soup.getText()
			city = city.replace(',','')
			return city
		except Exception:
			return 'None'

	def get_Job(self, url):

		site = self.mechRead(url)
		try:
			nameSplit1 = site.split('<div class="_42ef"><div><div class="_50f3">')[1]
			nameSplit2 = nameSplit1.split('<span class="_50f8">')[0]
			soup = BeautifulSoup(nameSplit2)
			job = soup.getText()
			return job.encode("utf-8")
		except Exception:
			return 'None'

	def get_Intel(self, name, areaName):

		name = name.split()
		firstName = name[0]
		lastName = name[-1]
		# if there's a middle name, these are usually made up by facebook users
		if len(name) == 3:
			middleName = name[1]
		url = 'http://www.intelius.com/results.php?ReportType=1&formname=name&qf=%s&qmi=&qn=%s&qcs=%s&focusfirst=1' % (firstName, lastName, areaName)
		#TO DO: Parse the intelius link. For now this is not neccessary. 
		try:
			browser = self.browser
			sitetest = browser.open(url)
			site = sitetest.read()
		except Exception:
			print "%s : intellius error" % name 
		return str(url)

	def get_areaCode(self, number):

		try:
			url = 'http://www.allareacodes.com/' + str(number)
			site = self.mechRead(url)
			nameSplit1 = site.split('<td>Major City:</td>')[1]
			nameSplit2 = nameSplit1.split('</td>')[0]
			soup = BeautifulSoup(nameSplit2)
			area = soup.getText()
			return area.encode("utf-8")
		except Exception:
			return 'None'

	def get_GPS(self, areaCode, key):

		areaCode = areaCode.replace(' ', '')
		if areaCode != 'None':
			#try:
			url ='https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false&key=%s' % (str(areaCode), key)
			response = urllib2.urlopen(url)
			geoCode = json.load(response)
			#latitude = geoCode['results']['geometry']['bounds']['northeast']['lat'] 
			#longitude = geoCode['results']['geometry']['bounds']['northeast']['lng'] 
			#pprint(geoCode)
			lat = geoCode['results'][0]['geometry']['bounds']['northeast']['lat']
			lng = geoCode['results'][0]['geometry']['bounds']['northeast']['lng']
			return lat,lng


	def get_phoneBook(self):
		print "Phone numbers found: %s" % (len(self.phoneBook))
		return self.phoneBook

	def edit_Gmap(self, gpsArray):

		jsArray = []
		for gps in gpsArray:
			gps = 'new google.maps.LatLng'+ str(gps)
			jsArray.append(gps)
		jsArray = str(jsArray)
		jsArray = jsArray.replace("'", "")
		jsArray = jsArray.replace("[", "")
		jsArray = jsArray.replace("]", "")
		text_file = open("gps.txt", "w")
		text_file.write(jsArray)
		text_file.close()
	def write_text(self, data, filename='log.txt'):
		pass
	def write_data(self, data, filename):
	    with open(filename,'w') as f:
		    for x in data:
		        for y in x:
					y = str(y)
					f.write(y + ',')
		        f.write('\n')
	def genderCheck(self,name):
		name = name.split()
		x = Find_Gender(name[0])
		return str(x.gender)

if __name__ == '__main__':
	#Site Test
	search = Load_FB()
	# Set delay in seconds between requests so Facebook doesnt get overloaded
	delay = 1
	findUsers = Identity(search.browser,search._input)
	print findUsers.site_Test()
	identityList = []
	gpsArray = []
	for phone in findUsers.phoneBook:
		name = findUsers.get_Name(phone)
		if name != 'None':
			url = findUsers.get_URL(phone)
			city = findUsers.get_City(url)
			job = findUsers.get_Job(url)
			areaName = findUsers.get_areaCode(phone)
			intel = findUsers.get_Intel(name, areaName)
			location = findUsers.get_GPS(areaName, search._api)
			gender = findUsers.genderCheck(name)
			appendOut = [phone,name, gender,url,city,job,areaName,intel,location]
			if appendOut not in identityList:
				gpsArray.append(location)
				identityList.append(appendOut)
		else:
			findUsers.failedCounter +=1
			print 'Searching... %s'%findUsers.failedCounter
		time.sleep(delay)
		findUsers.write_data(identityList, search._output)
		findUsers.edit_Gmap(gpsArray)
	
	print str(identityList)
	lenList= len(identityList)
	print '%d profiles found.\n%d numbers unidentitified.\n%dnumbers tested total.' % (len(identityList),findUsers.failedCounter, len(identityList)+findUsers.failedCounter)
	percent = float(lenList)
	percent = (percent) / (percent + float(findUsers.failedCounter))
	print '%f percent return rate on mobile numbers' % float(percent * 100.0)
	#findUsers.write_data(identityList), search._output)
	#findUsers.edit_Gmap(gpsArray)
	
