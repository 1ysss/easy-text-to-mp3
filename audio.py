import pyttsx3
from gtts import gTTS
from tqdm import tqdm
from time import sleep

engine = pyttsx3.init()

file_path = input( "Enter the path to the file ...(Введите путь к файлу)  ")

file = open( file_path, 'r')

theText = file.read()

engine.say( theText )
engine.runAndWait()

file.close()

for i in tqdm( range( 100 ) ):
	sleep( 0.01 )

tts = gTTS ( text = theText, lang = 'ru' )
tts.save( 'youfile.mp3' )

print( 'File Saved(Файл сохранен)...' )
