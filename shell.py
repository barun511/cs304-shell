'''
    This is the main shell application.
'''
import sys
import os
import shlex
from builtincommands import *


def break_into_arguments(command):
    return shlex.split(command)

def execute(command):
    if(command[-1]=='&'):
        background_process=True
        command.pop()
    else:
        background_process=False
    
    process_id = os.fork() # Dangerous. Use with care.
    
    if process_id==0:
        os.execvp(command[0],command)
    elif process_id>0:
        if background_process:
            return None
        else:
            returnid, status = os.waitpid(process_id, 0)
            return None
                

def shell_loop():
    status = True    
    while status == True:
        print(os.getcwd() + "$", end = ' ') # The shell prompt
        command = break_into_arguments(input())
        if len(command)==0: # Empty lines do nothing to the prompt
            continue
        if is_built_in(command[0]):
            error = response(command)
            if(error!=None):
                print(error)
        else:
            execute(command)

shell_loop()
