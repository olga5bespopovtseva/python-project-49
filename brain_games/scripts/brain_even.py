#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.cli import welcome_user


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_even():
    num = (randint(1, 99))
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    question = num
    return question, correct_answer    

def game_1():
    rounds = 1, 2, 3
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for num in rounds:
        question, correct_answer = get_even()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print('Correct!')
            print(f"Congratulations, '{name}'!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was " f"'{correct_answer}'.")
            print(f"Let's try again, '{name}'!")         


def main():

    print('Welcome to the Brain Games!')

    game_1()
    

if __name__ == '__main__':
    main()
