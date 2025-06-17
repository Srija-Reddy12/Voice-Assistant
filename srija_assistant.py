import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, I didn't catch that.")
        return "None"
    return query.lower()

# Main program
wish_user()

while True:
    query = take_command()

    if 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")

    elif 'date' in query:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {date}")

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif 'who is' in query:
        person = query.replace("who is", "")
        info = wikipedia.summary(person, sentences=2)
        speak(info)

    elif 'open notepad' in query:
        os.system('notepad.exe')
        speak("Opening Notepad")

    elif 'exit' in query or 'stop' in query:
        speak("Goodbye!")
        break