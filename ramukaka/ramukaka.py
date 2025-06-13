import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import threading
import datetime
import os

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen function
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        display_text("🎤 RAMU is listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        display_text("🧠 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        display_text(f"📢 You said: {query}")
    except:
        display_text("❌ RAMU didn’t catch that.")
        return "None"
    return query.lower()

# Show in GUI
def display_text(text):
    output_box.insert(tk.END, text + "\n")
    output_box.see(tk.END)

# Process voice commands
def process_command():
    query = take_command()

    if "open notepad" in query:
        speak("Opening Notepad.")
        display_text("🗒️ RAMU is opening Notepad.")
        os.system("notepad.exe")

    elif "open chrome" in query:
        speak("Opening Chrome.")
        display_text("🌐 RAMU is opening Chrome.")
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)

    elif "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
        display_text(f"🕒 RAMU says the time is {now}")

    elif "exit" in query or "quit" in query:
        speak("Goodbye Sahil. RAMU signing off.")
        root.destroy()

    else:
        speak("Sorry Sahil, RAMU doesn't understand that yet.")
        display_text("🤖 Unknown command.")

# Run commands without freezing GUI
def threaded_command():
    threading.Thread(target=process_command).start()

# RAMU greets you
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greet = "Good morning Sahil!"
    elif 12 <= hour < 18:
        greet = "Good afternoon Sahil!"
    else:
        greet = "Good evening Sahil!"
    speak(greet)
    display_text(greet)
    speak("I am RAMU, your assistant. How can I help you?")
    display_text("I am RAMU, your assistant. How can I help you?")

# --- GUI Setup ---
root = tk.Tk()
root.title("RAMU - Your Personal Assistant")
root.geometry("500x500")
root.configure(bg="black")
root.attributes('-topmost', True)

# Center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (500 // 2)
y = (screen_height // 2) - (500 // 2)
root.geometry(f"+{x}+{y}")

# Title Label
title = tk.Label(root, text="🤖 RAMU - AI Assistant", font=("Helvetica", 16, "bold"), fg="cyan", bg="black")
title.pack(pady=10)

# Output Area
output_box = scrolledtext.ScrolledText(root, font=("Consolas", 12), wrap=tk.WORD, bg="black", fg="white")
output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Mic Button
mic_btn = tk.Button(root, text="🎙️ Speak to RAMU", font=("Helvetica", 14), bg="cyan", fg="black", command=threaded_command)
mic_btn.pack(pady=20)

# Start Assistant
wish_me()
root.mainloop()
