import translate as translate
import speak as speak
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
import NonDocProcessing as non_doc_ocr
import DocProcessing as doc_ocr
import cv2
import pytesseract
import customtkinter as ctk

def convert_button_clicked(self, option):
	print("Convert Button clicked")
	# for document ocr
	if option == 1:
		self.checked_checkboxes = self.checkbox_frame.get()
		self.image= cv2.imread(self.file_name) #Reading the required image
		#all the choice values are the text value from the checkbox[see CheckboxFrame class
		for choice in self.checked_checkboxes:
			if(choice == "Binarize"):
				self.image = doc_ocr.binarize(self.image)
			elif(choice == "Noise Remove"):
				self.image = doc_ocr.no_noise(self.image)
			elif(choice == "Font Thinning"):
				self.image = doc_ocr.thin(self.image)
			elif(choice == "Font Thickening"):
				self.image = doc_ocr.thick(self.image)
		# cv2.imwrite ("images/doc_output_image.jpg", self.image) #Saving the image after preprocessing
		self.ocr_result= pytesseract.image_to_string (self.image)#, lang= self.source_language)	
		# doc_ocr.boxDraw (self)
		cv2.imwrite ("images/doc_output_image.jpg", self.image) #Saving the image after preprocessing
		self.image = Image.open ("images/doc_output_image.jpg")

	# for non document ocr
	if option == 2:
		self.ocr_result = non_doc_ocr.processing (self, self.source_language)
		self.image = Image.open ("images/non_doc_output_image.jpg")

	self.text_area.configure(font=('Times New Roman', 18))
	self.text_area.delete('1.0', 'end')
	self.text_area.insert('1.0', self.ocr_result)
	# #-------displaying the processed saved image-----------
	# self.image = Image.open("images/non_doc_output_image.jpg")
	self.resize_image = self.image.resize((350, 500))
	self.transformed_image =  ImageTk.PhotoImage(self.resize_image)
	self.converted_image_frame.header.configure(image = self.transformed_image)
	#---------------------------------------------------
	#--------------saving the text as voice using speak.py--------
	speak.saveVoice (self.ocr_result)

def browse_button_clicked(self):
	print("Browse Button clicked")
	self.file_name = filedialog.askopenfilename(title="Select a File")
	self.image = Image.open(self.file_name)
	self.resize_image = self.image.resize((350, 500))
	self.transformed_image =  ImageTk.PhotoImage(self.resize_image)
	self.original_image_frame.header.configure(image = self.transformed_image)

def translate_button_clicked(self):
	if (self.translate_language == None):
		messagebox.showinfo("Warning", "Please choose a Destination Language.")
		print ('File format not chosen.')
		return
	self.translated_text = translate.translate_text (self.ocr_result, self.source_language, self.translate_language)
	self.text_area.delete('1.0', 'end')
	self.text_area.insert('1.0', self.translated_text)
#-----------------------------------------------------------

#-------to listen the converted text audi------------	
def listen_button_clicked():
	print("listen button clicked")
	'''
	Consuming time for saving the voice in here.
	'''
	# self.text = self.text_area.get("1.0", "end-1c")
	# if(self.text == ""):
		# return
	# speak.save_voice(self.text)
	speak.playTTS ()

#-------stops playing the audio file----------
def stop_button_clicked():
	print("stop button clicked")
	speak.stopTTS ()	

def pause_button_clicked():
	print("pause button clicked")
	speak.pauseTTS ()	

def resume_button_clicked():
	print("resume button clicked")
	speak.resumeTTS ()		
#---------------------------------------------	

