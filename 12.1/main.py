import os
from utils.helpfull_funcs import greeting, math_questions, wright_user_name


USERS_FILE = os.path.join('..', 'sourses', 'users_info.txt')
USERS_DIRECTORY = os.path.join('..', 'sourses')


def main():

    if os.path.isfile(USERS_FILE):
        with open(USERS_FILE, 'r', encoding='utf-8') as file:
            users_list = file.readlines()
    elif not os.path.isdir(USERS_DIRECTORY):
        os.mkdir(USERS_DIRECTORY)

    user_name = str(input('Please tell me your name. \n:'))

    if os.path.isfile(USERS_FILE):
        greeting(user_name, USERS_FILE)
        if user_name+'\n' not in users_list:
            wright_user_name(user_name, USERS_FILE)

    elif not os.path.isfile(USERS_FILE):
        greeting(user_name)
        wright_user_name(user_name, USERS_FILE)

    points, iteration_count = math_questions()

    return points, iteration_count

    
if __name__ == '__main__':
    point, iteration_count = main()
    print(f'You also had {iteration_count} questions, and you got {point} right answers')
    print('I hope you are satisfied with your result!')
