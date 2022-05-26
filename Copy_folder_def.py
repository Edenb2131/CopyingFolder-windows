import os
import shutil
import bs4
import requests



#given a path and in the end a file name, and it copies it to the new path
def transfer_file(file_path, new_path, old_path, sub_fold = None):
    print(file_path)

#    print(f"the old path is:  {file_path}")
#    print(f"the new path is:  {new_path}")
    if sub_fold != None:
        file_name = f'{old_path}\{sub_fold}\{file_path}'
    else:
        file_name = f'{old_path}\{file_path}'
    print(file_name)
    print("Going to start the transfer")
#    os.mkdir(new_path)
    if file_path == 'desktop.ini':
        pass
    else:
        shutil.copy(file_name, new_path)
    print("Transfer complete")
    print('\n')

#A VARY good work around - just for the path name need to delete the trget folder
def transfer_file1(old_path, new_path):
    print("Im in transfer_files1111")
    shutil.copytree(old_path, new_path)

#getting the old path and looping throw every folder, sub folder and file in path
def loop_thro(old_path, new_path):


    for folder, sub_folders, files in os.walk(old_path):

        print("Currently looking at folder: " + folder)
        print('\n')
        print("THE SUBFOLDERS ARE: ")
        for sub_fold in sub_folders:
            print("\t Subfolder: " + sub_fold)

        print('\n')

        print("THE FILES ARE: ")
        for f in files:
            print("\t File: " + f)
            print("Making a copy")
            print(new_path)
            print(old_path)
            print(folder)
            transfer_file(f, new_path, folder)
        print('\n')