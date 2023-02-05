from random import randint, choice
from operator import add, sub, mul


GAME_DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operations = ('+', '-', '*')
    rand_a = randint(1, 30)
    rand_b = randint(1, 30)
    rand_op = choice(operations)
    question = [rand_a, rand_op, rand_b]
    return ' '.join([str(i) for i in question]), str(find_answer(question))


def find_answer(question):
    num1, operator, num2 = question
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return sub(num1, num2)
    else:
        return mul(num1, num2)
