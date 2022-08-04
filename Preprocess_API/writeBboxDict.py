#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:46:29 2021

@author: avasquez
"""
import os
import shutil
from tqdm import tqdm
import cv2
import time

class WriteBboxDict:
    def __init__(self, bboxDict, writepath):
        self.bboxDict = bboxDict
        self.writepath = writepath
        self.cnt = 0
    ##TODO Make sure that all chips are printed and not just the first one from the annotations
    def write(self):
        ##Check that dictionary exists
        if self.bboxDict['name'] != None:
            for i in tqdm(range(len(self.bboxDict['name'])), desc = 'Extracting Chips', 
                             colour='blue',mininterval=.05, smoothing=0.9):
                
                ##check that item at inded exists
                if self.bboxDict['name'][i] != None:
                    ##get width and height of chip
                    w = int(self.bboxDict['xmax'][i]) - int(self.bboxDict['xmin'][i])
                    h = int(self.bboxDict['ymax'][i]) - int(self.bboxDict['ymin'][i])
                    
                    ##get annotation at index
                    annotation = self.bboxDict['annotpath'][i] + self.bboxDict['file'][i] + '.xml'
                    ##get image at index
                    im = self.bboxDict['imagepath'][i] + self.bboxDict['file'][i] + '.jpg'
                        
                    ##read image to extract chip
                    image = cv2.imread(im)
            
                    ##extract chip
                    chip = image[int(self.bboxDict['ymin'][i]) : int(self.bboxDict['ymin'][i]) + h, 
                              int(self.bboxDict['xmin'][i]) : int(self.bboxDict['xmin'][i]) + w]
                
                    filename = self.writepath + self.bboxDict['name'][i] + '_' + \
                                        self.bboxDict['xmin'][i] + '_' + self.bboxDict['ymin'][i] + \
                                        '_' + self.bboxDict['xmax'][i] + '_' + self.bboxDict['ymax'][i]
                
                    cv2.imwrite(filename + '-' + self.bboxDict['file'][i] + '.jpg', chip)
                    self.cnt += 1 ##cnt chips in this iteration
                    
                    return self.cnt