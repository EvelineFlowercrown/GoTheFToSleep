import tkinter as tk
from playsound import playsound
import subprocess
import threading
from PIL import Image, ImageTk
from os import system


class ToggleButton(tk.Button):
    def __init__(self, parent, image_on, image_off, command=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.image_on = ImageTk.PhotoImage(Image.open(image_on))
        self.image_off = ImageTk.PhotoImage(Image.open(image_off))

        self.state = False
        self.command = command
        self.config(image=self.image_off, width=40, height=40)
        self.bind("<Button-1>", self.toggle)

    def toggle(self, event):
        self.state = not self.state
        if self.state:
            self.config(image=self.image_on)
        else:
            self.config(image=self.image_off)
        if self.command:
            self.command()


class Countdown:
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x400')
        self.master.title('Go the fuck to sleep')
        self.minutes = 0
        self.seconds = 0
        self.isMuted = True
        self.running = False
        self.create_widgets()

    def create_widgets(self):
        # Countdown timer label
        self.time_label = tk.Label(self.master, text='00:00:00', font=('Arial', 40))
        self.time_label.place(relx=0.5, rely=0.1, anchor='center')

        # Stop button
        self.stop_button = tk.Button(self.master, text='Stop', font=('Arial', 20), command=self.stop_countdown)
        self.stop_button.place(relx=0.9, rely=0.4, anchor='center')

        # Add 15 minutes button
        self.snooze_button = tk.Button(self.master, text='+15', font=('Arial', 20), command=self.add_15_minutes)
        self.snooze_button.place(relx=0.1, rely=0.4, anchor='center')

        # Add mute button
        self.toggle_btn = ToggleButton(root, "Icons/on.png", "Icons/off.png", command=self.mute)
        self.toggle_btn.place(relx=0.5, rely=0.4, anchor='center')

        # Timer selection buttons
        times = [('4 hours', 240), ('3 hours', 180), ('2 hours', 120), ('1 hour', 60), ('45 minutes', 45), ('30 minutes', 30)]
        for i, (text, mins) in enumerate(times):
            btn = tk.Button(self.master, text=text, font=('Arial', 14),
                            command=lambda mins=mins: self.start_countdown(mins))
            btn.place(relx=0.2 + i % 3 * 0.3, rely=0.7 + int(i / 3) * 0.15, anchor='center')

    def mute(self):
        self.isMuted = not self.isMuted
        if self.isMuted:
            print("muted")
        else:
            print("unmuted")

    def start_countdown(self, mins):
        self.minutes = mins
        self.seconds = 0
        self.update_time_label()
        self.running = True
        thread = threading.Thread(target=self.run_countdown)
        thread.start()

    def run_countdown(self):
        while self.running and (self.minutes > 0 or self.seconds > 0):
            if self.seconds == 0:
                self.seconds = 59
                self.minutes -= 1
            else:
                self.seconds -= 1
            self.update_time_label()
            if not self.isMuted:
                self.audioReminder()

            if self.minutes == 0 and self.seconds == 0:
                self.shutdown()
            else:
                pass
            threading.Event().wait(1)

    def audioReminder(self):
        if self.minutes == 30 and self.seconds == 1:
            playsound('sounds/30.wav', False)
        if self.minutes == 15 and self.seconds == 1:
            playsound('sounds/15.wav', False)
        if self.minutes == 5 and self.seconds == 0:
            playsound('sounds/5.wav', False)
        if self.minutes == 0 and self.seconds == 10:
            playsound('sounds/countdown.wav', False)

    def update_time_label(self):
        hours = str(self.minutes // 60).zfill(2)
        mins = str(self.minutes % 60).zfill(2)
        secs = str(self.seconds).zfill(2)
        self.time_label.config(text=f'{hours}:{mins}:{secs}')

    def stop_countdown(self):
        self.running = False
        self.master.destroy()

    def add_15_minutes(self):
        self.minutes += 15
        self.update_time_label()

    def shutdown(self):
        system("shutdown /s /f")


if __name__ == '__main__':
    root = tk.Tk()
    countdown = Countdown(root)
    root.mainloop()
