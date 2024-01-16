from tkinter import *
from tkinter import ttk
import datetime
import time
import winsound
from threading import Thread

def threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_label.config(text=f"Current Time: {current_time}")

        if current_time == set_alarm_time:
            alarm_label.config(text="Time to Wake up", fg="red")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        else:
            alarm_label.config(text="")

root = Tk()
root.geometry("400x250")
root.title("Modern Alarm Clock")

main_label = Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red")
main_label.pack(pady=10)

frame = Frame(root)
frame.pack()

current_label = Label(frame, text="Current Time: ", font=("Helvetica", 12))
current_label.grid(row=0, column=0, columnspan=3, pady=10)

hour = StringVar(root)
hours = [str(i).zfill(2) for i in range(25)]
hour.set(hours[0])

hrs = ttk.Combobox(frame, textvariable=hour, values=hours, state="readonly")
hrs.grid(row=1, column=0, padx=5)

minute = StringVar(root)
minutes = [str(i).zfill(2) for i in range(61)]
minute.set(minutes[0])

mins = ttk.Combobox(frame, textvariable=minute, values=minutes, state="readonly")
mins.grid(row=1, column=1, padx=5)

second = StringVar(root)
seconds = [str(i).zfill(2) for i in range(61)]
second.set(seconds[0])

secs = ttk.Combobox(frame, textvariable=second, values=seconds, state="readonly")
secs.grid(row=1, column=2, padx=5)

alarm_label = Label(root, text="", font=("Helvetica", 14, "bold"))
alarm_label.pack(pady=10)

set_button = Button(root, text="Set Alarm", font=("Helvetica", 15), command=threading)
set_button.pack(pady=20)

root.mainloop()
