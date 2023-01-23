from random import randint


def game_descript():
    print('What number is missing in the progression?')


def game_progression():
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
    return progression, correct_answer
