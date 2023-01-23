from random import randint, choice
from operator import add, sub, mul


def game_descript():
    print('What is the result of the expression?')


def game_calc():
    OPERATIONS = ('+', '-', '*')
    rand_a = randint(1, 30)
    rand_b = randint(1, 30)
    rand_op = choice(OPERATIONS)
    question = (rand_a, rand_op, rand_b)
    return question, find_answer(question)


def find_answer(question):
    num1, operator, num2 = question
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return sub(num1, num2)
    else:
        return mul(num1, num2)
