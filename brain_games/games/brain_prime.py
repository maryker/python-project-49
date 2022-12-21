from random import randint
from brain_games.scripts.game_script import greet_user, check_answer
from brain_games.scripts.game_script import congrats, ask_question


def game_prime():
    name = greet_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != 3:
        rand_num = randint(1, 100)
        ask_question((rand_num,))
        cor_answer = is_prime(rand_num)
        answer = input('Your answer: ')
        if check_answer(answer, cor_answer, name):
            count += 1
        else:
            break
        if count == 3:
            congrats(name)
            break


def is_prime(number):
    if number == 1:
        return 'no'
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    return 'yes'


def main():
    game_prime()


if __name__ == '__main__':
    main()
