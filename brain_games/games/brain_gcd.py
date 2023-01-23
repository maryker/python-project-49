from random import randint


def game_descript():
    print("Find the greatest common "
          "divisor of given numbers.")


def game_gcd():
    rand_a = randint(1, 100)
    rand_b = randint(1, 100)
    question = (rand_a, rand_b)
    return question, find_gcd(rand_a, rand_b)


def find_gcd(num1, num2):
    gcd = min(num1, num2)
    while gcd != 1:
        if num1 % gcd == 0 and num2 % gcd == 0:
            return gcd
        gcd -= 1
    return gcd
