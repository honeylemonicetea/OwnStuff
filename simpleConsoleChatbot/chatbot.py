"""
CHECKLIST
1. Time and weekday - DONE
2. Weather status - DONE
3. Joking - DONE
4. Todo: Chatting - Sentiment analysis
"""


# ALL THE IMPORTS HERE
from CCB.chat_bot_class import ConsoleChatBot, User
import random
import time
from bs4 import BeautifulSoup
import requests as req

# CHAT BOT CREATION
chat_bot = ConsoleChatBot()
topic_list = ["your day", "shadows in the alley", "that new movie", "colors of the night sky", "torn jeans", "bubblegum"]
reactions = {"positive": ["That's nice", "Lovely!", "Yay!"], "negative": ["Oh, that's bad", "Ugh"], "neutral": ["Got it", "K"]}
weekdays = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}


# can add menu
def main_menu():
    print("(*/ω＼*)Main Menu╰(*°▽°*)╯")
    print("""1. Change my name
2. Talk about life.
3. Tell about the weather.
4. Tell a joke
5. Tell a story
    """)


def change_name():
    new_name = input("Give me a nice name")
    chat_bot.name = new_name
    print(f"Now my name is {chat_bot.name}")


def life_chat():
    # use NLP to assess the statement sentiment and choose a response
    while True:
        topic = random.choice(topic_list)
        print(f"So tell me about {topic}")
        user_entry = input("Write it here...")


# functions for weather and time info
def set_time_data():  #WORKS
    full_time = time.localtime()
    hour = full_time.tm_hour
    weekday_number = full_time.tm_wday
    time_of_d = ""
    #TIME
    if 0 <= hour <= 6 or 22<= hour:
        time_of_d = "night"
    elif 7<= hour <= 11:
        time_of_d = "morning"
    elif 12 <= hour <= 16:
        time_of_d = "day"
    else:
        time_of_d = "evening"
    #WEEKDAY
    weekday = weekdays.get(weekday_number)
    return time_of_d, weekday
def set_weather_data():
    weather_page = req.get(
        "https://weather.com/en-KN/weather/today/l/ecf0ce04af6f721cec1964ac4d797bc985953dff9b2f775037ac082cfe06d8f4")
    soup = BeautifulSoup(weather_page.text, "lxml")
    temps_ = soup.find("span", {"class": "CurrentConditions--tempValue--3KcTQ"})
    wec = soup.find("div",{"class":"CurrentConditions--phraseValue--2xXSr"})
    current_temp = temps_.text
    current_condition = wec.text
    return current_temp, current_condition
def weather():
    # use bs to get the weather data and time module to get time
    time_, weeday = set_time_data()
    temp, condi = set_weather_data()
    print(f"Good {time_}, it's a lovely {weeday} {time_}! It's {temp}C outside, the current weather condition is: {condi}")

def joke():
    with open("jokesa.txt") as jokelist:
        jokes = jokelist.read()
    jokes = jokes.split("\n")
    a_joke = random.choice(jokes)
    print(f"So here's the joke:\n{a_joke}")

# first print a greeting for the user and ask them if they want to name the chatbot and provide their own name and for of address
print(f"Hello, my name is {chat_bot.name}, I am honored to serve you, Stranger")
user_name = input("Please input your name: ")
user_add = input("Which form of address do you prefer? ")
current_user = User(user_name, user_add)
print(f"Hello, {current_user.address}. {current_user.user_name}")
while True:
    main_menu()
    option = input("Please input the option number: ")
    if option == "1":
        change_name()
    elif option == "2":
        life_chat()
    elif option == "3": #weather!
        weather()
    elif option == "4": #joke
        joke()
    ask = input("Wanna continue?(input no to exit)")
    if ask.lower() == "no":
        break

# the bot must be able to have conversations on various topics and help the user do simple tasks


# nltk !!!
