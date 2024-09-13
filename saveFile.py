import tkinter as tk
from docx import Document
from tkinter.filedialog import asksaveasfile

fileFormat = ['txt', 'docx']

def save_button_clicked(option):
	print("Save Button clicked")
	if (option == 'txt'):
		f = asksaveasfile (mode = 'w', initialfile = 'Untitled.txt' , 
	 defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Document", "*.txt")])
		return (f)
	elif (option == 'docx'):
		f = asksaveasfile (mode = "w", initialfile = 'Untitled.docx' , 
	 defaultextension = ".docx", filetypes = [("All Files", "*.*"), ("Word Document", "*.docx")])
		return (f)

def saveToFile (textBox, formatComboBox):
	text = textBox.get('1.0', 'end')
	selection = formatComboBox.get()
	f = save_button_clicked (selection)
	
	if (selection not in fileFormat):
		tk.messagebox.showinfo("Warning", "Please choose a file format.")
		print ('File format not chosen.')
		return

	if (selection == 'docx'):
		document = Document()
		document.add_paragraph (text)
		document.save(f.name)
	else:
		# with open(f, 'w', encoding='utf-8') as f:
		tk.messagebox.showinfo("Warning", "If language is not English, it cannot save the file properly..")
		f.write(text)
		f.close()
	
	
