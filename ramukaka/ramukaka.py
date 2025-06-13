import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import threading
import datetime
import os

# Voice Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Show text in GUI
def display_text(text):
    output_box.insert(tk.END, text + "\n")
    output_box.see(tk.END)

# Listen from mic
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        display_text("🎤 RAMU is listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        display_text("🧠 Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        display_text(f"📢 You said: {query}")
    except:
        display_text("❌ RAMU didn’t catch that.")
        return "None"
    return query.lower()

# Process commands
def process_command():
    query = take_command()
    if query == "None":
        return

    if "open notepad" in query:
        speak("Opening Notepad.")
        display_text("🗒️ RAMU is opening Notepad.")
        os.system("notepad.exe")

    elif "open chrome" in query:
        speak("Opening Chrome.")
        display_text("🌐 RAMU is opening Chrome.")
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)

    elif "what time" in query or "tell me the time" in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")
        display_text(f"🕒 RAMU: The time is {time}")

    elif "exit" in query or "close" in query:
        speak("Goodbye Sahil. RAMU signing off.")
        root.destroy()

    else:
        speak("Sorry Sahil, I don't understand that command yet.")
        display_text("🤖 RAMU: Command not recognized.")

# Thread wrapper
def threaded_command():
    threading.Thread(target=process_command).start()

# Greet user
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
    speak("I am RAMU, your assistant. Tap the button and talk to me.")
    display_text("🤖 I am RAMU. Tap the button and talk to me.")

# ---------------- GUI -------------------
root = tk.Tk()
root.title("RAMU - Personal Assistant")
root.geometry("500x500")
root.configure(bg="black")
root.attributes('-topmost', True)

# Center window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (500 // 2)
y = (screen_height // 2) - (500 // 2)
root.geometry(f"+{x}+{y}")

# Title
title = tk.Label(root, text="🤖 RAMU - Voice Assistant", font=("Helvetica", 16, "bold"), fg="cyan", bg="black")
title.pack(pady=10)

# Output
output_box = scrolledtext.ScrolledText(root, font=("Consolas", 12), wrap=tk.WORD, bg="black", fg="white")
output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Mic Button
mic_btn = tk.Button(
    root,
    text="🎙️ Talk to RAMU",
    font=("Helvetica", 14),
    bg="cyan",
    fg="black",
    command=threaded_command
)
mic_btn.pack(pady=20)

# Start
wish_me()
root.mainloop()
