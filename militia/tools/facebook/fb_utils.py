import json
import mechanize
import os

class Load_FB:
	#Facebook Mechanize session
	def __init__(self, confPath = '../config.json'):
		#confPath = os.path.dirname(os.path.dirname(__file__)) +'/config.json'
		with open(confPath, 'r') as file:
			config = json.load(file)
		self._email = config['email']
		self._pass = config['pass']
		# Set Location of data file
		self._input = config['input_file']
		self._output = config['output_file']
		self._api = config['gmaps-api-key']

 		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		cookies = mechanize.CookieJar()
		browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
		browser.open("https://www.facebook.com/login.php")
		browser.select_form(nr=0)

		# Enter Facebook information of user that's performing the search
		browser.form['email'] = self._email
		browser.form['pass'] = self._pass
		response = browser.submit()
		self.browser = browser
		self.response = response

	def read_Response(self):
		 return self.response.read()
		
if __name__ == '__main__': 
	#Debugging
	Load_FB('../../config.json')
	print Load_FB().read_Response()
