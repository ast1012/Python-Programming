import psutil
import pyttsx3
import datetime
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import random
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to set a reminder
def remind():
    speak("What shall i remind  for")
    text = command()    #Takes the input of the purpose of reminder
    speak("Mam, please enter in how much time should i remind you?")
    timer = int(input("enter-->"))
    speak("Reminder set successfully")
    timer = timer * 60
    time.sleep(timer)
    speak(f"Mam, it's time for {text}. ")

def charge(num):
    if num <= 35:
        speak("Please plugin your system battery is low..")
    elif num <=20:
        speak("Please plugin urgently your system battery is extremly low")
    elif num>=80:
        speak("Hmm... your battery is quite healthy. Hope that dosen't drains out fast.")
    else:
        pass

def volume_contol(choice):
    if "volume up" in choice:
        pyautogui.press("volumeup")
    elif "volume down" in choice:
        pyautogui.press("volumedown")
    elif "mute" in choice:
        pyautogui.press("volumemute")


def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(f"Good Morning. Have a nice day")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("My Name is Luna. I am here to help you")



def command():
    """This function takes input from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening You......")
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='ENG-IN')
        print(f"You asked: {query}\n")
    except Exception as error:
        errors = [
            "I don't know what you mean",
            "Excuse me? What do you wanna say?",
            "Can you repeat it please?",
        ]
        error = random.choice(errors)
        print("Error.....Hang On")
        #speak("Error ....Hang on")
        speak(error)
        return "NONE"
    return query


if __name__ == '__main__':
    greet()
    speak("May I have your name please")
    name = command()
    speak(name)
    speak("Is that what I should call you?")
    ans = command()
    if ans=="no":
        speak("sorry for mistake! What should I call you?")
        name2 = command()
        speak(name2)
        speak("Hope That's Right")
        name = name2
    else:
        speak("Okay! So now lets begin with tasks")

    while True:
        query = command().lower()
        if 'search' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(f"{name}According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening..Youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening..Google")
            webbrowser.open("google.com")
            speak(f"What should i search for {name}?")
            search = command().lower()
            webbrowser.open(search)
        elif 'ip address' in query:
            ip = requests.get("https://api.ipify.org").text
            speak(f"Your ip address is {ip}")
        elif 'reminder' in query:
            remind()
        elif 'thank you' in query:
            speak(f"Ahh...No problem. That's my work!{name}")
        elif 'shutdown' in query:
            speak(f"{name}Are you sure you want to shutdown")
            answer = command()
            if answer=="yes":
                os.system("shutdown /s /t 1")
            else:
                break
        elif 'hello' in query:
            speak("Hi! In your service always")
        elif 'restart' in query:
            speak(f"{name}Are you sure you want to restart")
            answer = command()
            if answer=="yes":
                os.system("shutdown /r /t 1")
            else:
                break
        elif 'notepad' in query:
            speak(f"As your Order {name},Opening..Notepad")
            cmd = 'notepad'
            os.system(cmd)
        elif 'command prompt' in query:
            speak("opening...")
            os.system("start cmd")
        elif "volume" in query:
            volume_contol(query)
        elif "exit" in query:
            print("Quitting...")
            speak(f'Terminating.....\n Thankyou for your time. \n Hope to see you soon {name}')
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{name}The time is {strTime}")
        elif 'date' in query:
            strTime = datetime.datetime.now().strftime("%d-%B-%y")
            speak(f"{name}, the date is{strTime}")
        elif "battery" in query:
            battery = psutil.sensors_battery()
            percent = battery.percent
            speak(f"{name}The battery is {percent} percentage")
            charge(percent)
        elif 'stack overflow' in query:
            speak("Opening..")
            webbrowser.open("stackoverflow.com")
        elif 'who are you' in query:
            speak('I am Luna, your virtual friend. Here to help you at your tasks. I was born on 22 April 2021')
        elif 'sleep' in query:
            time.sleep(3)
        