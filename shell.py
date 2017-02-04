'''
    This is the main shell application.
'''
import sys
import os
import shlex
from builtincommands import *


def break_into_arguments(command):
    return shlex.split(command)


def shell_loop():
    status = True    
    while status == True:
        print("$", end = ' ')
        command = break_into_arguments(input())
        if is_built_in(command[0]):
            print("This part has yet to be implemented")
        else:
            os.execvp(command[0],command)
shell_loop()
