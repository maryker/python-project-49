from brain_games.games.brain_calc import get_question_and_answer, game_description
from brain_games.game_script import play_game


def main():
    play_game(get_question_and_answer, game_description)


if __name__ == '__main__':
    main()
