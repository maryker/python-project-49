import prompt
from random import randint
from brain_games.scripts.game_script import greet_user, check_answer
from brain_games.scripts.game_script import congrats, ask_question


def game_gcd():
    name = greet_user()
    print("Find the greatest common "
          "divisor of given numbers.")
    count = 0
    while True:
        rand_a = randint(1, 100)
        rand_b = randint(1, 100)
        question = (rand_a, rand_b)
        ask_question(question)
        cor_answer = correct_answer(question)
        answer = prompt.integer('Your answer: ')
        if check_answer(answer, cor_answer, name):
            count += 1
        else:
            break
        if count == 3:
            congrats(name)
            break


def correct_answer(numbers):
    num1, num2 = (numbers)
    gcd = min(numbers)
    while gcd != 1:
        if num1 % gcd == 0 and num2 % gcd == 0:
            return gcd
        gcd -= 1
    return gcd


def main():
    game_gcd()


if __name__ == '__main__':
    main()
