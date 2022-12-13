import prompt
from random import randint


def game_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        rand_num = randint(1, 100)
        print(f'Question: {rand_num}')
        answr = input('Your answer: ')
        answers = ('yes', 'no')
        cor_answr = answers[rand_num % 2]
        if answr == cor_answr:
            print('Correct!')
            count += 1
        else:
            print(f"'{answr}' is wrong answer ;(. ",
                  f"Correct answer was '{cor_answr}'")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    game_even()


if __name__ == '__main__':
    main()
