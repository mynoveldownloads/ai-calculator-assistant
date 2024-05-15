from functions import prompt
from stats import *
from instructions_list import list_of_instructions

xyz = [1+i for i in range(50, 101)]
hh = [10+i for i in range(50, 101)]
pp = [10*i for i in range(50, 101)]


def menu():
    while True:
        user_prompt = input('>>> ')
        bot = prompt(user_prompt, list_of_instructions(user_prompt))
        #print(bot) -> hint for function calling
        execute = f'print(\'Answer:\', {bot})'
        exec(execute)


if __name__ == '__main__':
    menu()