from functions import *

########################### MAIN EXECUTION #########################################

stopwords = open("../resources/stopwords.txt").read().splitlines()
directory = "../data/solutec.fr/"
filepath = "../data/solutec.fr/de-l-ambition.txt"


list = fileToList(filepath)
print(list)

toRemove = returnStopwords(list, stopwords)
print(toRemove)
listToFile(toRemove, changeExt(filepath, ".stopwords"))

list = cleanList(list, toRemove)
listToFile(list, changeExt(filepath, ".nostopwords"))


browser = open_browser()

toRemove = returnVerbs(list, browser)
print(toRemove)
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