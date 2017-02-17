'''
    This is the main shell application.
'''
import sys
import shlex
import os
from builtincommands import *

debug_mode = False
# Debug mode or not?
if len(sys.argv) > 1:
    option = sys.argv[1][1:]
    if option == 'd':
        debug_mode = True
        print("Entering Debug Mode")
    elif option == 'b':
        print("The creator of this shell is Barun Parruck")
    else:
        print("Invalid option. Please start with -d for debug mode.")

environment_variables = ["PATH", "HOME"]
local_variables = dict()


def break_into_arguments(command):
    return shlex.split(command)

def execute(command):
    # Background or foreground
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
            return returnid    

def shell_loop():
    status = True    
    while status == True:

        print(os.getcwd() + " | thsh>", end = ' ') # The shell prompt

        command = break_into_arguments(input())

        if len(command)==0: # Empty lines do nothing to the prompt
            continue

        if debug_mode:
            print("Running " + ' '.join(command))

        # Replace all variables with values that they should have
        for argument in command:
            if argument[0]=='$' and argument.find('=') < 0:
                variable_name = argument[1:]
                print(variable_name)
                if variable_name in environment_variables:
                    argument = os.environ[variable_name]
                    print(argument)
                elif variable_name in local_variables.key():
                    argument = local_variables[variable_name]

        if is_built_in(command[0]):
            error = response(command)
            if error=="Logout": # The quit command has been received
                staus=False
            if error!=None or debug_mode:
                print(error)
        else:
            returnid = execute(command)
            if debug_mode:
                print("Ended: " + ' '.join(command) + str(returnid))

shell_loop()
