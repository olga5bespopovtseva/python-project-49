#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_correct_answer():
    num = (randint(1, 99))
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    question = num
    return question, correct_answer    


def main():
    print(DESCRIPTION)
    print(get_correct_answer())
    

if __name__ == '__main__':
    main()
