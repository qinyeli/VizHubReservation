#!/usr/bin/env python3

import requests
import json
import getpass
from bs4 import BeautifulSoup
from datetime import datetime

uuid = {
	1: 'svdkdsflk', # 10
	2: 'lkklmrkja' # 10
}

def getTime():
	datetime.strftime("%Y %m %d %H %M %S")
	now = datetime.now()

def main():
	print("Running Qinye's VizHub reserving script...")
	# login = input('User: ')
	# password = getpass.getpass()

	start, end = getTime()
	print('Reserving VizHub from ' + start + ' to ' + end)

	# session = requests.Session()

	# # Login
	# response = requests.get('http://apps.engin.umich.edu/collab-reserve/')
	# cookies = dict(response.cookies)
	# form = {
	# 	'ref': 'https://apps.engin.umich.edu/collab-reserve/',
	# 	'service': 'cosign-apps.engin',
	# 	'required': '',
	# 	'login': login,
	# 	'password': password
	# }
	# response = session.post('https://weblogin.umich.edu/cosign-bin/cosign.cgi',\
	# 	data=form, cookies=cookies)

	# response = session.get('https://apps.engin.umich.edu/collab-reserve/reservatron.php?action=reserve&uuid=' + uuid[1]
	# 	+ '&start=' + start + '&end=' + end)

	# # The response is going to be something like {'id': 12345}
	# id = json.loads(respone.text)['id']
	# response = session.get('https://apps.engin.umich.edu/collab-reserve/reservatron.php?action=status&id=' + id)
	
	# # The response is going to be
	# # either {"message":"Queued"} or {"message":"Created"}
	# print(json.loads(response.text)['message'])

if __name__ == '__main__':
	main()