from random import randint
from brain_games.scripts.game_script import game_play


def game_descript():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game_even():
    rand_num = randint(1, 100)
    ANSWERS = ('yes', 'no')
    correct_answer = ANSWERS[rand_num % 2]
    return [rand_num], correct_answer


def main():
    game_play(game_even, game_descript)


if __name__ == '__main__':
    main()
