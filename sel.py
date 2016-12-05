from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import re

"""
Selenium downloads the page source code. 
"""
def getPageSrc(url):
	driver = webdriver.Firefox()
	driver.get(url)
	page_src = driver.page_source.encode('utf-8')
	file = open("Output.txt", "w")
	file.write(page_src)
	file.close()
	driver.close()

"""
Returns true if source code contains the phrase "see inside"
"""
def containsBusinessView():
	contains = False

	with open("Output.txt", "r") as file:
		for row in file:
			if re.search('see inside', row, re.I):
				contains = True
	return contains


if __name__ == "__main__":
	getPageSrc(url)
	containsBusinessView()