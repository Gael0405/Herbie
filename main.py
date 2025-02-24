
import speech_recognition as sr
import pyttsx3


#Creating a recognizer 
r = sr.Recognizer()

with sr.Microphone() as source: 
    while True:
     audio = r.listen(source)
    print(r.recognize_google(audio, language= 'pt'))

    