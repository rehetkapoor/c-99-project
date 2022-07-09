import os
import shutil

path=input("Enter Directory Name:- ")

list_of_files=os.listdir(path)

# This will go through each line

for file in list_of_files:
    name, ext = os.path.splitext(file)

    # Storing extension type
    ext=ext[1:]

    if ext=='':
        continue

    if os.path.exists(path + '/' + ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)