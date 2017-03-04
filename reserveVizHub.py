#!/usr/bin/env python3

import requests
import json
import getpass
import time


uuid = {
	1: 'svdkdsflk', # 10
	2: 'lkklmrkja', # 10
	3: 'ioqyDKJkbj', # 5
	4: 'ZhCbGLdzeC', # 5
	5: 'SriULTysLk', # 5
	6: 'FhQvgIbxoN', # 5
	7: 'XZCDatSVIN', # 10
	8: 'OvzyGxMaEp', # 10
	9: 'ALKEamOYNU', # 5
	10: 'COxXAIIzIT', # 5
	11: 'pafUhTdvvk', # 4
	12: 'NmauMgqblC', # 4
	13: 'EFuHkeNKrZ' # 4
}


# epochTime() returns the epoch time for begin time and end time
def epochTime(day_from_today, hour_begin, hour_end):
	# Ref: https://docs.python.org/3/library/time.html
	# Note: tm_isdst means daylight summer time

	# strftime converts time.struct_time into string
	year = time.strftime('%Y')
	day = int(time.strftime('%j')) # day of year
	day += int(day_from_today)

	# strptime converts string into time.struct_time
	time_begin = time.strptime(year + ' ' + str(day) + ' ' + hour_begin, '%Y %j %H')
	time_end = time.strptime(year + ' ' + str(day) + ' ' + hour_end, '%Y %j %H')

	print('\t' + time.strftime('%b. %d %a %H:%M ~ ', time_begin)
		+ time.strftime('%H:%M', time_end), end =':\t')

	# mktime converts (local) time.struct_time into epoch time
	epoch_begin = str(int(time.mktime(time_begin)))
	epoch_end = str(int(time.mktime(time_end)))

	return epoch_begin, epoch_end


def getTime():
	days = input('Input the days (0 for today, 1 for tomorrow and so on): ').split()
	assert (len(days) > 0)

	hours = input('Input the begin time and the end time (in 24-hour clock): ').split()
	assert(len(hours) == 2)

	return days, hours[0], hours[1]


def login():
	# Ref: http://docs.python-requests.org/
	login = input('User: ')
	if login == '':
		login = 'qinyeli'
	password = getpass.getpass()

	session = requests.Session()

	response = requests.get('http://apps.engin.umich.edu/collab-reserve/')
	cookies = dict(response.cookies)
	form = {
		'ref': 'https://apps.engin.umich.edu/collab-reserve/',
		'service': 'cosign-apps.engin',
		'required': '',
		'login': login,
		'password': password
	}
	response = session.post('https://weblogin.umich.edu/cosign-bin/cosign.cgi',\
		data=form, cookies=cookies)

	# print(response.status_code)
	# print(response.headers)
	# print(response.text)

	if response.text[0 : len('<!-- login_error.html -->')] == '<!-- login_error.html -->':
		print("Password or Account Name Incorrect. Is [caps lock] on?")
		return False, session
	else:
		return True, session


def main():
	ok = False
	while not ok:
		ok, session = login()

	vizhubID = int(input('Input the VizHub you want to reserve: '))
	assert(vizhubID != '')

	days, hour_begin, hour_end = getTime()

	# Start reserving!
	print('\nReserving VizHub ' + str(vizhubID) + ' for')
	for day_from_today in days:
		epoch_begin, epoch_end = epochTime(day_from_today, hour_begin, hour_end)

		response = session.get('https://apps.engin.umich.edu/collab-reserve/reservatron.php?action=reserve&uuid='
			+ uuid[vizhubID] + '&start=' + epoch_begin + '&end=' + epoch_end)

		id = json.loads(response.text)['id']
		status = 'Queued' # status will be Queued, Processing, Created, or Failed
		while status == 'Queued' or status == 'Processing':
			print(status, end = '... ', flush = True)
			time.sleep(2)
			response = session.get('https://apps.engin.umich.edu/collab-reserve/reservatron.php?action=status&id=' + str(id))
			status = json.loads(response.text)['message']
			
		print(status + '!', flush = True)


if __name__ == '__main__':
	print("Running Qinye's VizHub reserving script...")
	main()