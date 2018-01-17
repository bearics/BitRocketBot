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

options = webdriver.ChromeOptions()
options.binary_location = '/opt/google/chrome/google-chrome'
service_log_path = "{}/chromedriver.log".format("./")
service_args = ['--verbose --no-sandbox']
driver = webdriver.Chrome('/root/BitRocketBot/data/chromedriver',
        chrome_options=options,
        service_args=service_args,
        service_log_path=service_log_path)
