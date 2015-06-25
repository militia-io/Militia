import urllib2
import Scrapy

class Google_Image:

	def __init__(self, imageLink):
		#try: 
		url ='https://www.google.com/imghp?sbi=1' % (imageLink)
		response = urllib2.urlopen(url)
		#TO DO: Scrapy for image links
		#except Exception:
			#return None
		return links
