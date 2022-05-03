import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os

listener=sr.Recognizer()
engine  = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
   
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<12:
        talk("Good Morning!")
    elif hour>=12 and hour<18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")
    talk("I am Jasper")
    talk("How can I help you?")

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'jasper' in command:
                command=command.replace('jasper','')
                print(command)
    except:
        pass
    return command


def run_jasper():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+time)
    elif 'search wikipedia for' in command:
        search=command.replace('search wikipedia for','')
        info=wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'open code editor' in command:
        talk('opening vs codes')
        os.startfile("C:\\Users\91991\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    elif 'google' in command:
        talk('opening google')
        os.startfile("https://www.google.com/")  
    
    



wishMe()
run_jasper()



