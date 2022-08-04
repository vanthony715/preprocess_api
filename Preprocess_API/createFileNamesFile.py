#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Summary:
    Put files from a directory into a file

@author: avasquez
"""
#!/usr/bin/python

import argparse, os
from random import shuffle
from tqdm import tqdm

parser = argparse.ArgumentParser()

parser.add_argument('--filepath', default='./', type=str,
                    help='path to folder that contains images')

parser.add_argument('--outfileName', default='./data/train_shuffled.flist', type=str,
                    help='What should the outfile be called')

parser.add_argument('--shuffled', default='1', type=int,
                    help='Need to be shuffled?')

class CreateFileNamesFile:
    def __init__(self, filepath, outfileName, shuffled):
        
        self.filepath = filepath
        self.outfileName = outfileName
        self.shuffled = shuffled
        self.NamesList = []
        
    def getNamesList(self):
        for file in tqdm(os.listdir(self.filepath), desc = 'Creating Names List', colour = 'blue'):
            self.NamesList.append(self.filepath + file)
         # shuffle file names if set
        if self.shuffled == 1:
            shuffle(self.NamesList)
        
        f = open(self.outfileName, "w")
        f.write("\n".join(self.NamesList))
        f.close()
        

if __name__ == "__main__":
    args = parser.parse_args()
    CreateFileNamesFile(args.filepath, args.outfileName, args.shuffled).getNamesList()
    
    
    
    
    
    