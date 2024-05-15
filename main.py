from functions import *
from stats import *
from instructions_list import list_of_instructions as inst
from instructions_list import prompt_formatting, keyword
from datetime import datetime

xyz = [1+i for i in range(50, 101)]
hh = [10+i for i in range(50, 101)]
pp = [10*i for i in range(50, 101)]

def menu():

    while True:
        cmd_list = []
        try:
            user_prompt = input(f'{datetime.now().strftime("%H:%M:%S")} [👽] : ')
            cmd_list.extend(user_prompt.lower().split())
            #print(cmd_list)
            if ('bye' or 'exit') in cmd_list:
                print(f'{datetime.now().strftime("%H:%M:%S")} [🖥️] : Program exited. Goodbye!')
                break
            else:
                if inst(user_prompt) == 'None':
                    print(f'{datetime.now().strftime("%H:%M:%S")} [🖥️] : Invalid prompt! Try again.')
                else:
                    print(f'{datetime.now().strftime("%H:%M:%S")} [🖥️] : Calculating {keyword(user_prompt)}...')
                    #print(prompt_formatting(user_prompt)) # -> formatted prompt debug
                    bot = prompt(prompt_formatting(user_prompt), inst(user_prompt))
                    print(f'{datetime.now().strftime("%H:%M:%S")} [🖥️] : Executing {bot}') #-> hint for function calling debug
                    execute = f'print(\'{datetime.now().strftime("%H:%M:%S")} [🖥️] : Here you go!\', {bot})'
                    exec(execute)
        except Exception as e:
            print(f'{datetime.now().strftime("%H:%M:%S")} [🖥️] : Invalid prompt! Try again.')
            print(f'{datetime.now().strftime("%H:%M:%S")} [🖥️] : {e}')


if __name__ == '__main__':
    print(f'{datetime.now().strftime("%H:%M:%S")} [🖥️] : Ask away!')
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
