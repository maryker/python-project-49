from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    rand_num = randint(1, 100)
    correct_answer = 'yes' if is_even(rand_num) else 'no'
    return rand_num, correct_answer


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
