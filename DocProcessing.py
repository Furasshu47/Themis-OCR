import cv2
import numpy as np
import pytesseract

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

def to_gray(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

def binarize(image):
	image= to_gray(image) 
	_, image= cv2.threshold(image, 150, 255, cv2.THRESH_BINARY) 
	return(image)

def no_noise(image):
	kernel= np.ones((1,1), np.uint8) 
	image= cv2.dilate(image, kernel, iterations= 1) 
	kernel= np.ones((1,1), np.uint8) 
	image= cv2.erode(image, kernel, iterations= 1)
	image= cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel) 
	image= cv2.medianBlur(image, 3) 
	return(image) 


def thin(image):
	image= cv2.bitwise_not(image) 
	kernel= np.ones((2,2), np.uint8)
	image= cv2.erode(image, kernel, iterations= 1) 
	image= cv2.bitwise_not(image)
	return(image) 


def thick(image):
	image= cv2.bitwise_not(image) 
	kernel= np.ones((2,2), np.uint8) 
	image= cv2.dilate(image, kernel, iterations= 1) 
	image= cv2.bitwise_not(image)
	return(image) 

# draw boxes around each extracted text and print the text value under it
def boxDraw (self):
	img = cv2.imread (self.image)
	hImg, wImg, _ = img.shape
	#print (hImg, "    ", wImg)  
	boxes = pytesseract.image_to_boxes (img)
	for b in boxes.splitlines():
		#print (b)
		b = b.split (' ')
		#print (b)
		x, y, w, h = int (b[1]), int (b[2]), int (b[3]), int (b[4])
		cv2.rectangle (img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)
		cv2.putText (img, b[0], (x, hImg-y+20), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

	# cv2.imshow ('Resulted Pic Title ', img)
	# cv2.waitKey (0)

