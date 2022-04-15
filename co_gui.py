from tkinter import *
from tkinter import ttk
from tkinter import filedialog 

root = Tk()


def actup():
	#filename = filedialog.askopenfilename(title = "open")
	#fob = open(filename, 'r')
	#print( fob.read())
	file = filedialog.askopenfilename(title = "open", filetypes = (("HTML files","*.html"),("All files","*.*")))
	fop= open(file,'r')
	data = fop.read()
	txtarea.insert(END, data)
	fop.close()
	
mybutton = ttk.Button(root, text="open file", command= actup)
mybutton.pack()

scrollbar= Scrollbar(root)
scrollbar.pack(side = RIGHT, fill= Y)


txtarea = Text(root, yscrollcommand = scrollbar.set)
txtarea.pack(side = RIGHT, fill= Y)

scrollbar.config(command= txtarea.yview)



root.mainloop()