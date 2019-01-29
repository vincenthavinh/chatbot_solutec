from tkinter import *
from functions import *

class GuiSW:
	def __init__(self, listFrom, filepath):
		self.filepath = filepath
		self.listFrom = listFrom
		
		self.root = Tk()
		
		self.root.title("ListBox")
		
		self.label = Label(self.root, text="Selectionner les nouveaux stopwords à ajouter à stopwords.txt")
		self.label.pack()
		
		self.box = Listbox(self.root, height=25, selectmode=MULTIPLE)
		for i in self.listFrom:
			self.box.insert(END, i)
		self.box.pack()
		
		self.button = Button(self.root, text="Add to stopwords.txt", command=self.fct)
		self.button.pack()
		
		self.root.mainloop()
	
	def fct(self):
		indexes = self.box.curselection()
		
		selectedWords = []
		
		for i in indexes:
			selectedWords.append(self.listFrom[i])
			print(self.listFrom[i])
		
		self.root.destroy()
		
		stopwords = open(self.filepath).read().splitlines()
		stopwords += selectedWords
		stopwords = sorted(set(stopwords))
		
		listToFile(stopwords, self.filepath)


list = fileToList("../../data/solutec.fr/de-l-ambition.txt")
stopwords = fileToList("../../resources/stopwords2.txt")
list = cleanList(list, stopwords)

resultats = GuiSW(list , "../../resources/stopwords2.txt")

print(resultats)