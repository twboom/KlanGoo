import json
import random
klangoo = {}

with open('intents.json', 'r') as myIntents:
    klangoo['intents'] = json.load(myIntents)

with open('responses.json', 'r') as myResponses:
    klangoo['responses'] = json.load(myResponses)

def confusion():
    return random.choice(klangoo['responses']['confused'])

def get_intent(question):
    intents = list(klangoo['intents'])
    words = question.split(' ')
    probability = {}
    for intent in intents:
        matches = list(set(klangoo['intents'][intent]).intersection(words))
        probability[intent] = len(matches)
    intent = max(probability, key=probability.get)
    return intent

def ask(question):
    answer = []
    ansWordCount = random.randint(3, 9)
    intents = klangoo['intents']
    responses = klangoo['responses']
    if question == '': return confusion()
    intent = get_intent(question)

    print (intent)

    return ''

    words = question.split(' ')
    wordList = []
    for key in responses:
        for i, word in enumerate(responses[key]):
            wordList.append(word)
    
    for i in range(ansWordCount):
        thisWord = random.choice(wordList)
        answer.append(thisWord)
        answer.append('')


    output = ''
    for word in answer:
        output += word + ' '

    return output