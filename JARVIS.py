# -*- coding: utf-8 -*-
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to,content):
    server= smtplib.SMTP("smtp.gmailcom", 587)
    server.ehlo()
    server.starttls()
    server.login('jainritz.ritika18@gmail.com', 'ritika18')
    server.sendmail('jainritz.ritika18@gmail.com', to, content)
    server.close()
    
    

if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("Wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia....")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverFlow' in query:
            webbrowser.open("stackoverFlow.com")
        elif 'open Github' in query:
            webbrowser.open("github.com')
        elif 'open HackerRank' in query:
            webbrowser.open("hackerrank.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H%M%S")
            speak(f"The time is {strTime}")
        elif 'send email to Ritika' in query:
            try:
                speak("What should i say")
                content=takeCommand()
                to="jainritz.ritika18@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send the email")
                
                
        
        
