#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate chips
Input: Annotations and JPEGImages
Output: Chips
@author: avasquez
"""
import os
import cv2
import xml.etree.ElementTree as ET

class GetBboxDict:
    def __init__(self, file, annotpath, imagepath, bboxArea, percentDeviation, classNamesFile):
        self.file = file
        self.annotpath = annotpath
        self.imagepath = imagepath
        self.bboxArea = bboxArea
        self.percentDeviation = percentDeviation
        self.classNamesFile = classNamesFile
            
    ##gets chip coords from XML file
    def chipDict(self):
        tree = ET.parse(self.annotpath + self.file)
        root = tree.getroot()
        pre, _ =  os.path.splitext(self.file)
        
        self.bboxDict = {'name':[], 'xmin':[], 'ymin':[], 'xmax':[], 'ymax':[], 
                       'file': [], 'imagepath': [],'annotpath': [], 
                       'imageHeight': [], 'imageWidth': [], 'imageDepth': [],
                       'image': []}
    
        if os.path.exists(self.classNamesFile):
            with open(self.classNamesFile, 'r') as f:
                classnames = f.readlines()
                classnames = [i.strip('\n') for i in classnames]
        else:
            classnames = None
        
        # print(self.imagepath + pre + '.jpg')
        image = cv2.imread(self.imagepath + pre + '.jpg')
        imageHeight, imageWidth, imageDepth = image.shape
        
        for elem in root.iter('name'): 
            if elem.text in classnames:
                self.bboxDict['name'].append(elem.text)
                self.bboxDict['file'].append(pre)
                self.bboxDict['annotpath'].append(self.annotpath)
                self.bboxDict['imagepath'].append(self.imagepath)
                self.bboxDict['imageHeight'].append(imageHeight)
                self.bboxDict['imageWidth'].append(imageWidth)
                self.bboxDict['imageDepth'].append(imageDepth)
                self.bboxDict['image'].append(image)
                
                
        for elem in root.iter('xmin'):
            self.bboxDict['xmin'].append(elem.text) 
        for elem in root.iter('ymin'): 
            self.bboxDict['ymin'].append(elem.text)
        for elem in root.iter('xmax'):
            self.bboxDict['xmax'].append(elem.text)
        for elem in root.iter('ymax'): 
            self.bboxDict['ymax'].append(elem.text)
        return self.bboxDict
    
    def filterChipDict(self):
        for i in range(len(self.bboxDict['name'])):
            try: ##there may be nothin in the annotations, so pass
                w = int(self.bboxDict['xmax'][i]) - int(self.bboxDict['xmin'][i])
                h = int(self.bboxDict['ymax'][i]) - int(self.bboxDict['ymin'][i])
    
                if self.bboxArea:
                    upperBound = w*h + w*h*self.percentDeviation
                    lowerBound = w*h - w*h*self.percentDeviation
                    
                    if self.bboxArea <= upperBound and self.bboxArea >= lowerBound:
                        continue ##do nothing if criteria met
                    else: ##delete items from dictionary
                        self.bboxDict['name'][i] = None
                        self.bboxDict['xmin'][i] = None
                        self.bboxDict['ymin'][i] = None
                        self.bboxDict['xmax'][i] = None
                        self.bboxDict['ymax'][i] = None
                        self.bboxDict['file'][i] = None
                        self.bboxDict['annotpath'][i] = None
        
                else: ##do nothing since size is not a priority
                    continue
            except:
                pass 
        return self.bboxDict