#!/bin/bash 
training_directory="/u/demorali/corpora/1g-word-lm-benchmark-r13output/training-monolingual.tokenized.shuffled"
kenLM_directory="/u/demorali/bin/x86_64/moses_3.0/bin"
test_file="/u/demorali/corpora/1g-word-lm-benchmark-r13output/heldout-monolingual.tokenized.shuffled/news.en-00000-of-00100"

train(){
    python search.py $training_directory -n $1 | $kenLM_directory/lmplz -o 2 > ./data.arpa
    $kenLM_directory/build_binary data.arpa data.binary
} 
compute(){
    python computing.py $test_file ./data.binary -n 1000 -r "data.txt"
} 

# Clear the data file if already exists 
if test -f ./data.txt; then 
    > ./data.txt
fi 

# Get the number 'n' of files in the training directory then launch the process 'n' times for a traing which contains i tranches
number_of_files=$(expr $(ls -l $training_directory | grep -v ^d| wc -l) - 1)
for i in $(eval echo {1..$number_of_files})
do
  train $i # Train the model    
  compute # Predict with new data files 
done



