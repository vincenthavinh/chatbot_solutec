import re
import os

def makeCleanFile(path):
	print(path)
	
	file = open(path)
	line = file.read()
	text = re.split('[\W\d]+', line)
	text = [x.lower() for x in text]
	print(text)
	
	words = [word for word in text if word not in stopwords]
	print(words)
	print(" ")
	
	with open(path+".clean", 'w') as f:
		for item in words:
			f.write("%s\n" % item)


stopwords = open("stopwords.txt").read().splitlines()
directory = "../data/solutec.fr/"
#print(stopwords)

#makeCleanFile("../data/solutec.fr/accelerateur-de-carriere.txt")


for file in os.listdir(directory):
	if file.endswith((".txt")):
		#print(directory + file)
		makeCleanFile(directory + file)
		


