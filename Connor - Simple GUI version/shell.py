"""
1. Create a simple shell UI DONE
2.  dark mode DONE
3. Make it work
"""

import tkinter as tk
from resources.chat_bot_class import ConsoleChatBot, User
import time
from bs4 import BeautifulSoup
import requests as req
import random
import colorama
import json
#more reqs - lxml






root = tk.Tk()
root.title('ChatBot')
root.geometry('550x500')
root.configure(bg='seagreen1')

#FUNCTIONS

def dark_md():
    if root['bg'] == 'seagreen1':
        root['bg'] = 'gray16'
        menu_label['bg'] = 'gray16'
        menu_label['fg'] = 'white'
        dark_mode_btn['bg'] = 'white'
        dark_mode_btn['fg'] = 'black'
        dark_mode_btn['text'] = 'LIGHT MODE🌞'
        #BUTTONS
        name_btn ['fg'] =  'white'
        name_btn['bg'] = 'gray25'
        life_btn['fg'] = 'white'
        life_btn['bg'] = 'gray25'
        weather_btn['fg'] = 'white'
        joke_btn['fg'] = 'white'
        mad_libs_btn['fg'] = 'white'
        send_btn['fg'] = 'white'
        weather_btn['bg'] = 'gray25'
        joke_btn['bg'] = 'gray25'
        mad_libs_btn['bg'] = 'gray25'
        send_btn['bg'] = 'gray25'


        input_label['fg'] = 'white'
        input_label['bg'] = 'gray16'

        input_field['bg'] = 'gray30'
        input_field['fg'] = 'white'
        output_field['bg'] = 'gray30'
        output_field['fg'] = 'white'

    else:
        root['bg'] = 'seagreen1'
        menu_label['bg'] = 'seagreen1'
        menu_label['fg'] = 'black'
        dark_mode_btn['bg'] = 'gray16'
        dark_mode_btn['fg'] = 'WHITE'
        dark_mode_btn['text'] = 'DARK MODE🌙'

        # BUTTONS
        name_btn['fg'] = 'black'
        name_btn['bg'] = 'lavender'
        life_btn['fg'] = 'black'
        life_btn['bg'] = 'lavender'
        weather_btn['fg'] = 'black'
        joke_btn['fg'] = 'black'
        mad_libs_btn['fg'] = 'black'
        send_btn['fg'] = 'black'
        weather_btn['bg'] = 'lavender'
        joke_btn['bg'] = 'lavender'
        mad_libs_btn['bg'] = 'lavender'
        send_btn['bg'] = 'lavender'

        input_label['fg'] = 'black'
        input_label['bg'] = 'seagreen1'

        input_field['bg'] = 'lavender'
        input_field['fg'] = 'black'
        output_field['bg'] = 'lavender'
        output_field['fg'] = 'black'


def change_name(event):
    print('change name...ok')

def life_talk(event):
    print('life talk...ok')

def weather_inf(event):
    print('weather...ok')

def joking(event):
    print('jokes aside...ok')

def mad_libs(event):
    print('mad mad libs... ok')



#BUTTONS AND LABELS
menu_label = tk.Label(root, text = '  */ω＼*)Main Menu╰(*°▽°*)╯', font=('Century Gothic', 20, 'normal'), bg='seagreen1')
menu_label.grid(row=1, column=1)

#DARK MODE

dark_mode_btn = tk.Button(root, text='DARK MODE🌙', command=dark_md, bg='gray16', fg='white', font=('Arial', 7,'bold'))
dark_mode_btn.grid(sticky='NE', padx=20, pady=10)

name_btn = tk.Button(root, text='1. Change my name', width = 20, bg='lavender',font=('Century Gothic', 10, 'normal'), command=lambda e='1':change_name(e))
name_btn.grid(row=2, column=1, pady=5)

life_btn = tk.Button(root, text='2. Talk about life',width = 20, bg='lavender',font=('Century Gothic', 10, 'normal'),command=lambda e='2':life_talk(e))
life_btn.grid(row=3, column=1,pady=5)

weather_btn = tk.Button(root, text='3. Tell about the weather',width = 20, bg='lavender',font=('Century Gothic', 10, 'normal'), command=lambda e='3':weather_inf(e))
weather_btn.grid(row=4, column=1,  pady=5)

joke_btn = tk.Button(root, text='4. Tell a joke',width = 20, bg='lavender',font=('Century Gothic', 10, 'normal'), command=lambda e='4':joking(e))
joke_btn.grid(row=5, column=1, pady=5)

mad_libs_btn = tk.Button(root,  text='5. Tell a story',width = 20, bg='lavender',font=('Century Gothic', 10, 'normal'), command=lambda e='5':mad_libs(e))
mad_libs_btn.grid(row=6, column=1, pady=5)

input_label = tk.Label(root, text='Write something here', bg='seagreen1')
input_label.grid(row=8, column=1, pady=10)


#KEY BINDINGS
root.bind('1', change_name)
root.bind('2',life_talk)
root.bind('3', weather_inf)
root.bind('4', joking)
root.bind('5', mad_libs)




#FIELDS

output_field = tk.Text(root, width=40, heigh=4, font=('Century Gothic', 10, 'normal'), state=tk.DISABLED, bg = 'lavender')
output_field.grid(row=7, column=1,  pady=5)

#disabled unless user input is required
input_field = tk.Entry(root, width=40,font=('Century Gothic', 10, 'normal'), bg = 'lavender', state=tk.DISABLED)
input_field.grid(row=9, column=1, pady=10)
input_field.focus_set()

send_btn = tk.Button(root, text='Send',width = 20, bg='lavender',font=('Century Gothic', 10, 'normal'))
send_btn.grid(row=10, column=1, padx=5, pady= 5)

root.mainloop()