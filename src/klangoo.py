import json
klangoo = {}

with open('intents.json', 'r') as intents:
    klangoo[intents] = json.load(intents)

with open('responses.json', 'r') as responses:
    klangoo[responses] = json.load(responses)

def ask(question):
    
    answer = 'Hello'
    return answer

print(klangoo)