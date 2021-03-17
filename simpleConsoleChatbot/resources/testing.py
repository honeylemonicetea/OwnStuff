import json

with open('test1.json') as data:
    h = json.load(data)
with open('test1.json', 'w') as file:
    h['userName'] = ''
    h['botName'] = ''
    json.dump(h, file)