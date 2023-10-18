import random


def greeting(name, file=None):
    if file is None:
        print(f'Hi, {name}. I see you first time, i\'m reale nice to meet you!')
    else:
        with open(file, 'r', encoding='utf-8') as file:
            file_info = file.read()
        if name in file_info:
            print(f'Hi, {name} nice to see you agan!')
        else:
            print(f'Hi, {name}. I see you first time, i\'m reale nice to meet you!')


def wright_user_name(name, file):
    with open(file, 'a', encoding='utf-8') as file:
        file.write(name + '\n')


def math_questions():
    mode = str(input('Tell me what are you chose. \n:'))
    iteration_number = int(input('Tell me number of questions. \n:'))
    right_answers_count = 0
    for i in range(0, iteration_number):
        first_number = random.randint(0, 100)
        second_number = random.randint(0, 100)
        if mode == '*':
            print(f'{first_number} * {second_number}')
            answer = int(input('Yore answer? \n:'))
            resalt = int(first_number) * int(second_number)
            if answer == resalt:
                print('Your right!')
                right_answers_count += 1
            elif answer != resalt:
                print('I\'m sorry but you falt!')
        elif mode == '/':
            print(f'{first_number} / {second_number}')
            answer = int(input('Yore answer? \n:'))
            resalt = int(first_number) / int(second_number)
            if answer == int(resalt):
                print('Your right!')
                right_answers_count += 1
            elif answer != int(resalt):
                print('I\'m sorry but you falt!')
        elif mode == '+':
            print(f'{first_number} + {second_number}')
            answer = int(input('Yore answer? \n:'))
            resalt = int(first_number) + int(second_number)
            if answer == resalt:
                print('Your right!')
                right_answers_count += 1
            elif answer != resalt:
                print('I\'m sorry but you falt!')
        elif mode == '-':
            print(f'{first_number} - {second_number}')
            answer = int(input('Yore answer? \n:'))
            resalt = int(first_number) - int(second_number)
            if answer == resalt:
                print('Your right!')
                right_answers_count += 1
            elif answer != resalt:
                print('I\'m sorry but you falt!')

    return right_answers_count, iteration_number
