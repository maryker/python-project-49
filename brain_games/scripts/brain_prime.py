from brain_games.games.brain_prime import get_question_and_answer
from brain_games.games.brain_prime import GAME_DESCRIPTION
from brain_games.game_script import play_game


def main():
    play_game(get_question_and_answer, GAME_DESCRIPTION)


if __name__ == '__main__':
    main()
