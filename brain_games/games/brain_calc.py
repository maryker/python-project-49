import prompt
from random import randint, choice
from brain_games.scripts.game_script import greet_user, check_answer, congrats


def game_calc():
    name = greet_user()
    operations = ('+', '-', '*')
    count = 0
    while True:
        rand_a = randint(1, 30)
        rand_b = randint(1, 30)
        rand_op = choice(operations)
        print(rand_a, rand_op, rand_b)
        cor_answer = correct_answer(rand_op, rand_a, rand_b)
        answer = prompt.integer('Your answer: ')
        if check_answer(answer, cor_answer, name):
            count += 1
        else:
            break
        if count == 3:
            congrats(name)
            break


def correct_answer(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


def main():
    game_calc()


if __name__ == '__main__':
    main()
