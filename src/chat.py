import klangoo as kg
import os

os.system('cls' if os.name == 'nt' else 'clear')

def run():
    question = input('> ')
    answer = kg.ask(question)
    print(str(answer))
    run()

print('Hello!')

run()