class ConsoleChatBot:
    def __init__(self, name="ChatBot"):
        self.name = name

    def greeting(self):
        greeting_neutral = f"Hello, my name is {self.name}"


class User:
    def __init__(self, user_name, address):
        self.user_name = user_name
        self.address = address
