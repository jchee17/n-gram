#!/bin/bash
#Note: wiki_dir is the smaller one
wiki_dir="/home/jerry/Data/Hopper_Project/ptm_data/wiki_concepts/"
arxiv_dir="/home/jerry/Data/Hopper_Project/bigger_ptm_data/arxiv_processed/"

# corpus to test on
test_dir=$arxiv_dir
# directory of lm models
lm_dir="/home/jerry/GitHub/hopper_loc/n-gram/prototype/lmWB_arxiv/"
# write to folder
output_dir="/home/jerry/GitHub/hopper_loc/n-gram/prototype/eval/arxiv_to_arxiv/WB/"

write=".eval"
everything="*"

count=0
cd $lm_dir
for lm in *.txt.bo
do
	#echo $output_dir$lm$write
	touch $output_dir$lm$write 	
	cd $test_dir
	for txt in *.txt
	do
		#echo $lm_dir$lm
		ngram -lm $lm_dir$lm -ppl $txt >> $output_dir$lm$write
	done
done
