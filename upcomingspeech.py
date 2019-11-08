import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import time
import random
import webbrowser

r = sr.Recognizer()
def speak(string):
    a = random.random()
    if "visit" in string:
        url = string[6:]
        tts = gTTS(text="Opening "+url, lang="en")
        tts.save("audio"+str(a)+".mp3")
        playsound("audio"+str(a)+".mp3", True)
        os.remove("audio"+str(a)+".mp3")
        webbrowser.open(url)
while True:
    print("Speak")
    with sr.Microphone() as source:
        audio = r.listen(source)
    data = r.recognize_google(audio)
    speak(data)
        
    time.sleep(2)

