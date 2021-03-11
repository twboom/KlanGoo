import json
import random
klangoo = {}

with open('intents.json', 'r') as myIntents:
    klangoo['intents'] = json.load(myIntents)

def confusion():
    return random.choice(klangoo['intents']['self_confused']['responses'])

def get_intent(question):
    intents = list(klangoo['intents'])
    unclean_words = ''.join(filter(str.isalpha, question))
    words = unclean_words.split(' ')
    print(words)
    probability = {}
    for intent in intents:
        matches = list(set(klangoo['intents'][intent]).intersection(words))
        probability[intent] = len(matches)
    intent = max(probability, key=probability.get)
    print(probability)
    if probability[intent] == 0: return 'confusion'
    return intent

def ask(question):
    intent = get_intent(question)
    print (intent)
    if intent == 'confusion': return confusion()
    return ''