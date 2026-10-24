import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from replit import audio
import pytz
import re
import pygame
country = pytz.timezone('Asia/Singapore')
pygame.mixer.init()
pygame.mixer.music.load("SoundFolder/alarm-clock-90867.mp3")
window = tk.Tk()
window.geometry("500x500")
window.configure(bg='#E6E6E6')
window.title("Alarm Clock")
def updateTime():
    timeNow = datetime.now(country).strftime("%H:%M:%S")
    time_label.config(text=timeNow)
    time_label.after(1000,updateTime)
    checkAlarm()
def checkFormat(text):
    time_pattern = re.compile(r'\d{2}:\d{2}:\d{2}')
    if time_pattern.match(text):
        return True
    else:
        return False
def checkAlarm():
    alarmTime = alarm_entry.get()
    currentTime = datetime.now(country).strftime("%H:%M:%S")
    if currentTime == alarmTime:
        pygame.mixer.music.play(-1)
        global popup
        popup = tk.Toplevel(window)
        popup.title("Alarm")
        tk.Label(popup,text="Alarm is Playing...").pack()
        tk.Button(popup,text="Stop",command=stopAlarm).pack(pady=10)
def stopAlarm():
    pygame.mixer.music.stop()
    popup.destroy()
def updateLabel():
    alarm_text = alarm_entry.get()
    if alarm_text == "":
        messagebox.showerror(title="Error!", message="Put in a value.")
    elif not checkFormat(alarm_text):
        messagebox.showerror(title="Error!", message="Wrong format. (HH:MM:SS)")  
    else:
        timer_label.config(text=f"Alarm set at {alarm_text}.")
timeNow = datetime.now(country).strftime("%H:%M:%S")
time_label = tk.Label(text=f"Time {timeNow}", font=("Arial", 48))
time_label.pack(pady="5", anchor="center")
alarm_entry = tk.Entry()
alarm_entry.pack(pady="5",anchor="center")
submit_button = tk.Button(text="Submit", command=updateLabel)
submit_button.pack(pady="5",anchor="center")
timer_label = tk.Label()
timer_label.pack(pady="5",anchor="center")
updateTime()
window.mainloop()