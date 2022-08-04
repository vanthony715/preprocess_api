#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 15:26:36 2021

@author: avasquez
"""
import sys
import time
import argparse

sys.path.append('/home/domain/avasquez/ML/APIs/')
from Preprocess_API.classifierRandomDrawFromDirectory import *

##Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--basepath", type=str, default = './',
                    help="common path to to all paths")

parser.add_argument("--datapath", type=str, default = 'allFiles/',
                    help="path to large images")

parser.add_argument("--validSet", type=bool, default = True,
                    help="store false if validation set is not needed")

parser.add_argument("--validPercent", type=float, default = 0.10,
                    help="percentage of dataset for validation set ")

parser.add_argument("--validWritePath", type=str, default = 'valid/imgs/',
                    help="path to write validation set")

parser.add_argument("--testSet", type=bool, default = False,
                    help="store false if test set is not needed")

parser.add_argument("--testPercent", type=float, default = 0.15,
                    help="percentage of dataset for test set")

parser.add_argument("--testWritePath", type=str, default = 'test/imgs/', 
                    help="path to write test set")

parser.add_argument("--trainWritePath", type=str, default = 'train/imgs/', 
                    help="path to write train set")

args = parser.parse_args()

if __name__ == "__main__":
    ##start clock
    t0 = time.time()
    
    print('\n ************************ Job Description ************************')
    print('Job Name: Classifier Random Draw Single Class')
    print('Basepath: ', args.basepath)
    print('Data Path: ', args.datapath)
    print('Validation Set: ', args.validSet)
    print('Validation Percent: ', args.validPercent)
    print('Validation Write Path: ', args.validWritePath)
    print('Test Set: ', args.testSet)
    print('Test Percent: ', args.testPercent)
    print('Test Write Path: ', args.testWritePath)
    print('Train Write Path: ', args.trainWritePath)
    print(' *****************************************************************')
    
    ##/mnt/opsdata/neurocondor/datasets/avasquez/data/Neuro/MWIRN/RIPS/data/cegan/training/umapGen/inverseTransformed/
    
    drawObject = ClassifierRandomDrawFromDirectory(os.path.join(args.basepath, args.datapath),
                                                   args.validSet, args.validPercent, 
                                                   os.path.join(args.basepath, args.validWritePath), 
                                                   args.testSet, args.testPercent, 
                                                   os.path.join(args.basepath, args.testWritePath), 
                                                   os.path.join(args.basepath, args.trainWritePath))
    
    validList, testList, trainList = drawObject.getData()
    
    drawObject.writeData(validList, testList, trainList)
    
    fileCnt = len(os.listdir(args.basepath + args.datapath))
    
    t1 = time.time()
    print('----------------Stats---------------------')
    print('File Cnt: ', fileCnt)
    if validList:
        print('Valid Cnt: ', len(validList))
    if testList:
        print('Test Cnt: ', len(testList))
    print('Train Cnt: ', len(trainList))
    print('Execution Time: ', round((t1 - t0), 5))