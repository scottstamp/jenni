#!/usr/bin/env python
"""
stocks.py - jenni Stocks Ticker Module
Copyright 2015, Scott Stamp <scott@hypermine.com>
Licensed under IDGAF

More info:
 * jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import json
import urllib
import web

def stocks(jenni, input):
	txt = input.group(2)
	if not txt:
		return jenni.say('Please provide a stock symbol.')

	url = 'http://dev.markitondemand.com/Api/v2/Quote/json?symbol=%s'

	url = url % input.group(2).upper()

	## Basic error checking
	try:
		## Return an error if the page cannot load
		page = web.get(url)
	except:
		return jenni.say('Could not access the stock ticker service')

	## load URL and fetch JSON
	try:
		data = json.loads(page)
	except:
		return jenni.say('The server did not return anything that was readable as JSON.')

	if 'Status' not in data or 'SUCCESS' not in data['Status']:
		return jenni.say('The server did not return any usable data, please check your stock symbol.')

	name			= data['Name']
	symbol			= data['Symbol']
	last_price		= data['LastPrice']
	change			= data['Change']
	change_percent		= data['ChangePercent']
	timestamp		= data['Timestamp']
	ms_date			= data['MSDate']
	market_cap		= data['MarketCap']
	volume			= data['Volume']
	change_ytd		= data['ChangeYTD']
	change_percent_ytd	= data['ChangePercentYTD']
	high			= data['High']
	low			= data['Low']
	open			= data['Open']

	## Format decimals to the second-most significant place
	form = u'%.2f'

	last_price		= form % last_price
	change			= form % change
	change_percent		= form % change_percent
	change_ytd		= form % change_ytd
	change_percent_ytd	= form % change_percent_ytd
	high			= form % high
	low			= form % low
	open			= form % open

	## {Name} - {Symbol} - {LastPrice} - {Change} - {ChangePercent} - {Timestamp}
	resp = '{0} ({1}) | Last Price: {2} | Change: {3} ({4}%) | {5}'
	jenni.say(resp.format(name, symbol, last_price, change, change_percent, timestamp))
stocks.commands = ['stocks', 'stock', 'ticker']

if __name__ == '__main__':
	print __doc__.strip()
