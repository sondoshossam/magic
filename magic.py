import random

answers =

print('  __  __          _____ _____ _____   ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____| /   \ ')
print(' | \  / |  /  \ | |  __  | || |     |     |')
print(' | |\/| | / /\ \| | |_ | | || |     |     |')
print(' | |  | |/ ____ \ |__| |_| || |____ |     |')
print(' |_|  |_/_/    \_\_____|_____\_____| \___/ ')
print('')

print('Hello World, I am the Magic 8 Ball, What is your name?')
name = input()
print('hello ' + name)



def Magic0():
    print('Ask me a question.')
    input()
    print(answers[random.randint(0, len(answers) - 1)])
    print('I hope that helped!')
    Replay()


def Replay():
    print('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'Y':
        Magic0()()
    elif reply == 'N':
        exit()
    else:
        print('I apologies, I did not catch that. Please repeat.')
        Replay()


Magic0()

