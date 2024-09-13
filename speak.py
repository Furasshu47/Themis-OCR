from gtts import gTTS
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #to hide the welcome prompt
import pygame

pygame.mixer.init() #initialize pygame mixer

# # Import the required module
# import pyttsx3
 
# # Initialize the Pyttsx3 engine
# engine = pyttsx3.init()

def saveVoice (text):
	tts = gTTS (text, lang = 'en', slow= False)
	file_path = 'voices/voice.mp3'
	# if file_path != None:
	# 	del (file_path)
	# 	print ('file deleted')
	tts.save(file_path)
	# We can use file extension as mp3 and wav, both will work
	# engine.save_to_file(text, 'voices/voice.mp3')

	# # Wait until above command is not finished.
	# engine.runAndWait()


def playTTS(): #using pygame	
	pygame.mixer.music.load('voices/voice.mp3')
	pygame.mixer.music.play(loops = 0)

def stopTTS():
	pygame.mixer.music.stop()

def pauseTTS():
	pygame.mixer.music.pause()

def resumeTTS():
	pygame.mixer.music.unpause()
