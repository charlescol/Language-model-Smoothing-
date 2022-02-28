""" 
Creator : charlescol
Date 09/24/2021
Get metrics with a binary model and a test file. Can apply preprocessing on the test file.
"""

import kenlm
import cleantext
import math
import time
import argparse
import statistics
import os

parser = argparse.ArgumentParser()
parser.add_argument("file_working_directory", help = "add file to analyze")
parser.add_argument("binary_model", help = "add binary model path")
parser.add_argument("-n", "--number", default = 1000, help = "Number of lines read", type=int)
parser.add_argument("-r", "--result", default = "", help = "filename to store results")
parser.add_argument("-p", "--preprocessing", action='store_true')
args = parser.parse_args()

def main() :
    perplexity_data = []  
    data = []  
    start_time = time.time()
    model = kenlm.Model(args.binary_model)
    with open(args.file_working_directory, 'r') as file:
        lines = file.readlines()
        for i in range(0, min(args.number,len(lines))) :
            if args.preprocessing :
                preprocess_line = cleantext.clean(lines[i], lower=True, no_urls=True, no_numbers=True, no_phone_numbers=True)
            perplexity_data.append(model.perplexity(lines[i]))
    
    time_occured = time.time() - start_time
    average = sum(perplexity_data) / len(perplexity_data)
    max_value = max(perplexity_data)
    min_value = min(perplexity_data)
    st_dev = statistics.pstdev(perplexity_data)
    
    print(args.file_working_directory + " : ")
    print(str(average) + "|" + str(max_value) + "|" + str(min_value))
    
    file = open(args.result, "a")
    file.write(str(average) + ',' + str(st_dev) + ',' + str(time_occured) + ',' + str(os.path.getsize(args.binary_model)) + '\n')

main()

