import argparse
import os
import shutil
import Copy_folder_def
import CopyFolder_logger



def main():
    parser = argparse.ArgumentParser(description="getting a folder and coping it to another place")
    parser.add_argument('-p', '--path', required=True, help='getting the path of the folder i want to copy')
    parser.add_argument('-p1', '--path1', required=True, help='getting the path where i want to folder to be copied')
    parser.add_argument('-l', '--log', type=argparse.FileType('w+'), required=False, help='txt file that logged')
    args = parser.parse_args()

    old_path = args.path
    new_path = args.path1


    print(args.path)
#    Copy_folder_def.transfer_file(args.path, args.path1)
    Copy_folder_def.loop_thro(old_path, new_path)
#    Copy_folder_def.transfer_file1(old_path, new_path)


main()
