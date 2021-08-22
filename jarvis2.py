import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import platform
import ctypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning saloo")
    elif hour >12 and hour<=18:
        speak("good afternoon saloo")
    else:
        speak("good evening saloo")

    speak("hye sir ! i am JARVIS. please! tell me how may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'tell me about system' in query:
            uname = platform.uname()
            system = uname.system
            procrssor = uname.processor
            version = uname.version

            
            print("Your system:"+system)

            speak("Your system is "+system)
            
            print("System version:"+version)
            
            speak("and your system version is"+version)
            
            print("Your Processor:"+procrssor)
            
            speak("and your Processor is"+procrssor)
            
        elif "lock the system" in query:
            print("Locking the system ...")
            speak("Locking the system")
            ctypes.windll.user32.LockWorkStation()


            
            
