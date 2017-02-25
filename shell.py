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
local_variables["barun"] = "Barun is the most awesome guy ever"

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
        
        if command[0]=="set" or command[0]=="append": # set is keyword to set a variable
            if len(command)>3:
                print("Incorrect format: Use set/append <variable_name> <value>")
            elif command[0]=="set":
                if command[1] in environment_variables:
                    os.environ[command[1]]=command[2]
                else:
                    local_variables[command[1]]=command[2]
            else:
                if command[1] in environment_variables:
                    os.environ[command[1]]+=command[2]
                elif command[1] in local_variables:
                    local_variables[command[1]]+=command[2]
                else:
                    local_variables[command[1]]=command[2]
            continue
        # Replace all variables with values that they should have
        for i in range(len(command)):
            if command[i][0]=='$' and command[i][0].find('=') < 0:
                variable_name = command[i][1:]
                if variable_name in environment_variables:
                    command[i] = os.environ[variable_name]
                elif variable_name in local_variables:
                    command[i] = local_variables[variable_name]
               

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
