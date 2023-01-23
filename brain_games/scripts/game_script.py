import prompt


def game_play(make_question, game_descript):
    name = greet_user()
    game_descript()
    count = 0
    while True:
        question, correct_answer = make_question()
        ask_question(question)
        answer = input('Your answer: ')
        if check_answer(answer, correct_answer, name):
            count += 1
        else:
            break
        if count == 3:
            congrats(name)
            break


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(question):
    print('Question:', *question)


def check_answer(answer, correct_answer, name):
    if str(correct_answer) == str(answer):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. ",
              f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
        return False


def congrats(name):
    print(f'Congratulations, {name}!')
