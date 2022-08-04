#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:46:50 2021

@author: avasquez
"""

import os
import shutil
import random
from tqdm import tqdm

class ClassifierRandomDrawFromDirectory:
    
    ''''Randomly Draws images from a directory
        Can choose train, test, and valid.'''
        
    def __init__(self, datapath, validSet, validPercent, validWritePath, testSet, testPercent, testWritePath, trainWritePath):
        self.datapath = datapath
        self.validSet = validSet
        self.validPercent = validPercent
        self.validWritePath = validWritePath
        self.testSet = testSet
        self.testPercent = testPercent
        self.testWritePath = testWritePath
        self.trainWritePath = trainWritePath
        
    def getData(self):
        trainList = []
        validList = []
        testList = []
        usedList = []
        self.dataList = os.listdir(self.datapath)
        
        ##get test list
        if self.testSet:
            for i in tqdm(range(int(len(self.dataList)*self.testPercent)), desc = 'Random Draw of Test Set', colour = 'yellow'):
                randomFile = random.choice(self.dataList)
                fileIndex = self.dataList.index(randomFile)
                ##delete the file by index
                del self.dataList[fileIndex]
                ##add to test list
                testList.append(randomFile)
                ##add to usedList as a sanity check
                usedList.append(randomFile)
        ##get valid list
        if self.validSet:
            for i in tqdm(range(int(len(self.dataList)*self.validPercent)), desc = 'Random Draw of Validation Set', colour = 'yellow'):
                randomFile = random.choice(self.dataList)
                fileIndex = self.dataList.index(randomFile)
                ##delete the file by index
                del self.dataList[fileIndex]
                ##add to valid list
                validList.append(randomFile)
                ##add to usedList as a sanity check
                usedList.append(randomFile)
                
        ##get remainder of datalist and check that it's not in usedList
        for file in tqdm(self.dataList, desc = 'Validating Train Dataset', colour = 'yellow'):
            if file in usedList:
                fileIndex = self.dataList.index(file)
                ##delete the file by index
                del self.dataList[file]
            else:
                trainList.append(file)
        
        return validList, testList, trainList
    
    def writeData(self, validList, testList, trainList):
        if self.testSet:
            if os.path.exists(self.testWritePath):
                    shutil.rmtree(self.testWritePath)
                    os.makedirs(self.testWritePath)
            else:
                os.makedirs(self.testWritePath)
                
            for file in tqdm(testList, desc = 'Writing Test Files', colour = 'green'):
                shutil.copy(self.datapath + file, self.testWritePath + file)
        
        if self.validSet:
            if os.path.exists(self.validWritePath):
                    shutil.rmtree(self.validWritePath)
                    os.makedirs(self.validWritePath)
            else:
                os.makedirs(self.validWritePath)
                
            for file in tqdm(validList, desc = 'Writing Valid Files', colour = 'green'):
                shutil.copy(self.datapath + file, self.validWritePath + file)
                
        if os.path.exists(self.trainWritePath):
                    shutil.rmtree(self.trainWritePath)
                    os.makedirs(self.trainWritePath)
        else:
            os.makedirs(self.trainWritePath)
            
        for file in tqdm(trainList, desc = 'Writing Train Files', colour = 'green'):
            shutil.copy(self.datapath + file, self.trainWritePath + file)
