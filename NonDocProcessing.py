from easyocr import *
import cv2

LANGUAGES = {
	'Abaza'     :	'abq',
	'Adyghe'	:	'ady',
	'Afrikaans'	:	'af',
	'Angika'	:	'ang',
	'Arabic'	:	'ar',
	'Assamese'	:	'as',
	'Avar'		:	'ava',
	'Azerbaijani':	'az',
	'Belarusian':	'be',
	'Bulgarian'	:	'bg',
	'Bihari'	:	'bh',
	'Bhojpuri'	:	'bho',
	'Bengali'	:	'bn',
	'Bosnian'	:	'bs',
	'Simplified Chinese' :	'ch_sim',
	'Traditional Chinese':	'ch_tra',
	'Chechen'	:	'che',
	'Czech'		:	'cs',
	'Welsh'		:	'cy',
	'Danish'	:	'da',
	'Dargwa'	:	'dar',
	'German'	:	'de',
	'English'	:	'en',
	'Spanish'	:	'es',
	'Estonian'	:	'et',
	'Persian (Farsi)'	:	'fa',
	'French'	:	'fr',
	'Irish'		:	'ga',
	'Goan Konkani'	:	'gom',
	'Hindi'		:	'hi',
	'Croatian'	:	'hr',
	'Hungarian'	:	'hu',
	'Indonesian':	'id',
	'Ingush'	:	'inh',
	'Icelandic'	:	'is',
	'Italian'	:	'it',
	'Japanese'	:	'ja',
	'Kabardian'	:	'kbd',
	'Kannada'	:	'kn',
	'Korean'	:	'ko',
	'Kurdish'	:	'ku',
	'Latin'		:	'la',
	'Lak'		:	'lbe',
	'Lezghian'	:	'lez',
	'Lithuanian':	'lt',
	'Latvian'	:	'lv',
	'Magahi'	:	'mah',
	'Maithili'	:	'mai',
	'Maori'		:	'mi',
	'Mongolian'	:	'mn',
	'Marathi'	:	'mr',
	'Malay'		: 	'ms',
	'Maltese'	:	'mt',
	'Nepali'	:	'ne',
	'Newari'	:	'new',
	'Dutch'		:	'nl',
	'Norwegian'	:	'no',
	'Occitan'	:	'oc',
	'Pali'		:	'pi',
	'Polish'	:	'pl',
	'Portuguese':	'pt',
	'Romanian'	:	'ro',
	'Russian'	:	'ru',
	'Serbian (cyrillic)':	'rs_cyrillic',
	'Serbian (latin)'	:	'rs_latin',
	'Nagpuri'	:	'sck',
	'Slovak'	:	'sk',
	'Slovenian'	:	'sl',
	'Albanian'	:	'sq',
	'Swedish'	:	'sv',
	'Swahili'	:	'sw',
	'Tamil'		:	'ta',
	'Tabassaran':	'tab',
	'Telugu'	:	'te',
	'Thai'		:	'th',
	'Tajik'		:	'tjk',
	'Tagalog'	:	'tl',
	'Turkish'	:	'tr',
	'Uyghur'	:	'ug',
	'Ukranian'	:	'uk',
	'Urdu'		:	'ur',
	'Uzbek'		:	'uz',
	'Vietnamese':	'vi'
}

source_language = list (LANGUAGES.keys())

def processing (self, language):
	print ("Convert Button clicked nondoc")
	self.image = cv2.imread (self.file_name) #Reading the required image
	reader = easyocr.Reader ([LANGUAGES[language]], gpu = True )
	# extracting text into list
	text = reader.readtext (self.image, detail= 0, paragraph= True)
	# storing text into string variable
	non_doc_ocr_text = ''
	for x in text:
		non_doc_ocr_text += ('\n' + x) 
	
	ocr_result= non_doc_ocr_text
	boxDraw (self, language)
	return (ocr_result)
	

def boxDraw(self, language):
	reader = easyocr.Reader (['en'], gpu = True )
	result = reader.readtext (self.image)
	for detection in result:	
		top_left = tuple ([int(val) for val in detection[0][0]])
		bottom_right = tuple ([int(val) for val in detection[0][2]])
		text = detection[1] 
		if language == 'English':
			font = cv2.FONT_HERSHEY_SIMPLEX
			print ('28 ' , ' ' , self.image)
			self.image = cv2.rectangle (self.image, top_left, bottom_right, (0,255,0), 3)
			self.image = cv2.putText (self.image, text, top_left, font,0.5, (255,255,255), 3, cv2.LINE_AA)
			self.image = cv2.putText (self.image, text, top_left, font,0.5, (0,0,0), 1, cv2.LINE_AA)
		else:
			self.image = cv2.rectangle (self.image, top_left, bottom_right, (0,255,0), 3)
			
	cv2.imwrite ("images/non_doc_output_image.jpg", self.image) #Saving the image after preprocessing
