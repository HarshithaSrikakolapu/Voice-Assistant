# 🎙️ Mahi – Personal Voice Assistant

Mahi is a Python-based **personal voice assistant** that listens to voice commands, understands them using speech recognition, and responds using text-to-speech.

It can perform common tasks such as opening websites, playing YouTube videos, searching the web, telling the current time and date, and retrieving information from Wikipedia.

---

## ✨ Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech responses
* 👋 Greeting and basic conversation
* ⏰ Current time
* 📅 Current date
* ▶️ Play songs/videos on YouTube
* 🔎 Search the web
* 📖 Search Wikipedia
* 🌐 Open Google
* ▶️ Open YouTube
* 🤖 Open ChatGPT
* 🛑 Voice-controlled exit
* 🌍 Uses Google Speech Recognition for converting speech to text

---

## 🛠️ Technologies Used

| Technology        | Purpose                              |
| ----------------- | ------------------------------------ |
| Python            | Core programming language            |
| SpeechRecognition | Converts voice commands into text    |
| PyAudio           | Provides microphone input            |
| pyttsx3           | Converts text into speech            |
| PyWhatKit         | YouTube playback and web search      |
| Wikipedia         | Retrieves information from Wikipedia |
| Webbrowser        | Opens websites                       |
| Datetime          | Retrieves current date and time      |

---

## 📁 Project Structure

```text
Mahi-Voice-Assistant/
│
├── mahi.py
└── README.md
```

---

## ⚙️ Requirements

Make sure Python is installed on your system.

Check your Python version:

```bash
python --version
```

Install the required libraries:

```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia
```

For microphone support, install PyAudio:

```bash
pip install PyAudio
```

If PyAudio installation fails on Windows, try:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/HarshithaSrikakolapu/Voice-Assistant.git
```

### 2. Navigate to the project

```bash
cd voice-assistant
```

### 3. Install dependencies

```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia PyAudio
```

### 4. Run the assistant

```bash
python voice_assistant.py
```

Mahi will start with:

```text
Hello. I am Mahi, your personal voice assistant.
I am ready to help you.
```

---

## 🎤 Voice Commands

Mahi supports commands such as:

### Basic Conversation

```text
Hello
Hi
How are you
What is your name
Thank you
```

### Date and Time

```text
What is the time
What is today's date
```

### Open Websites

```text
Open YouTube
Open Google
Open ChatGPT
```

### Play YouTube

```text
Play Believer
Play Shape of You
Play Python tutorials
```

### Web Search

```text
Search Python programming
Search artificial intelligence
Search latest technology
```

### Wikipedia

```text
Who is Albert Einstein
What is artificial intelligence
What is machine learning
```

### Exit

```text
Stop
Exit
Bye
```

---

## 🧠 How It Works

The assistant follows a simple voice-processing pipeline:

```text
        🎤 Microphone
              │
              ▼
     Speech Recognition
              │
              ▼
       Voice → Text
              │
              ▼
       Command Processing
              │
       ┌──────┴──────┐
       │             │
       ▼             ▼
  Local Actions   Web Services
       │             │
       └──────┬──────┘
              ▼
       Text Response
              │
              ▼
       Text-to-Speech
              │
              ▼
           🔊 Voice
```

### 1. Listen

The microphone captures the user's voice using `SpeechRecognition`.

### 2. Convert Speech to Text

Google Speech Recognition converts the captured audio into text.

### 3. Process the Command

The `run_assistant()` function checks the recognized command and determines the appropriate action.

### 4. Perform the Action

Depending on the command, Mahi can:

* Open a website
* Search the web
* Play a YouTube video
* Retrieve Wikipedia information
* Tell the time or date

### 5. Respond

`pyttsx3` converts the response text into speech.

---

## 🔑 Main Functions

### `talk(text)`

Converts text into speech.

```python
def talk(text):
    print("Mahi:", text)
    engine.say(text)
    engine.runAndWait()
```

### `take_command()`

Listens through the microphone and converts speech into text.

```python
def take_command():
    ...
```

### `run_assistant()`

Processes the recognized command and executes the corresponding action.

```python
def run_assistant():
    ...
```

---

## 🌐 External Services

The project uses external services/libraries for some functionality:

* **Google Speech Recognition** – Speech-to-text
* **YouTube** – Video/song playback
* **Wikipedia** – Information retrieval
* **Google Search** – Web searching

An active internet connection is required for speech recognition, Wikipedia searches, web searches, and YouTube-related functionality.

---

## ⚠️ Troubleshooting

### Microphone not detected

Check that your microphone is connected and available to Python.

You can also list available microphones:

```python
import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(index, name)
```

### `ModuleNotFoundError`

Install the missing package:

```bash
pip install package-name
```

For example:

```bash
pip install SpeechRecognition
```

### PyAudio installation error

On Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

### Speech recognition not working

Make sure:

* Your microphone is working.
* Python has microphone permissions.
* Your internet connection is active.
* You are speaking clearly.
* Google Speech Recognition is accessible.

---

## 🔮 Future Improvements

Possible improvements for Mahi include:

* 🔐 Wake-word detection
* 🤖 AI-powered conversational responses
* 📧 Send emails using voice commands
* 📱 WhatsApp messaging
* 📰 News updates
* 🌦️ Weather information
* 🎵 Spotify integration
* 📂 Computer file management
* ⏰ Voice-controlled alarms and reminders
* 🧠 Context-aware conversations
* 🗣️ Multiple language support
* 🏠 Smart-home device control
* 🔒 User authentication

---

## 📌 Limitations

* Speech recognition depends on an internet connection.
* The current command system uses predefined `if/elif` conditions.
* The assistant does not maintain conversation context.
* Wikipedia responses may fail for ambiguous topics.
* Some features depend on third-party services.
* Microphone permissions are required.

---

## 👩‍💻 Author

**Harshitha Srikakakolapu**

B.Tech – Computer Science & Engineering

---

## 📄 License

This project is intended for educational and personal use.
