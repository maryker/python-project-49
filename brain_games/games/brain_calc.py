import prompt
from random import randint, choice
from brain_games.scripts.game_script import greet_user, check_answer
from brain_games.scripts.game_script import congrats, ask_question


def game_calc():
    name = greet_user()
    print('What is the result of the expression?')
    OPERATIONS = ('+', '-', '*')
    count = 0
    while True:
        rand_a = randint(1, 30)
        rand_b = randint(1, 30)
        rand_op = choice(OPERATIONS)
        question = (rand_a, rand_op, rand_b)
        ask_question(question)
        cor_answer = correct_answer(rand_op, rand_a, rand_b)
        answer = prompt.integer('Your answer: ')
        if check_answer(answer, cor_answer, name):
            count += 1
        else:
            break
        if count == 3:
            congrats(name)
            break


def correct_answer(question):
    num1, operator, num2 = question
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
