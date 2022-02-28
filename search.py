""" 
Creator : charlescol
Date 09/24/2021
Open each file in a directory and print it in the standard ouput. Can apply preprocessing on the files
"""

import os
import math
import argparse
import cleantext


parser = argparse.ArgumentParser()
parser.add_argument("directory", help = "add working directory")
parser.add_argument("-n", "--number", default=math.inf, help = "number of files open", type=int)
parser.add_argument("-p", "--preprocessing", action='store_true')
args = parser.parse_args()

# To get all files in a directory
def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

	# Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    file_paths.sort()
    return file_paths  # Self-explanatory. 	

def main() :
    data = [] 
    current =[] 
    final = None
    files = get_filepaths(args.directory)
    for i in range(0, min(abs(int(args.number)), len(files))) :
        with open(files[i], 'r') as fin:
            if args.preprocessing :
                current += cleantext.clean(fin.read(), lower=True, no_urls=True, no_numbers=True, no_phone_numbers=True).split()
            else :
                current += fin.read().split()
            data.append(len(set(current)))
            print(i, " : ", data[-1])
    print(data)
main()