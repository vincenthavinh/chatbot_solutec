from tkinter import *
from functions import *


class Gui:
	
	def __init__(self, list1, list2):
		self.root = Tk()
		
		##################################
		self.listLeft = list1
		
		self.labelLeft = Label(self.root, text="list1")
		self.boxLeft = Listbox(self.root, height=25, selectmode=MULTIPLE)
		
		for i in self.listLeft:
			self.boxLeft.insert(END, i)
			
		self.labelLeft.grid(row=0, column=0)
		self.boxLeft.grid(row=1, column=0)
		
		##################################
		self.listRight = list2
		
		self.labelRight = Label(self.root, text="list2")
		self.boxRight = Listbox(self.root, height=25, selectmode=MULTIPLE)
		
		for i in self.listRight:
			self.boxRight.insert(END, i)
			
		self.labelRight.grid(row=0, column=2)
		self.boxRight.grid(row=1, column=2)
		
		##################################
		self.buttonsFrame = Frame(self.root)
		self.buttonsFrame.grid(row=1, column=1)
		
		self.buttonToRight = Button(self.buttonsFrame, text="=>", command=lambda x="=>":self.move(x))
		self.buttonToRight.grid(in_=self.buttonsFrame, row=0)
		
		self.buttonToLeft = Button(self.buttonsFrame, text="<=", command=lambda x="<=":self.move(x))
		self.buttonToLeft.grid(in_=self.buttonsFrame, row=1)
		
		##################################
	
		self.root.mainloop()
		
	def move(self, direction):
		if direction=="=>":
			print("=>")
			
			indexes = self.boxLeft.curselection()
			
			for i in reversed(indexes):
				print(self.listLeft[i])
				self.listRight.append(self.listLeft[i])
				self.list
				
		else:
			print("<=")
	
	def fct(self):
		indexes = self.boxLeft.curselection()
		
		selectedWords = []
		
		for i in indexes:
			selectedWords.append(self.listFrom[i])
			print(self.listFrom[i])
		
		self.root.destroy()
		
		stopwords = open(self.filepath).read().splitlines()
		stopwords += selectedWords
		stopwords = sorted(set(stopwords))
		
		#listToFile(stopwords, self.filepath)


list = fileToList("../../data/solutec.fr/de-l-ambition.txt")
stopwords = fileToList("../../resources/stopwords2.txt")
list = cleanList(list, stopwords)

Gui(list, stopwords)
