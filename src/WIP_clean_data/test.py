from tkinter import *
from functions import *


def fileToList(path):
	file = open(path)
	line = file.read()
	text = re.split('[\W\d]+', line)
	text = [x.lower() for x in text]
	return text


class App:
	def __init__(self, list):
		self.root = Tk()
		self.list = list
		self.selectedWords = []
		self.iterator = 0
		self.label = Label(self.root, text=self.list[self.iterator])
		self.nextButton = Button(self.root, text="Ok", command=self.next)
		self.selectButton = Button(self.root, text="Select", command=self.select)
		self.label.pack()
		self.nextButton.pack()
		self.selectButton.pack()
		self.root.mainloop()
	
	def select(self):
		self.selectedWords.append(self.label.cget("text"))
		self.next()
	
	def next(self):
		self.iterator += 1
		if (self.iterator < len(self.list)):
			self.label.configure(text=self.list[self.iterator])
		else:
			self.root.destroy()


stopwords = fileToList("../../resources/stopwords.txt")
verbstokeep = fileToList("../../resources/verbsToKeep.txt")
words = fileToList("../../data/solutec.fr/la-valeur-ajoutee-solutec.nostopwords")
print(stopwords)
print(words)

# on enleve les stopwords deja connus
words = cleanList(words, stopwords)

# on trouve les stopwords non connus
app = App(words)
newStopwords = app.selectedWords
stopwords = list(set(stopwords + newStopwords)).sort()

'''
# on récupère les verbes reconnus sur Bescherelle.com
browser = open_browser()
verbs = returnVerbs(words, browser)
verbs = cleanList(verbs, verbstokeep)

# on retire de la liste de verbes les mots qui sont ambigüs
app = App(verbs)
newVerbstokeep

print(verbs)

app = App(words)
newStopwords = app.selectedWords
stopwords += newStopwords
print(list(set(stopwords)).sort())
print(stopwords)
'''