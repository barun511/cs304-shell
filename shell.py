'''
    This is the main shell application.
'''
def shell_loop():
    status = True
    
    while status == True:
        print("$", end = ' ')
        command = input()
        print(command)                 

shell_loop()
