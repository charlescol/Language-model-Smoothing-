#!/bin/bash 
training_directory="/u/demorali/corpora/1g-word-lm-benchmark-r13output/training-monolingual.tokenized.shuffled"
kenLM_directory="/u/demorali/bin/x86_64/moses_3.0/bin"
test_file="/u/demorali/corpora/1g-word-lm-benchmark-r13output/heldout-monolingual.tokenized.shuffled/news.en-00000-of-00100"

train(){
    python searchFilesFromDirectory.py $training_directory -p -n $1| $kenLM_directory/lmplz -o 3 > ./data.arpa
    $kenLM_directory/build_binary data.arpa data.binary
} 
compute(){
    python computing.py $test_file ./data.binary -n 1000 -r "data.txt"  -p
} 
# Clear the data file if already exists 
if test -f ./data.txt; then 
    > ./data.txt
fi 

train 99 # Train the model    
compute # Predict with new data files 
