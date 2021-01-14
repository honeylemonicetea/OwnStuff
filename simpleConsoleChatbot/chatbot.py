"""
CHECKLIST
1. Time and weekday - DONE
2. Weather status - DONE
3. Joking - DONE
4. Todo: Chatting - Sentiment analysis
"""

# ALL THE IMPORTS HERE

from resources.chat_bot_class import ConsoleChatBot, User
import time
from bs4 import BeautifulSoup
import requests as req
import random

# CHAT BOT CREATION
chat_bot = ConsoleChatBot()
topic_list = ["your day", "shadows in the alley", "that new movie", "colors of the night sky", "torn jeans",
              "bubblegum"]
reactions = {"positive": ["That's nice", "Lovely!", "Yay!"], "negative": ["Oh, that's bad", "Ugh"],
             "neutral": ["Got it", "K"]}
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
    new_name = input(f"{chat_bot.name}: Give me a nice name")
    chat_bot.name = new_name
    print(f"{chat_bot.name}: Now my name is {chat_bot.name}")


def life_chat():
    # use NLP to assess the statement sentiment and choose a response
    while True:
        topic = random.choice(topic_list)
        print(f"{chat_bot.name}: So tell me about {topic}, type \"no\" to exit")
        user_entry = input(f"{chat_bot.name}: Write it here...")
        if user_entry.lower() == "no":
            break


# functions for weather and time info
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


def weather():
    # use bs to get the weather data and time module to get time
    time_, weeday = set_time_data()
    temp, condi = set_weather_data()
    print(f"{chat_bot.name}: Good {time_}, it's a lovely {weeday} {time_}! It's {temp}C outside, the current weather "
          f"condition is: {condi}")


def joke():
    with open("resources/jokesa.txt") as jokelist:
        jokes = jokelist.read()
    jokes = jokes.split("\n")
    a_joke = random.choice(jokes)
    print(f"{chat_bot.name}: So here's the joke:\n{a_joke}")


def story_tell(user):
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
    print(f"""{chat_bot.name}:
   Dear {user},
I am having a(n) {random.choice(adjectives)} time at camp. The counselour is {random.choice(adjectives)} and the food is {random.choice(adjectives)}.
I met {random.choice(adjectives)} and we became {random.choice(adjectives)} friends. Unfortunately, {random.choice(people)} is {random.choice(adjectives)} and I {random.choice(verbs)} my {random.choice(nouns)} so we couldn`t
go {random.choice(verbs)} like everybody else. I need more {random.choice(nouns)} and a {random.choice(nouns)} sharpener, so please {random.choice(adverbs)} {random.choice(verbs)} more when you {random.choice(verbs)} back.
Your bot,
{chat_bot.name}
    """)


# first print a greeting for the user and ask them if they want to name the chatbot and provide their own name and for of address
print(f"{chat_bot.name}: Hello, my name is {chat_bot.name}, I am honored to serve you, Stranger")
user_name = input(f"{chat_bot.name}: Please input your name: ")
user_add = input(f"{chat_bot.name}: Which form of address do you prefer? ")
current_user = User(user_name, user_add)
print(f"Hello, {current_user.address}. {current_user.user_name}")
while True:
    main_menu()
    option = input(f"{chat_bot.name}: Please input the option number: ")
    if option == "1":
        change_name()
    elif option == "2":
        life_chat()
    elif option == "3":  # weather!
        weather()
    elif option == "4":  # joke
        joke()
    elif option == "5":  # tell a story
        story_tell(user_name)
    ask = input(f"{chat_bot.name}: Wanna continue?(input no to exit)")
    if ask.lower() == "no":
        break

# the bot must be able to have conversations on various topics and help the user do simple tasks


# nltk !!!
