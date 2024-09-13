import customtkinter as ctk
import commonFunctions as cf
import translate
import saveFile as sF
import DocProcessing as doc_text 

#--------FOR DOCUMENT RELATED WORK---------------------------	
class DocumentFrame(ctk.CTkFrame):
	file_name = "" #available throughout the class
	ocr_result = ""
	def __init__(self, master):
		super().__init__(master)
		self.header= ctk.CTkLabel(self, text = "Document",font=('Times New Roman', 24, 'bold'))
		self.header.grid(row = 0, column = 1, padx = 10, pady= (10,0))
		#---Browse Button: for browsing file to upload---------------
		self.browse_button= ctk.CTkButton(self, text="Browse File", command= lambda: cf.browse_button_clicked  
		 (self))
		self.browse_button.grid(row = 1, column = 1, padx = 10, pady = (10,10))
		#----------------------------------------
		#adding CheckboxFrame for filtering choices
		self.checkbox_frame = CheckboxFrame (self)
		self.checkbox_frame.grid(row = 2, column = 1)
		#------------------------------------------
		#---Convert Button: for converting the image to text--------------- 
		self.convert_button= ctk.CTkButton(self, text="Convert", command= lambda: cf.convert_button_clicked (self, 1))
		self.convert_button.grid(row = 3, column = 1, padx = 10, pady = (10,0))
		#----------------------------------------
		#------adding ImageFrame for original as well as converted image-----
		self.original_image_frame = ImageFrame(self)
		self.original_image_frame.grid(row = 4, column = 0, padx = (10,10), pady =(10,0))
		self.converted_image_frame = ImageFrame(self)
		self.converted_image_frame.grid(row = 4, column = 2, padx = (10,10), pady =(10,0))
		#---------------------------------------------------------------------
		#-----adding Text Area to display the recognized text----------------
		self.text_area = ctk.CTkTextbox(master = self, height=500, width=400, padx =10, pady=10)
		self.text_area.grid(row = 4, column = 1, padx = (10,10), pady = (10, 0))
		#---------------------------------------------------------------------
		
		#InsideFrame ()
		self.translate_Frame= ctk.CTkFrame (self, width = 330)
		self.translate_Frame.grid_propagate (False)
		self.translate_Frame.columnconfigure (0, weight= 1)
		self.translate_Frame.grid (row = 5, column = 0, padx = 10, pady = 10, sticky = 'w')
		# --------------------------------------------------------------------------------
		self.voice_Frame = ctk.CTkFrame (self, width= 620)
		self.voice_Frame.grid_propagate (False)
		self.voice_Frame.columnconfigure (1, weight= 1)
		self.voice_Frame.grid (row = 5, column = 1, padx = 112, pady = 10, sticky = 'w')
		# --------------------------------------------------------------------------------
		self.fileSave_Frame = ctk.CTkFrame (self, width= 330)
		self.fileSave_Frame.grid_propagate (False)
		self.fileSave_Frame.columnconfigure (2, weight= 1)
		self.fileSave_Frame.grid (row = 5, column = 2, padx = 10, pady = 10, sticky = 'w')
		# --------------------------------------------------------------------------------
		self.listen_button = ctk.CTkButton(self.voice_Frame, text="Listen", command= cf.listen_button_clicked)
		self.listen_button.place (relx= 0.1, rely= 0.1)
		self.stop_button = ctk.CTkButton(self.voice_Frame, text="Stop", command= cf.stop_button_clicked)
		self.stop_button.place (relx= 0.55, rely= 0.1)
		self.pause_button = ctk.CTkButton(self.voice_Frame, text="Pause", command= cf.pause_button_clicked)
		self.pause_button.place (relx= 0.1, rely= 0.3)
		self.resume_button = ctk.CTkButton(self.voice_Frame, text="Resume", command= cf.resume_button_clicked)
		self.resume_button.place (relx= 0.55, rely= 0.3)
		
		#--------------------------------------------------------------
		# Create Dropdown menu for source language
		self.source_comboBox = ctk.CTkComboBox (master= self, values = doc_text.source_language, command = self.combobox_callback_source)
		self.source_comboBox.grid (row = 3, column = 0, padx = 10, pady = (10,0))
		self.source_comboBox.bind ("<KeyRelease>", self.check_source_language)
		# initial menu text
		self.source_comboBox.set ('English')
		self.source_language = 'English'
		self.sourceLabel = ctk.CTkLabel (self, text= 'Select Source Language')
		self.sourceLabel.grid (row = 2, column = 0)
		#--------------------------------------------------------------
		# Create Dropdown menu for translate language
		self.translate_comboBox = ctk.CTkComboBox ( master= self.translate_Frame, values = translate.lang_value_list, command = self.combobox_callback_translate)
		self.translate_comboBox.bind ("<KeyRelease>", self.check_translate_language)
		self.translate_comboBox.place (relx= 0.3, rely= 0.1)
		# initial menu text
		self.translate_comboBox.set ("Select Language")
		self.translate_language = None
		# Create button to translate
		self.translate_button = ctk.CTkButton (self.translate_Frame , text = "Translate" ,
		 command = lambda: cf.translate_button_clicked (self))
		self.translate_comboBox.place (relx= 0.3, rely= 0.1)
		self.translate_button.place (relx = 0.3, rely = 0.3)
		# --------------------------------------------------------------------------------------
		
		# save file
		self.saveComboBox = ctk.CTkComboBox (self.fileSave_Frame, values= sF.fileFormat)
		self.saveComboBox.place (relx= 0.3, rely= 0.1)
		self.saveComboBox.set ('Select file format')
		# save button
		self.saveButton = ctk.CTkButton (self.fileSave_Frame, text= 'Save', 
		 command= lambda: sF.saveToFile (self.text_area, self.saveComboBox))
		self.saveButton.place (relx= 0.3, rely= 0.3)
		# --------------------------------------------------------------------------------------
		
		self.grid_columnconfigure(1, weight=1) #to center horizontally all the widgets in column 1
	
	#----gets invoked when source language is clicked on combobox---------
	def combobox_callback_source (self, choice):
		print("combobox dropdown clicked:", choice)
		self.source_language = choice
		return (self)
	
	#----gets invoked when translate language is clicked on combobox---------
	def combobox_callback_translate (self, choice):
		print("combobox dropdown clicked:", choice)
		self.translate_language = choice
		return (self)
	#-----------------------------------------------------------

	# check items in combo box of translate language
	def check_translate_language (self, e): 
		typed = e.widget.get()		# grab what was typed
		print (typed)

		if typed == '':
			data = translate.lang_value_list
		else:
			data = []
			for item in translate.lang_value_list:
				if typed.lower() in item.lower():
					data.append (item)
		
		self.translate_comboBox = ctk.CTkComboBox (self.translate_Frame, values= data, command = self.combobox_callback_translate)
		self.translate_comboBox.place (relx= 0.3, rely= 0.1)
		self.translate_comboBox.bind ("<KeyRelease>", self.check_translate_language)
		self.translate_comboBox.set (typed)

	# check items in combo box of source language
	def check_source_language (self, e): 
		typed = e.widget.get()		# grab what was typed
		print (typed)

		if typed == '':
			data = doc_text.source_language
		else:
			data = []
			for item in doc_text.source_language:
				if typed.lower() in item.lower():
					data.append (item)
		
		self.source_comboBox = ctk.CTkComboBox (self, values= data, command = self.combobox_callback_source) 
		self.source_comboBox.grid (row = 3, column = 0, padx = 10, pady = (10,0))
		self.source_comboBox.bind ("<KeyRelease>", self.check_source_language)
		self.source_comboBox.set (typed)


class CheckboxFrame(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		
		CheckVar = ctk.IntVar()
		CheckVar.set(1)
		self.binarization = ctk.CTkCheckBox(self, text="Binarize", variable= CheckVar)
		self.binarization.grid(row=0, column=0, padx=5, pady=(10, 0), sticky="w")
		self.noise_removal = ctk.CTkCheckBox(self, text="Noise Remove")
		self.noise_removal.grid(row=0, column=1, padx=5, pady=(10, 0), sticky="w")

		variable = ctk.IntVar (self)
		self.font_thickening = ctk.CTkCheckBox(self, text="Font Thinning", onvalue= 1, variable= variable)
		self.font_thickening.grid(row=0, column=2, padx=5, pady=(10, 0), sticky="w")
		self.font_thinning = ctk.CTkCheckBox(self, text="Font Thickening", onvalue= 2, variable= variable)
		self.font_thinning.grid(row=0, column=3, padx=5, pady=(10, 0), sticky="w")	
		
	def get(self):
		checked_checkboxes = []
		if self.binarization.get() == 1:
			checked_checkboxes.append(self.binarization.cget("text"))
		if self.noise_removal.get() == 1:
			checked_checkboxes.append(self.noise_removal.cget("text"))
		if self.font_thickening.get() == 1:
			self.font_thinning.deselect (0)
			checked_checkboxes.append(self.font_thickening.cget("text"))
		if self.font_thinning.get() == 2:
			self.font_thickening.deselect (0)
			checked_checkboxes.append(self.font_thinning.cget("text"))
		return checked_checkboxes	
#-----------------------------------------------------------------

class ImageFrame(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.header= ctk.CTkLabel(self,text = "IMage",font=('Times New Roman', 10, 'bold'), height = 400, width = 300)
		self.header.grid(row = 0, column = 0, padx = 10, pady= (50,0))



'''
# class SideFrame(ctk.CTkFrame):
# 	def __init__(self, master):
# 		super().__init__(master)
		
# 		self.doc_button = ctk.CTkButton(self, text="DOCUMENT OCR", command= master.doc_button_clicked)
# 		self.doc_button.grid(row = 0, column = 0, padx = 10, pady = (10,0), sticky = "w")
# 		# self.non_doc_button = ctk.CTkButton(self, text="NON-DOCUMENT OCR", command=master.non_doc_button_clicked)
# 		# self.non_doc_button.grid(row = 1, column = 0, padx = 10, pady = (30,0), sticky = "w")
# 		self.help_button = ctk.CTkButton(self, text="HELP", command=master.help_button_clicked)
# 		self.help_button.grid(row = 2, column = 0, padx = 10, pady = (30,10), sticky = "w")

# class MainFrame(ctk.CTkFrame):
# 	def __init__(self, master):
# 		super().__init__(master)
# 		self.intro= ctk.CTkLabel(self,
# 		text = "Optical Character Recoginition\n"+
# 		"Use it for getting text and voice from images\n"+
# 		"For Document related work, click on the DOCUMENT button in the left pane\n"+
# 		"For Non-Document related work, click on the NON-DOCUMENT button in the left pane\n",
# 		font=('Times New Roman', 24, 'bold'))
# 		self.intro.grid(row = 0, column = 1, padx = 10, pady= (50,0))
# 		self.grid_rowconfigure(0, weight=1)
# 		self.grid_columnconfigure(1, weight=1)


# class HELP (ctk.CTkFrame):
# 	pass

# class ImageFrame(ctk.CTkFrame):
# 	def __init__(self, master):
# 		super().__init__(master)
# 		self.header= ctk.CTkLabel(self,text = "IMage",font=('Times New Roman', 10, 'bold'), height = 400, width = 300)
# 		self.header.grid(row = 0, column = 0, padx = 10, pady= (50,0))

# class App(ctk.CTk):
# 	def __init__(self):
# 		super().__init__()
		
# 		self.title("OPTICAL CHARACTER RECOGINITION")
# 		self.geometry("1200x800")
# 		# self.grid_columnconfigure(0, weight=0)
# 		self.grid_rowconfigure(0, weight=1)
# 		self.grid_columnconfigure(1, weight = 2)
		
# 		self.side_frame = SideFrame(self)
# 		self.side_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "e")
# 		self.main_frame = MainFrame(self)
# 		self.main_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "news")
		
# 	def doc_button_clicked(self):
# 		print("doc pressed master")
# 		self.main_frame = DocumentFrame(self)
# 		self.main_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "news")
# 	# def non_doc_button_clicked(self):
# 	# 	print("non-doc pressed master")
# 	# 	self.main_frame = NonDocumentFrame(self)
# 	# 	self.main_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "news")

# 	def help_button_clicked(self):
# 		print("non-doc pressed master")
# 		self.main_frame = HELP(self)
# 		self.main_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "news")
		
# app = App()
# app.mainloop()

'''