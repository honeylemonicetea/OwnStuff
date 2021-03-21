"""
1. Create a simple shell UI DONE
2.  dark mode DONE
3. Make it work
===================
==               ==
==     BUTTONS   ==
==               ==
===================
CHANGE MY NAME --  WORKING
TALK ABOUT LIFE --  WORKING
TELL ABOUT WEATHER --  WORKING
TELL A JOKE -- WORKING
TELL A STORY --  WORKING
DARK MODE - WORKING
RESET NAME - WORKING


"""
#IMPORTS
import tkinter as tk
from resources.chat_bot_class import ConsoleChatBot, User
import time
from bs4 import BeautifulSoup
import requests as req
import random
import colorama
import json
#more reqs - lxml
from resources.chat_bot_class import ConsoleChatBot, User
import time
from bs4 import BeautifulSoup
import requests as req
import random
import json
from resources.connor_SentAn import Sentiment
from resources.sentence_resources import happy_responses, supportive_responses
import tkinter.messagebox as tkm
import time

# CHAT BOT CREATION
chat_bot = ConsoleChatBot()
topic_list = ["your day", "shadows in the alley", "that new movie", "colors of the night sky", "torn jeans",
              "bubblegum"]
reactions = {"positive": ["That's nice", "Lovely!", "Yay!"], "negative": ["Oh, that's bad", "Ugh"],
             "neutral": ["Got it", "K"]}
weekdays = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
current_user = User("", "")
current_action = ""



root = tk.Tk()
root.title('ChatBot')
root.geometry('550x500')
root.configure(bg='seagreen1')


#TECHNICAL FUNCTIONS
def write_data(user_name="", bot_name=""):
    with open("data.json") as data:
        h = json.load(data)
    if user_name != "":
        with open("data.json", "w") as file:
            h["userName"] = user_name
            json.dump(h, file)
    if bot_name != "":
        with open("data.json", "w") as file:
            h["botName"] = bot_name
            json.dump(h, file)
def get_name_data():
    with open("data.json") as data:
        h = json.load(data)
    user_name = h.get("userName")
    bot_name = h.get("botName")
    return user_name, bot_name
def reset_names():
    global  user
    if tkm.askyesno('Confirm Action','Are you sure you want to erase all name data?'):
        with open('data.json') as data:
            h = json.load(data)
        with open('data.json', 'w') as file:
            h['userName'] = ''
            h['botName'] = ''
            json.dump(h, file)
            chat_bot.name = 'Connor'
            user = ''
        tkm.showinfo('Done', 'All the name data have been erased')
def set_time_data():  # WORKS
    full_time = time.localtime()
    hour = full_time.tm_hour
    weekday_number = full_time.tm_wday
    time_of_d = ""
    # TIME
    if 0 <= hour <= 6 or 22 <= hour:
        time_of_d = "night"
    elif 7 <= hour <= 11:
        time_of_d = "morning"
    elif 12 <= hour <= 16:
        time_of_d = "day"
    else:
        time_of_d = "evening"
    # WEEKDAY
    weekday = weekdays.get(weekday_number)
    return time_of_d, weekday
def set_weather_data():
    weather_page = req.get(
        "https://weather.com/en-KN/weather/today/l/ecf0ce04af6f721cec1964ac4d797bc985953dff9b2f775037ac082cfe06d8f4")
    soup = BeautifulSoup(weather_page.text, "lxml")
    temps_ = soup.find("span", {"class": "CurrentConditions--tempValue--3KcTQ"})
    wec = soup.find("div", {"class": "CurrentConditions--phraseValue--2xXSr"})
    current_temp = temps_.text
    current_condition = wec.text
    return current_temp, current_condition







def option_selection(event):
    global current_action
    if current_action == 1:  #changing name
        output_field.delete(1.0, 'end')
        new_name = input_field.get()
        chat_bot.name = new_name
        write_data(bot_name=new_name)

        output_field.insert(1.0, f"{chat_bot.name}: Now my name is {chat_bot.name}")
        input_field.delete(0, 'end')
    if current_action == 2:
        output_field.delete(1.0, 'end')
        user_entry = input_field.get()
        processed_sentence = Sentiment(user_entry)
        processed_sentence.sentiment_analysis()
        score = processed_sentence.score
        if score >= 0:
            response = random.choice(happy_responses)
        else:
            response = random.choice(supportive_responses)

        output_field.insert(1.0, f'{chat_bot.name}: {response}')
        input_field.delete(0, 'end')
    if current_action == 3:
        time_, weeday = set_time_data()
        temp, condi = set_weather_data()
        output_field.insert(1.0, f"{chat_bot.name }: Good {time_}, it's a lovely {weeday} {time_}! It's {temp}C outside, the current weather "
            f"condition is: {condi}")
    if current_action == 10:
        user_name = input_field.get()
        current_user.user_name = user_name
        input_field.delete(0, 'end')
        write_data(user_name=current_user.user_name)
        output_field.delete(1.0, 'end')
        output_field.insert(1.0, f"Hello, {current_user.user_name}")




#FUNCTIONS  for Buttons

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

        reset_button['fg'] = 'white'
        reset_button['bg'] = 'gray30'

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
        reset_button['fg'] = 'black'
        reset_button['bg'] = 'lavender'

def change_name(event):
    global current_action
    output_field.delete(1.0, 'end')
    current_action = 1
    output_field.insert(1.0,f"{chat_bot.name}: Give me a nice name")

def life_talk(event):
    global current_action
    output_field.delete(1.0, 'end')
    print('life talk...ok')
    current_action = 2
    topic = random.choice(topic_list)
    output_field.insert(1.0, f"{chat_bot.name}: So tell me about {topic}" )

def weather_inf(event):
    global current_action
    output_field.delete(1.0, 'end')
    current_action = 3
    print('weather...ok')
    time_, weeday = set_time_data()
    temp, condi = set_weather_data()
    output_field.insert(1.0,f"{chat_bot.name}: Good {time_}, it's a lovely {weeday} {time_}! It's {temp}C outside, the current weather "
                        f"condition is: {condi}")

def joking(event):
    global current_action
    output_field.delete(1.0, 'end')
    current_action = 4
    print('jokes aside...ok')
    with open("resources/jokesa.txt") as jokelist:
        jokes = jokelist.read()
    jokes = jokes.split("\n")
    a_joke = random.choice(jokes)
    output_field.insert(1.0, f"{chat_bot.name}: So here's the joke:\n{a_joke}")

def mad_libs(event):
    global current_action
    output_field.delete(1.0, 'end')
    current_action = 5
    print('mad mad libs... ok')
    people = ["mum", "dad", "sister", "brother", "Anne", "Marie", "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava",
              "William", "Sophia", "Elijah", "Isabella", "James", "Charlotte", "Benjamin", "Amelia", "Lucas", "Mia",
              "Mason", "Harper", "Ethan", "Evelyn"]
    adjectives = ["adorable", "adventurous", "aggressive", "agreeable", "alert", "alive", "amused", "angry", "annoying",
                  "anxious", "arrogant", "ashamed", "attractive", "average", "awful", "bad", "beautiful", "better",
                  "bewildered", "black", "bloody", "blue", "blue-eyed", "blushing", "bored", "brainy", "brave",
                  "breakable", "bright", "busy", "calm", "careful", "cautious", 'charming', "cheerful", "clean",
                  "clear", "clever", "cloudy", "clumsy", "colorful", "combative", "comfortable", "concerned",
                  "condemned", "confused", "cooperative", "courageous", "crazy", "creepy", "crowded", "cruel",
                  "curious", "cute", "dangerous",
                  "dark", "defeated", "defiant", "delightful", "depressed", "determined", "different", "difficult",
                  "disgusted",
                  "distinct", "disturbed", "dizzy", "doubtful", "drab", "dull"]
    verbs = ["beat", "become", "begin", "bend", "bite", "bleed", "break", "bring", "broadcast", "build", "burn",
             "burst",
             "buy", "can", "cast", "catch"]
    adverbs = ["boldly", "bravely", "brightly", "cheerfully", "deftly", "devotedly", "eagerly", "elegantly",
               "faithfully",
               "fortunately", "gleefully", "gracefully", "happily", "honestly", "innocently", "justly", "kindly",
               "merrily",
               "obediently", "perfectly", "politely", "powerfully", "safely", "victoriously", "warmly"]
    nouns = ["time", "way", "thing", "life",
             "world", "school", "family", "student", "group", "country", "problem", "hand", "place", "home", "water",
             "room", "fact", "month", "game",
             "line", "end", "member", "law", "car", "city", "community", "name", "parent", "face", "others", "level",
             "office", "door", "health",
             "person", "party", "result", "reason", "teacher"]
    output_field.insert(1.0, f"""{chat_bot.name}:
       Dear {user},
    I am having a(n) {random.choice(adjectives)} time at camp. The counselour is {random.choice(adjectives)} and the food is {random.choice(adjectives)}.
    I met {random.choice(adjectives)} and we became {random.choice(adjectives)} friends. Unfortunately, {random.choice(people)} is {random.choice(adjectives)} and I {random.choice(verbs)} my {random.choice(nouns)} so we couldn`t
    go {random.choice(verbs)} like everybody else. I need more {random.choice(nouns)} and a {random.choice(nouns)} sharpener, so please {random.choice(adverbs)} {random.choice(verbs)} more when you {random.choice(verbs)} back.
    Your bot,
    {chat_bot.name}
        """)



#BUTTONS AND LABELS
menu_label = tk.Label(root, text = '  */ω＼*)Main Menu╰(*°▽°*)╯', font=('Century Gothic', 20, 'normal'), bg='seagreen1')
menu_label.grid(row=1, column=1)

#DARK MODE

dark_mode_btn = tk.Button(root, text='DARK MODE🌙', command=dark_md, bg='gray16', fg='white', font=('Arial', 7,'bold'))
dark_mode_btn.grid(sticky='NE', padx=20, pady=10)

reset_button = tk.Button(root, text='RESET NAME', bg='lavender', font=('Arial', 7,'bold'), command=reset_names)
reset_button.grid(sticky='NE', padx=20, pady=10)

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

output_field = tk.Text(root, width=40, heigh=4, font=('Century Gothic', 10, 'normal'), bg = 'lavender')
output_field.grid(row=7, column=1,  pady=5)

#disabled unless user input is required
input_field = tk.Entry(root, width=40,font=('Century Gothic', 10, 'normal'), bg = 'lavender')
input_field.grid(row=9, column=1, pady=10)
input_field.focus_set()

send_btn = tk.Button(root, text='Send',width = 20, bg='lavender',font=('Century Gothic', 10, 'normal'), command=lambda e='<Return>':option_selection(e))
send_btn.grid(row=10, column=1, padx=5, pady= 5)

root.bind('<Return>', option_selection)



def greeting_new():
    global current_action
    output_field.insert(1.0, f"{chat_bot.name}: Hello, my name is {chat_bot.name}, I am honored to serve you, Stranger. Please input your name:")
    current_action = 10


def greeting_seasoned(user_name, bot_name="ChatBot"):
    output_field.delete(1.0, 'end')
    current_user.user_name = user_name
    chat_bot.name = bot_name
    output_field.insert(1.0, f"{chat_bot.name}: Hey, {current_user.user_name}, it's nice to see ya! Pick an option")
user, bot = get_name_data()
print(user)
print(bot)
if user == "" and bot == "Connor":
    greeting_new()
elif user != "" and bot != "":
    greeting_seasoned(user, bot)
elif user != "" and bot == "":
    greeting_seasoned(user)
else:
    greeting_new()


root.mainloop()