#!/bin/bash

#Note: wiki_dir is the smaller one
wiki_dir="/home/jerry/Data/Hopper_Project/ptm_data/wiki_concepts/"
arxiv_dir="/home/jerry/Data/Hopper_Project/bigger_ptm_data/arxiv_processed/"

# Set dir from which to train LM's
train_dir=$arxiv_dir
lmGT_dir="/home/jerry/GitHub/hopper_loc/n-gram/prototype/lmGT_arxiv/"
lmWB_dir="/home/jerry/GitHub/hopper_loc/n-gram/prototype/lmWB_arxiv/"
cd $train_dir
pwd

# try Witten-Bell discounting method for small corpus
for f in *.txt
do
	#ngram-count -order 2 -text $f -lm $lmGT_dir$f.bo
	ngram-count -order 2 -wbdiscount2 -text $f -lm $lmWB_dir$f.bo
done
