from threading import Thread
from tkinter import *
from tkinter.ttk import Combobox

from PIL import ImageTk, Image

from datetime import datetime
from pygame import mixer
from time import sleep

# use PIL module to load the image icon

# colors
bg_color = '#ffffff'
color1 = '#566FC6'

# Create an instance of tkinter frame or window
window = Tk()

# Set the size of the window, tittle and color
window.geometry("450x250")
window.configure(bg=bg_color)
window.title("Alarm Clock")

# frames
frame_line = Frame(window, width=500, height=5, bg=color1)
frame_line.grid(row=0, column=0)

# Configuring frame body;
frame_body = Frame(window, width=450, height=300, bg=bg_color)
frame_body.grid(row=1, column=0)

# loading and Configuring the image;
img = Image.open('AlarmIcon.png')
img.resize((300, 300))
img = ImageTk.PhotoImage(img)

# load the image into the tkinter window
app_image = Label(frame_body, height=150, image=img, bg=bg_color)
app_image.place(x=1, y=10)

name = Label(frame_body, text='Alarm', height=1, font='ivy 18 bold', bg=bg_color)
name.place(x=125, y=10)

# hour label
hour = Label(frame_body, text='hour', height=1, font='ivy 10 bold', bg=bg_color, fg=color1)
hour.place(x=127, y=60)

# hour combobox
c_hour = Combobox(frame_body, width=2, font='arial 15')
c_hour['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
c_hour.current(0)
c_hour.place(x=126, y=79)

# minute label
min_time = Label(frame_body, text='min', height=1, font='ivy 10 bold', bg=bg_color, fg=color1)
min_time.place(x=197, y=60)

# minute combobox
c_min = Combobox(frame_body, width=2, font='arial 15')
c_min['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                   '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
                   '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                   '51', '52', '53', '54', '55', '56', '57', '58', '59')
c_min.current(0)
c_min.place(x=195, y=79)

# seconds label
sec_time = Label(frame_body, text='sec', height=1, font='ivy 10 bold', bg=bg_color, fg=color1)
sec_time.place(x=260, y=60)

# seconds combobox
c_sec = Combobox(frame_body, width=2, font='arial 15')
c_sec['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                   '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
                   '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                   '51', '52', '53', '54', '55', '56', '57', '58', '59')
c_sec.current(0)
c_sec.place(x=260, y=79)

period = Label(frame_body, text='period', height=1, font='ivy 10 bold', bg=bg_color, fg=color1)
period.place(x=330, y=60)

c_period = Combobox(frame_body, width=3, font='arial 15')
c_period['values'] = ('AM', 'PM')
c_period.current(0)
c_period.place(x=325, y=79)


# LOGI

def activate_alarm():
    t = Thread(target=alarm)
    t.start()


def deactivate_alarm():
    print('Deactivate alarm: ', selected.get())
    mixer.music.stop()


# Radio button for activate
selected = IntVar()

rad1 = Radiobutton(frame_body, font='arial 10 bold', value=1, text='Activate', bg=bg_color, command=activate_alarm,
                   variable=selected)
rad1.place(x=125, y=115)


def alarm_sound():
    mixer.music.load('alarmSound.mp3')
    mixer.music.play()
    selected.set(0)
    # Radio button for deactivate
    rad2 = Radiobutton(frame_body, font='arial 10 bold', value=2, text='Deactivate', bg=bg_color,
                       command=deactivate_alarm,
                       variable=selected)
    rad2.place(x=187, y=115)


def alarm():
    while True:
        control = selected.get()
        print(control)

        alarm_hour = c_hour.get()
        alarm_minute = c_min.get()
        alarm_second = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour_input = now.strftime('%I')
        minute_input = now.strftime('%M')
        second_input = now.strftime('%S')
        period_input = now.strftime('%p')

        if control == 1:
            if alarm_period == period_input:
                if alarm_hour == hour_input:
                    if alarm_minute == minute_input:
                        if alarm_second == second_input:
                            print('Time to take a break')
                            alarm_sound()

        sleep(1)


mixer.init()

window.mainloop()
