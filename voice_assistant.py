import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia

# -----------------------------
# Initialize Engine
# -----------------------------
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) 
engine.setProperty("rate", 170)

listener = sr.Recognizer()


# -----------------------------
# Speak Function
# -----------------------------
def talk(text):
    print("Mahi:", text)
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# Listen Function
# -----------------------------
def take_command():
    command = ""

    with sr.Microphone() as source:
        print("\nListening...")

        listener.adjust_for_ambient_noise(source, duration=1)
        listener.pause_threshold = 1

        try:
            audio = listener.listen(source, timeout=5)

            command = listener.recognize_google(audio)
            command = command.lower()

            print("You:", command)

        except sr.UnknownValueError:
            print("Couldn't understand.")
        except sr.WaitTimeoutError:
            print("No voice detected.")
        except sr.RequestError:
            talk("Internet connection error.")

    return command


# -----------------------------
# Assistant Logic
# -----------------------------
def run_assistant():
    command = take_command()

    if command == "":
        return

    # Wake word
    if "mahi" in command:
        talk("Yes, how can I help you?")

    elif "hello" in command or "hi" in command:
        talk("Hello! I am Mahi. How can I help you?")

    elif "how are you" in command:
        talk("I am doing great. Thank you for asking.")

    elif "your name" in command:
        talk("My name is Mahi.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The current time is " + current_time)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        talk("Today is " + today)

    elif "open youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        talk("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open chatgpt" in command:
        talk("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif "play" in command:
        song = command.replace("play", "").strip()

        if song:
            talk("Playing " + song)
            pywhatkit.playonyt(song)
        else:
            talk("Please tell me the song name.")

    elif "search" in command:
        topic = command.replace("search", "").strip()

        if topic:
            talk("Searching for " + topic)
            pywhatkit.search(topic)
        else:
            talk("Please tell me what to search.")

    elif "who is" in command:
        person = command.replace("who is", "").strip()

        try:
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        except:
            talk("Sorry, I couldn't find information.")

    elif "what is" in command:
        topic = command.replace("what is", "").strip()

        try:
            info = wikipedia.summary(topic, 2)
            print(info)
            talk(info)
        except:
            talk("Sorry, I couldn't find information.")

    elif "thank you" in command:
        talk("You're welcome.")

    elif "stop" in command or "exit" in command or "bye" in command:
        talk("Goodbye! Have a nice day.")
        exit()

    else:
        talk("Sorry, I didn't understand that command.")


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    talk("Hello. I am Mahi, your personal voice assistant. I am ready to help you.")

    while True:
        run_assistant()
