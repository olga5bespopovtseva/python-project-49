from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def get_question_with_answer():
    rand_num = randint(1, 99)
    correct_answer = 'yes' if is_prime(rand_num) is True else 'no'
    question = f"{rand_num}"
    return question, correct_answer
