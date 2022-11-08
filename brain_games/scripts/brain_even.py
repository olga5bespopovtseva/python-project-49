#!/usr/bin/env python3
from random import randint
from scripts.brain_even import get_correct_answer


def get_correct_answer():
    num = (randint(1, 99))
    if num % 2 == 0:
        correct_answer = 'yes'
    if num % 2 != 0:
        correct_answer = 'no'
    question = f'Question: {num}'
    return question, correct_answer


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    get_correct_answer()


if __name__ == '__main__':
    main()
