from random import randint


GAME_DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    rand_a = randint(1, 100)
    rand_b = randint(1, 100)
    question = [rand_a, rand_b]
    return ' '.join([str(i) for i in question]), str(find_gcd(rand_a, rand_b))


def find_gcd(num1, num2):
    gcd = min(num1, num2)
    while gcd != 1:
        if num1 % gcd == 0 and num2 % gcd == 0:
            return gcd
        gcd -= 1
    return gcd
