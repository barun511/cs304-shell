import os
def find(filename, path):
    directories = []
    if path[-1]=='/':
        path = path[0:-1]  # To make sure we don't have that stupid trailing slash
    print(path)
    for file in os.listdir(os.path):
        if os.path.isdir(os.path+file):
            directories.append(os.path+file)
        else:
            if file==filename:
                return path + '/ ' + filename
    for directory in directories:
        result = find(filename,path + directory)
        if result!=None:
            return result
    return None
filename, path = input().split()
print(filename)
print(path)
print (find(filename, path))
