import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("User said:", command)
            return command
        except sr.UnknownValueError:
            talk("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            talk("Sorry, there is a network issue.")
            return ""
        except sr.WaitTimeoutError:
            talk("No input received.")
            return ""
def run_assistant():
    command = take_command()
    if "hello" in command:
        talk("Hello! How can I help you today?")
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " + time)
    elif "date" in command:
        date = datetime.datetime.now().strftime('%A, %d %B %Y')
        talk("Today's date is " + date)
    elif "search" in command:
        topic = command.replace("search", "").strip()
        talk("Searching for " + topic)
        pywhatkit.search(topic)
    elif command != "":
        talk("I didn't understand that. Please try again.")
while True:
    run_assistant()

