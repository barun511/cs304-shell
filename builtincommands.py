'''
    Checks if a set of commands is implemented within the shell or whether it will have to be searched for in the path.
'''
builtincommands = [ "cd", "exit", "print" ]
def is_built_in(command):
    return command in builtincommands
