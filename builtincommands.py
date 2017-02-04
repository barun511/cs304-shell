'''
    Checks if a set of commands is implemented within the shell or whether it will have to be searched for in the path.
    The built in commands will return None if they execute correctly, otherwise they will return an error string.
'''
import os
builtincommands = [ "ls", "cd", "exit", "print","pwd" ]
def is_built_in(command):
    return command in builtincommands

def cd(command):
    if(len(command)>2):
        return "Error: Cannot change to multiple directories."
    if(len(command)==1):
        return "Error: No directory specified."
    else:
        if(os.path.isdir(command[1])):
            os.chdir(command[1])
        else:
            return "Error: Directory not found."
def pwd(command):
    if(len(command)>=2):
        return "Error: arguments invalid"
    else:
        print(os.getcwd())
def ls(command):
    if(len(command)>2):
        return "Error: Too many commands."
    if(len(command)==1):
        for file in os.listdir(os.getcwd()):
            print(file)
    elif(len(command)==2):
        if(os.path.isdir(command[1])):
            for file in command[1]:
                print(file)
        else:
            return "Error: Not a directory"


def response(command): # There must surely be a better way to do this...
    print(command[0])
    if(command[0]=="cd"):
        return cd(command)
    if(command[0]=="pwd"):
        return pwd(command)
    if(command[0]=="ls"):
        return ls(command)

