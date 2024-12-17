from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
import os

def play():
    text = myentry.get() 
    if text.strip():  
        tts = gTTS(text=text, lang='en') 
        tts.save("speech.mp3") 
        playsound("speech.mp3")  
        os.remove("speech.mp3")  
    else:
        messagebox.showwarning("Warning", "Please enter some text!")

def exit():
    root.destroy() 

def set():
    myentry.delete(0, END) 

root = Tk()
root.title("Text to Speech")  
root.geometry("500x600")

mylable1 = Label(root, text=" praivet Text for na3em ").pack(pady=10)
mylable2 = Label(root, text="Enter your text:").pack(pady=10)
myentry = ttk.Entry(root)
myentry.pack(pady=10)

button1 = ttk.Button(root, text="Play", command=play)
button1.pack(pady=10)

button2 = Button(root, text="set", bg="blue", command=set)
button2.pack(pady=10)

button3 = Button(root, text="exit", bg="red", command=exit)
button3.pack(pady=10)

root.mainloop()