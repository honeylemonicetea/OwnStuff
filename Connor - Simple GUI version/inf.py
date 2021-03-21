import json

with open("data_reserve.json") as data:
    h = json.load(data)


with open("data_reserve.json", "w") as file:
    h["userName"] = "Bella"
    print(h)
    json.dump(h, file)