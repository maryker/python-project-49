import prompt
MAX_ROUNDS = 3


def play_game(game):
    name = greet_user()
    print(game.GAME_DESCRIPTION)
    count = 0
    while True:
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if correct_answer == answer:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break
        if count == MAX_ROUNDS:
            print(f'Congratulations, {name}!')
            break


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
