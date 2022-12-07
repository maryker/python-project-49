import prompt

def welcome_user():
    '''Asks user's name and welcomes him'''
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')