#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 12:03:51 2021

@author: avasquez
"""

import os
import sys
import argparse

sys.path.append('../')
from Preprocess_API.getBboxDict import *
from Preprocess_API.writeBboxDict import *

##Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--imagepath", type=str, default = 'JPEGImages/',
                    help="path to large images")
parser.add_argument("--annotpath", type=str, default = 'Annotations/',
                    help="path to annotations")
parser.add_argument("--writepath", type=str, default = 'chips/', 
                    help="where to write output images")
parser.add_argument("--bboxArea", type=int, default = None,
                    help="What's the area of the bbox desired? Example bbWidth * bbHeight")
parser.add_argument("--percentDeviation", type=float, default = 0.75,
                    help="plus/minus this percent larger/smaller(example: 0.25)")
parser.add_argument("--classNamesFile", type=str, default = 'classNames.txt',
                    help=".txt file of class names of interest (one name per line) - leave blank if all classes desired")
args = parser.parse_args()

if __name__ == "__main__":
    ##start clock
    t0 = time.time()
    
    if os.path.exists(args.writepath):
        shutil.rmtree(args.writepath)
        os.mkdir(args.writepath)
    else:
        os.mkdir(args.writepath)
    
    if os.path.exists(args.classNamesFile):
        with open(args.classNamesFile, 'r') as f:
            classnames = f.readlines()
            classnames = [i.strip('\n') for i in classnames]
    else:
        classnames = None
    
    print('\n ************************ Job Description ************************')
    print('Job Name: Get Chips')
    print('Annotation Path: ', args.annotpath)
    print('Image Path: ', args.imagepath)
    print('write Path: ', args.writepath)
    print('Class Names Path: ', args.classNamesFile)
    print('Scanning For BB Area: ', args.bboxArea)
    print('BB Area Percent Deviation: ', args.percentDeviation)
    print(' *****************************************************************')
    
    fileCnt = 0 ##cnt files processed
    totalChipCnt = 0
    for file in tqdm(os.listdir(args.annotpath), desc = 'Extracting Chips', 
                     colour='blue',mininterval=.05, smoothing=0.9):
        ##make sure that the file is a file
        if os.path.isfile(args.annotpath + file):
            
            ##initialize
            bboxes = GetBboxDict(file, args.annotpath, args.imagepath, args.bboxArea, 
                                 args.percentDeviation, args.classNamesFile)
            
            ##get chips
            bboxDict = bboxes.chipDict()
            
            ##filter by size
            bboxDict = bboxes.filterChipDict()
            
            ##write chips
            chipCnt = WriteBboxDict(bboxDict, args.writepath).write()
            
            fileCnt += 1
            
            if chipCnt != None:
                totalChipCnt += chipCnt   
            
    t1 = time.time()
    print('----------------Stats---------------------')
    print('Total Files Processed: ', fileCnt)
    print('Total Chips Processed: ', totalChipCnt)
    
