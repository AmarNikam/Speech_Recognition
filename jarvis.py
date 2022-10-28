import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)       #0 = Male voice     #1 = Female voice

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                command = command.replace("jarvis", " ")
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", " ")
        talk("playing this" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M %p")
        talk("current time is" + time)
        print(time)
    elif "who is" in command:
        wiki = command.replace("who is", "")
        person = wikipedia.summary(wiki)
        talk(person)
        print(person)
    elif "your name" in command:
        name = command.replace("your name", "")
        talk("My name is Jarvis and i am your friend" + name)
        print(talk())
    else:
        talk("Please,say again!")

while True:
    run_jarvis()