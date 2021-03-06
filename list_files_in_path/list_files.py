########################################################
# Take the name of path and character from console and
# find out the file in the given path those are starting
# with the given character
#
# Invoke :- python list_files.py <path> <ch>
#########################################################

import os, sys

def list_files(path, ch, ignore_case = False):
    '''
    Finds out the files (not directories) starting with
    the given character, present in the given path.

    If 'ignore_case' is True, then finds the files, names 
    starting with both lowercase and uppercase of given character.
    '''
    content = os.listdir(path)
    directories = [i for i in content if os.path.isdir(path+os.sep+i)]
    files = [i for i in content if os.path.isfile(path+os.sep+i)]
    selected_files = [f for f in files if f.startswith(ch)]
    if ignore_case and ch.isalpha():
        selected_files2 = [f for f in files if f.startswith(ch.capitalize())] if ch.islower() else [f for f in files if f.startswith(ch.lower())]
        selected_files.extend(selected_files2)
    print("Directories present in the given path are :-\n {}".format(directories))
    print("Files present in the given path are  :-\n {}".format(files))
    return selected_files

path = sys.argv[1]
ch = sys.argv[2]
# Take input from User whether to list files for both upper and lower case
ignore_case = input("Do you want to list the files for both upper and lower case of the given character ? (Yes/No): ")
f = list_files(path, ch) if ignore_case is 'No' else list_files(path, ch, True)
if f == []:
    print("No files sstarting with letter '{}' are present in {}".format(ch, path))
else:
    print("Files whose name starts with '{}' in {} are :- ".format(ch, path))
    for i in f:
        print(i)



