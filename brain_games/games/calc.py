import random


DESCRIPTION = 'What is the result of the expression?'


def get_correct_answer():
    action = random.choice('+' '-' '*')
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    if action == '+':
        correct_answer = num1 + num2
    if action == '-':
        correct_answer = num1 - num2
    if action == '*':
        correct_answer = num1 * num2
    question = f'Question: {num1} {action} {num2}'
    return question, correct_answer

