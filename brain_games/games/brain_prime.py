from random import randint


def game_descript():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def game_prime():
    rand_num = randint(1, 100)
    correct_answer = 'yes' if is_prime(rand_num) else 'no'
    return [rand_num], correct_answer


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
