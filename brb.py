#!/usr/bin/python
# encoding=utf-8		// for korea

import sys
import time
import telegram
import os
import random

# for crawling
import requests
import json
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1024, 768))
display.start()
print "start monitor"


# base path for file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# for webdriver chromedriver 2.35 linux64

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(os.path.join(BASE_DIR, 'data/chromedriver'))
#driver = webdriver.Chrome('/root/BitRocketBot/data/chromedriver')

#driver = webdriver.Chrome()

# Create Bot


# remove tag


class Upbit:
	def __init__(self, term, inter, coin, count):
		# setting info and make url for parse
		self.term = term
		self.inter = inter
		self.coin = coin
		self.count = count
		self.url = "https://crix-api.upbit.com/v1/crix/candles/{term}/{inter}?code=CRIX.UPBIT.KRW-{coin}&count={count}".format( term = self.term, inter = self.inter, coin = self.coin, count = self.count)
		print self.url
		return

	def parse(self):
		# intro
		print self.coin

		# download char infomation and save at data
		self.data = requests.get(self.url)
		driver.get(self.url)

		driver.get(self.url)
		self.html = driver.page_source
		self.soup = BeautifulSoup(self.html, 'html.parser')
		self.data = self.soup.find('pre').get_text()
		#print self.data

		self.data = json.loads(self.data)

	
		# save data to array
		for item in self.data:
			self.code = item['code'].replace("CRIX.UPBIT.", "")
			self.openPrice = item['openingPrice']
			self.highPrice = item['highPrice']
			self.lowPrice = item['lowPrice']	
			self.tradePrice = item['tradePrice']
			self.kst = item['candleDateTimeKst']
			self.timestamp = item['timestamp']
			self.time = time.ctime(self.timestamp/1000)

			if item == self.data[-1]:
				self.nowPrice = self.tradePrice
				self.chart = []
				self.chart.append([self.code, self.openPrice, self.highPrice, self.lowPrice, self.tradePrice, self.time])
			else :
				self.prevPrice = self.tradePrice

		# save data in array and save in file
		print self.coin + str(self.nowPrice / self.prevPrice)
		if (self.nowPrice / self.prevPrice) > 1.007:
			bot.sendMessage(chat_id='@BitRocketCH', text="%s가 현재 떡상 중입니다. %s >> %s"%(self.coin, self.prevPrice, self.nowPrice))
		elif (self.nowPrice / self.prevPrice) < 0.993:
			bot.sendMessage(chat_id='@BitRocketCH', text="%s가 현재 떡락 중입니다. %s >> %s"%(self.coin, self.prevPrice, self.nowPrice))

		return

# main function
if __name__ == "__main__":

	# @BitRocketFS_bot 's token
	bot = telegram.Bot('520338177:AAEVT6CHrb-2r8y8x5lW-QqF0u9c_CUFdck')
	
	upbit = [
		Upbit("minutes", 1, "XRP", 2),
		Upbit("minutes", 1, "BTC", 2),
		Upbit("minutes", 1, "ADA", 2),
		Upbit("minutes", 1, "SNT", 2),
		Upbit("minutes", 1, "BTG", 2),
		Upbit("minutes", 1, "ETH", 2),
		Upbit("minutes", 1, "QTUM", 2),
		Upbit("minutes", 1, "BCC", 2),
		Upbit("minutes", 1, "NEO", 2),
		Upbit("minutes", 1, "ETC", 2),
	]
	print "Ready to start bot."
	while 1:
		upbit[int(random.random()*10%10)].parse()
		time.sleep(random.random()*10%6)
	print ('Listening ...')

	# Keep the program running.
	while 1:
		time.sleep(10)
