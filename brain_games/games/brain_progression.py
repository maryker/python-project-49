import prompt
from random import randint
from brain_games.scripts.game_script import greet_user, check_answer
from brain_games.scripts.game_script import congrats, ask_question


def game_progression():
    name = greet_user()
    print('What number is missing in the progression?')
    count = 0
    while count != 3:
        progr, cor_answer = progression()
        ask_question(progr)
        answer = prompt.integer('Your answer: ')
        if check_answer(answer, cor_answer, name):
            count += 1
        else:
            break
        if count == 3:
            congrats(name)
            break


def progression():
    start = randint(1, 50)
    step = randint(2, 10)
    length = randint(5, 10)
    progression = []
    for _ in range(length):
        progression.append(start)
        start += step
    rand_index = randint(0, len(progression) - 1)
    cor_answer = progression[rand_index]
    progression.remove(cor_answer)
    progression.insert(rand_index, '..')
    return progression, cor_answer


def main():
    game_progression()


if __name__ == '__main__':
    main()
