import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

	
def fileToList(path):
	file = open(path)
	line = file.read()
	text = re.split('[\W\d]+', line)
	text = [x.lower() for x in text]
	return text

def cleanList(list, unwanted):
	words = [word for word in list if word not in unwanted]
	return words

def returnStopwords(list, stopwords):
	words = [word for word in list if word in stopwords]
	return words
	

def listToFile(list, path):
	with open(path, 'w') as f:
		for item in list:
			f.write("%s\n" % item)

def changeExt(path, newExt):
	return path.rsplit(".",1)[0] + newExt
	
def open_browser():
	print("starting web browser...")
	browser = webdriver.Firefox(executable_path="../resources/geckodriver")
	browser.set_window_size(700, 700)
	browser.set_window_position(0, 0)
	browser.get("http://bescherelle.com/conjugueur.php")
	browser.switch_to.frame("conjugueurweb")
	return browser

def returnVerbs(list, browser):
	wait = WebDriverWait(browser, 15)
	searchField = wait.until(ec.presence_of_element_located((By.ID, "frm_search:dim_searchField")))
	searchResults = wait.until(ec.presence_of_element_located((By.ID, "cnj_searchResults")))
	
	newList = []
	
	for word in list:
		if word == '': continue
		
		searchField.clear()
		searchField.send_keys(word)
		
		wait.until(ec.staleness_of(searchResults))
		searchResults = wait.until(ec.presence_of_element_located((By.ID, "cnj_searchResults")))
		
		try:
			exactResults = searchResults.find_element_by_id("cnj_searchResults:cnj_searchExactResults:tb")
		except NoSuchElementException:
			continue
		
		matchingVerbs = exactResults.find_elements_by_xpath("./tr")
		
		if len(matchingVerbs) == 0:
			continue
		else:
			print(word)
			newList.append(word)
	
	return newList
	

	
########################### MAIN EXECUTION #########################################

stopwords = open("../resources/stopwords.txt").read().splitlines()
directory = "../data/solutec.fr/"
filepath = "../data/solutec.fr/de-l-ambition.txt"


list = fileToList(filepath)

toRemove = returnStopwords(list, stopwords)
listToFile(toRemove, changeExt(filepath, ".stopwords"))

list = cleanList(list, toRemove)
listToFile(list, changeExt(filepath, ".nostopwords"))


browser = open_browser()

toRemove = returnVerbs(list, browser)
listToFile(toRemove, changeExt(filepath, ".verbs"))

list = cleanList(list, toRemove)
listToFile(list, changeExt(filepath, ".nostopwords_noverbs"))

browser.close()

'''
for file in os.listdir(directory):
	if file.endswith((".txt")):
		print(file)
		path = directory + file
		list = fileToList(path)
		
		toRemove = returnStopwords(list, stopwords)
		listToFile(toRemove, changeExt(path, ".stopwords"))
		
		list = cleanList(list, toRemove)
		listToFile(list, changeExt(path, ".nostopwords"))
'''


