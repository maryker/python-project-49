import prompt


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(question):
    print('Question:', *question)


def check_answer(answer, cor_answer, name):
    if cor_answer == answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. ",
              f"Correct answer was '{cor_answer}'")
        print(f"Let's try again, {name}!")
        return False


def congrats(name):
    print(f'Congratulations, {name}!')
