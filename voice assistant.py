import speech_recognition as sr
import pyttsx3
import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is currently unavailable.")
        return ""

def get_user_name():
    speak("What should I call you?")
    return listen()

def welcome_statement(name):
    speak(f"Welcome {name}! I'm here to assist you.")

def respond_to_greeting(command):
    if "hello" in command or "hi" in command:
        speak("Hello! How can I assist you today?")
    elif "your name" in command:
        speak("I am your voice assistant.")
    else:
        speak("Hi there!")

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def tell_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def tell_tomorrow():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    speak(f"Tomorrow is {tomorrow.strftime('%A, %B %d, %Y')}")

def handle_command(command, name):
    if any(word in command for word in ["hello", "hi", "your name"]):
        respond_to_greeting(command)
    elif "time" in command:
        tell_time()
    elif "tomorrow" in command:
        tell_tomorrow()
    elif "date" in command:
        tell_date()
    elif "stop" in command or "exit" in command or "bye" in command:
        speak(f"Goodbye {name}, have a great day!")
        return False
    else:
        speak(f"Sorry {name}, I didn't understand that.")
    return True

def main():
    name = get_user_name()
    welcome_statement(name)
    speak(f"{name}, how can I help you?")
    while True:
        command = listen()
        if not handle_command(command, name):
            break

if __name__ == "__main__":
    main()
