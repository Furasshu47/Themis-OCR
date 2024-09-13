#----------------------------------
import customtkinter as ctk
#----------------------------------
import commonFunctions as cf
#----------------------------------
import DocumentFrame as DF
import NonDocumentFrame as NDF
#----------------------------------

class SideFrame(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		
		self.doc_button = ctk.CTkButton(self, text="DOCUMENT OCR", command= master.doc_button_clicked)
		self.doc_button.grid(row = 0, column = 0, padx = 10, pady = (10,0), sticky = "w")
		self.non_doc_button = ctk.CTkButton(self, text="NON-DOCUMENT OCR", command=master.non_doc_button_clicked)
		self.non_doc_button.grid(row = 1, column = 0, padx = 10, pady = (30,0), sticky = "w")
		self.help_button = ctk.CTkButton(self, text="HELP", command=master.help_button_clicked)
		self.help_button.grid(row = 2, column = 0, padx = 10, pady = (30,10), sticky = "w")


# MainFrame will be replaced  with DocumentFrame or NonDocumentFrame
# and then that frame will be served as the Main Pane on the UI

class MainFrame(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.intro= ctk.CTkLabel(self,
		text = "Optical Character Recoginition\n"+
		"Use it for getting text and voice from images\n"+
		"For Document related work, click on the DOCUMENT button in the left pane\n"+
		"For Non-Document related work, click on the NON-DOCUMENT button in the left pane\n",
		font=('Times New Roman', 24, 'bold'))
		self.intro.grid(row = 0, column = 1, padx = 10, pady= (50,0))
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)

class HELP (ctk.CTkFrame):
	pass

class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		
		self.title("OPTICAL CHARACTER RECOGINITION")
		self.geometry("1200x800")
		# self.grid_columnconfigure(0, weight=0)
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight = 2)
		
		self.side_frame = SideFrame(self)
		self.side_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "e")
		self.main_frame = MainFrame(self)
		self.main_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "news")
	
	def doc_button_clicked(self):
		print("doc pressed master")
		self.main_frame = DF.DocumentFrame(self)
		self.main_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "news")
	def non_doc_button_clicked(self):
		print("non-doc pressed master")
		self.main_frame = NDF.NonDocumentFrame(self)
		self.main_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "news")

	def help_button_clicked(self):
		print("non-doc pressed master")
		self.main_frame = HELP(self)
		self.main_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "news")
		
app = App()
app.mainloop()

