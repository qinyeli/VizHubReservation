#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def main():

	print("Running Qinye's VizHub reserving script...")

	# r = requests.get('https://weblogin.umich.edu/')
	# #print(r.status_code, r.text)
	
	# soup = BeautifulSoup(r.text, 'html.parser')
	# print(soup.title)
	# print(soup.find_all('form'))
	
	s = requests.Session()
	form = {
		'ref': '',
		'service': '',
		'required': '',
		'login': 'login',
		'password': 'password'
	}
	r = s.post("https://weblogin.umich.edu/cosign-bin/cosign.cgi", data=form)
	# r = requests.get('http://apps.engin.umich.edu/collab-reserve/')
	print(r.status_code)
	print(r.text)

	# s.cookies

	# connection = http.client.HTTPConnection('apps.engin.umich.edu')
	# connection.request('GET', '/collab-reserve/')
	# response = connection.getresponse()
	# content = response.read().decode('utf-8')
	# print(content)

	# # Log in needed
	# if response.status == 302:
	# 	print (response.reason)
	# 	print("lalal")

if __name__ == '__main__':
	main()