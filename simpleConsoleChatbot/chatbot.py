"""
CHECKLIST
1. Time and weekday - DONE
2. Weather status - DONE
3. Joking - DONE
4. TODO: Chatting - Sentiment analysis
5. TODO: MULTI LANGUAGE SUPPORT
"""

# ALL THE IMPORTS HERE

from resources.chat_bot_class import ConsoleChatBot, User
import time
from bs4 import BeautifulSoup
import requests as req
import random
import colorama
import json

# CHAT BOT CREATION
chat_bot = ConsoleChatBot()
topic_list = ["your day", "shadows in the alley", "that new movie", "colors of the night sky", "torn jeans",
              "bubblegum"]
reactions = {"positive": ["That's nice", "Lovely!", "Yay!"], "negative": ["Oh, that's bad", "Ugh"],
             "neutral": ["Got it", "K"]}
weekdays = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
current_user = User("", "")


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
def main_menu():
    print(colorama.Fore.LIGHTCYAN_EX+colorama.Style.BRIGHT+"(*/ω＼*)Main Menu╰(*°▽°*)╯"+colorama.Style.RESET_ALL)
    print(colorama.Fore.LIGHTMAGENTA_EX+colorama.Style.BRIGHT+"1. Change my name"+colorama.Style.RESET_ALL)
    print(colorama.Fore.LIGHTBLUE_EX+colorama.Style.BRIGHT+"2. Talk about life."+colorama.Style.RESET_ALL)
    print(colorama.Fore.LIGHTGREEN_EX+colorama.Style.BRIGHT+"3. Tell about the weather."+colorama.Style.RESET_ALL)
    print(colorama.Fore.LIGHTRED_EX+colorama.Style.BRIGHT+"4. Tell a joke"+colorama.Style.RESET_ALL)
    print(colorama.Fore.WHITE+colorama.Style.BRIGHT+"5. Tell a story"+colorama.Style.RESET_ALL)
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

#outputting funcs
def change_name():
    new_name = input(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: Give me a nice name")
    chat_bot.name = new_name
    write_data(bot_name=new_name)
    print(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: Now my name is {chat_bot.name}")
def life_chat():
    # use NLP to assess the statement sentiment and choose a response
    while True:
        topic = random.choice(topic_list)
        print(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: So tell me about {topic}, type \"no\" to exit")
        user_entry = input(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: Write it here...")
        if user_entry.lower() == "no":
            break
def weather():
    # use bs to get the weather data and time module to get time
    time_, weeday = set_time_data()
    temp, condi = set_weather_data()
    print(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: Good {time_}, it's a lovely {weeday} {time_}! It's {temp}C outside, the current weather "
          f"condition is: {condi}")
def joke():
    with open("resources/jokesa.txt") as jokelist:
        jokes = jokelist.read()
    jokes = jokes.split("\n")
    a_joke = random.choice(jokes)
    print(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: So here's the joke:\n{a_joke}")
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
    print(f"""{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}:
   Dear {user},
I am having a(n) {random.choice(adjectives)} time at camp. The counselour is {random.choice(adjectives)} and the food is {random.choice(adjectives)}.
I met {random.choice(adjectives)} and we became {random.choice(adjectives)} friends. Unfortunately, {random.choice(people)} is {random.choice(adjectives)} and I {random.choice(verbs)} my {random.choice(nouns)} so we couldn`t
go {random.choice(verbs)} like everybody else. I need more {random.choice(nouns)} and a {random.choice(nouns)} sharpener, so please {random.choice(adverbs)} {random.choice(verbs)} more when you {random.choice(verbs)} back.
Your bot,
{chat_bot.name}
    """)

#If there is a user name in the json file, use it instead of asking name
# first print a greeting for the user and ask them if they want to name the chatbot and provide their own name and for of address

def greeting_new():
    print(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: Hello, my name is {chat_bot.name}, I am honored to serve you, Stranger")
    user_name = input(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: Please input your name: ")
    user_add = input(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: Which form of address do you prefer? ")
    current_user.user_name = user_name
    current_user.address = user_add
    write_data(user_name=current_user.user_name)
    print(f"Hello, {current_user.address}. {current_user.user_name}")

def greeting_seasoned(user_name, bot_name="ChatBot"):
    current_user.user_name = user_name
    chat_bot.name = bot_name
    print(f"{chat_bot.name}: Hey, {current_user.user_name}, it's nice to see ya! Pick a number")

while True:
    user, bot = get_name_data()
    if user == "" and bot == "":
        greeting_new()
    elif user != "" and bot != "":
        greeting_seasoned(user, bot)
    elif user != "" and bot == "":
        greeting_seasoned(user)
    else:
        greeting_new()
    main_menu()
    option = input(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: Please input the option number: ")
    if option == "1":
        change_name()
    elif option == "2":
        life_chat()
    elif option == "3":  # weather!
        weather()
    elif option == "4":  # joke
        joke()
    elif option == "5":  # tell a story
        story_tell(current_user.user_name)
    ask = input(f"{colorama.Fore.CYAN+chat_bot.name+colorama.Style.RESET_ALL}: Wanna continue?(input no to exit)")
    if ask.lower() == "no":
        break

# the bot must be able to have conversations on various topics and help the user do simple tasks


# nltk !!!
