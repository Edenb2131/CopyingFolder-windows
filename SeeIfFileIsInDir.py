import argparse
import os



def main():

    parser = argparse.ArgumentParser(description="check to see if a file is in the dircatory")
    parser.add_argument('file', type=argparse.FileType('r'), help='name of file')
    parser.add_argument('dire', help='holding the diractory name')
    args = parser.parse_args()

    print(os.listdir(args.dire))
    d = os.listdir(args.dire)
    print(type(d)) # = list
    print(os.path.basename(args.file.name))

#WORKS
#    a = input("Whats the name of the file ?")
#    if a in d:
#        print("Its in d")

    for d in os.listdir(args.dire):
        if os.path.basename(args.file.name) == d:
            print("The file is in the diractory")
        else:
            print("Its not there")



    with args.file as file:
        print(file.read())

main()