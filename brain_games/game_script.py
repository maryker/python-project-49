import prompt
max_rounds = 3


def play_game(make_question, game_description):
    name = greet_user()
    print(game_description)
    count = 0
    while True:
        question, correct_answer = make_question()
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
        if count == max_rounds:
            print(f'Congratulations, {name}!')
            break


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
