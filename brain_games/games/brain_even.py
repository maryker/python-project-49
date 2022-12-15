from random import randint
from brain_games.scripts.game_script import greet_user, check_answer, congrats


def game_even():
    name = greet_user()
    count = 0
    while count != 3:
        rand_num = randint(1, 100)
        print(f'Question: {rand_num}')
        answer = input('Your answer: ')
        answers = ('yes', 'no')
        cor_answer = answers[rand_num % 2]
        if check_answer(answer, cor_answer, name):
            count += 1
        else:
            break
        if count == 3:
            congrats(name)
            break


def main():
    game_even()


if __name__ == '__main__':
    main()
