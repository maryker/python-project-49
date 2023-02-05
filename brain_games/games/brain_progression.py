from random import randint


GAME_DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    progression = make_progression()
    rand_index = randint(0, len(progression) - 1)
    correct_answer = progression[rand_index]
    progression[rand_index] = '..'
    return ' '.join([str(i) for i in progression]), str(correct_answer)


def make_progression():
    start = randint(1, 50)
    step = randint(2, 10)
    length = randint(5, 10)
    progression = []
    for _ in range(length):
        progression.append(start)
        start += step
    return progression
