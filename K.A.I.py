# IMPORT DEPENDENCIES #
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
from bs4 import BeautifulSoup

# SET VOICE ASSISTANT SETTINGS #
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

# SET CHROME PATH #
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# SET MUTE VARIABLES #
muted = False

# DEFINE SPEAK FUNCTION #
def speak(text):
    engine.say(text)
    engine.runAndWait()

# DEFINE COMMAND TAKING FUNCTIONALITY #
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak ("Sorry, I don't understand what you said")
            return "None"
        return statement
        
# PRINT AND SPEAK A GREETING #
print("Loading your AI personal assistant K.A.I")
speak("Loading your AI personal assistant KAI")

# SET THE MAIN FUNCTIONS IN MOTION #
if __name__=='__main__':
    while True:
        statement = takeCommand().lower()
        if "mute" in statement:
            muted = True

        if "unmute" in statement:
            muted = False
            
        while muted == False: 
            if statement==0:
                continue

            if "stop" in statement:
                speak("KAI is shutting down")
                print("K.A.I is shutting down")
                break

            elif 'search wikipedia for' in statement:
                speak('KAI is searching Wikipedia...')
                statement = statement.replace("search wikipedia for ", "")
                try:
                    results = wikipedia.summary(statement, sentences=3, auto_suggest=False)
                    speak("According to Wikipedia")
                    webbrowser.open_new_tab(f"https://en.wikipedia.org/wiki/{statement}")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.PageError:
                    print(f"Sorry! K.A.I couldn't find anything on wikipedia for the term {statement}")
                    speak(f"Sorry! KAI couldn't find anything on wikipedia for the term {statement}")
                    continue
                break

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube has been opened")
                time.sleep(5)
                break

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("google has been opened")
                time.sleep(5)
                break

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("https://www.gmail.com")
                speak("gmail has been opened")
                time.sleep(5)
                break

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M")
                speak(f"the time is {strTime}")
                break

            elif 'search google for' in statement:
                statement = statement.replace("search google for ", "")
                statement = statement.replace("/", "")
                webbrowser.get(chrome_path).open_new_tab("https://www.google.com/?#q=" + statement)
                time.sleep(5)
                break

            elif 'ask' in statement:
                speak('What do you want me to answer')
                question=takeCommand()
                app_id="Paste your unique ID here "
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)
                break

            elif "weather" in statement:
                api_key="0cd7154e622527c76c419aceb2585127"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("what is the city name")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                          str(current_temperature) +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    print(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))
                break

            elif "log off" in statement or "sign out" in statement:
                speak("are you sure")
                question=takeCommand()
                if "yes" in question:
                    speak("shutting down")
                    subprocess.call(["shutdown", "/l"])
                else:
                    speak("aborting shut down")
                break
        
            else:
                speak("Sorry KAI couldn't find what you were looking for")
                print("Sorry K.A.I couldn't find what you were looking for")
                break
