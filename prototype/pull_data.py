# pull logprob, ppl, ppl1 from test.sh (text) output files
# one statistic per 2D numpy array 
# row: train
# col: test

import os
import pickle
import numpy as np

wiki_dir="/home/jerry/Data/Hopper_Project/ptm_data/wiki_concepts/"
arxiv_dir="/home/jerry/Data/Hopper_Project/bigger_ptm_data/arxiv_processed/"
cwd            = "/home/jerry/GitHub/hopper_loc/n-gram/prototype/"
readin_dir     = "eval/arxiv_to_arxiv/WB/"

#def pull_train(cwd, readin_dir):
#    parse = readin_dir.split('_')
#    train = parse[0]
#    if train == 'wiki':
#        train_dir = wiki_dir
#    elif train == 'arxiv':
#        train_dir = arxiv_dir
#    else :
#        break #error message
#    list_train = os.listdir(train_dir)
#    pickle.dump(list_train, cwd+"analysis/"+train)

def gen_list_dir(list_dir, save_dir):
    list_out = os.listdir(list_dir)
    pickle.dump(list_out, open(save_dir, 'w'))

def pull_data(cwd, readin_dir):
    """ pulls data from srilm output into 3 numpy matrices 
        NOTE: train is partial of full set, test equal to 
        full set
        """
    # parse readin_dir to get train and test sets
    parse = readin_dir.split('_')
    train_set = parse[0]
    test_set  = parse[2]
    
    # list_train, list_test 
    list_train      = pickle.load(open(cwd+"analysis/list_{}.p".format(
        train_set), 'r'))
    list_test       = pickle.load(open(cwd+"analysis/list_{}.p".format(
        test_set), 'r')) 

    # read matrix sizes 
    num_train       = len(list_train)
    num_test        = len(list_test)
    logprob_matrix  = np.zeros((num_train, num_test))
    ppl_matrix      = np.zeros((num_train, num_test))
    ppl1_matrix     = np.zeros((num_train, num_test))

    count = 0
    # look in directory because do not have all tested
    for f in os.listdir(cwd+"eval/"+readin_dir+"/WB/"):
        fp = open(cwd+"eval/"+readin_dir+"/WB/"+f, 'r')
        if count % 100 == 0:
            print(count)
        count += 1
        while True:
            line1   = fp.readline()
            line2   = fp.readline()
            if not line2: break 
        
            # read in new data to be added
            test    = line1.split(' ')[1].rstrip(':')
            line2   = line2.split(' ')

            logprob = float(line2[3])
            ppl     = float(line2[5])
            ppl1    = line2[7].rstrip('\n')
            if (ppl1 == "undefined"):
                ppl1 = -1 # error code
            else:
                ppl1 = float(ppl1)
            train   = f.strip('.bo.eval')

            # write to matrix
            idx_train = list_train.index(f.rstrip('.bo.eval'))
            idx_test  = list_test.index(test)
            logprob_matrix[idx_train,idx_test] = logprob
            ppl_matrix[idx_train,idx_test] = ppl
            ppl1_matrix[idx_train,idx_test] = ppl1
    
    # write to numpy file
    np.save(cwd+"analysis/logprob_{}_to_{}.npy".format(
        train_set, test_set), logprob_matrix)
    np.save(cwd+"analysis/ppl_{}_to_{}.npy".format(
        train_set, test_set), ppl_matrix)
    np.save(cwd+"analysis/ppl1_{}_to_{}.npy".format(
        train_set, test_set), ppl1_matrix)

# =============================================================================
#gen_list_dir(wiki_dir,  cwd+"analysis/list_wiki.p")
#gen_list_dir(arxiv_dir, cwd+"analysis/list_arxiv.p")

pull_data(cwd, "arxiv_to_arxiv") 
#pull_data(cwd, "arxiv_to_wiki") 
#pull_data(cwd, "wiki_to_arxiv") 
#pull_data(cwd, "wiki_to_wiki") 
