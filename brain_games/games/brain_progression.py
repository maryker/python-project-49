from random import randint


game_description = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 50)
    step = randint(2, 10)
    length = randint(5, 10)
    progression = []
    for _ in range(length):
        progression.append(start)
        start += step
    rand_index = randint(0, len(progression) - 1)
    correct_answer = progression[rand_index]
    progression.remove(correct_answer)
    progression.insert(rand_index, '..')
    return ' '.join([str(i) for i in progression]), str(correct_answer)
