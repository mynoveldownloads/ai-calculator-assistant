from functions import prompt
from stats import *
from instructions_list import list_of_instructions as inst

xyz = [1+i for i in range(50, 101)]
hh = [10+i for i in range(50, 101)]
pp = [10*i for i in range(50, 101)]


def menu():
    while True:
        try:
            user_prompt = input('>>> ')

            if inst(user_prompt) == 'None':
                print('invalid prompt')
            else:
                bot = prompt(user_prompt, inst(user_prompt))
                print(bot) #-> hint for function calling
                execute = f'print(\'Answer:\', {bot})'
                exec(execute)
        except Exception as e:
            print(f'invalid prompt \n{e}')


if __name__ == '__main__':
    menu()

"""
Sample prompts:
- give median xyz
- give median xyz, hh, pp
- what is variance of xyz, hh
- variance of xyz, hh, pp
- give mean of xyz, hh, pp
- sd of xyz, pp
- give sd of xyz, hh and pp
- what is the sum of xyz
"""
