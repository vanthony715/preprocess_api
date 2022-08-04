# -*- coding: utf-8 -*-
"""
Resizes images in a specified directory
    
@author: avasquez
"""
import os
import time
import shutil
import cv2
import argparse
from tqdm import tqdm

class ResizeImages:
    def __init__(self, filepath, writepath, resizeWidth, resizeHeight):
        self.filepath = filepath
        self.writepath = writepath
        self.resizeWidth = resizeWidth
        self.resizeHeight = resizeHeight
        
    def resize(self):
        fileCnt = 0
        dim = (self.resizeWidth, self.resizeHeight)
        for file in tqdm(os.listdir(self.filepath), desc='Resizing Images', colour = 'blue'): 
            chip = cv2.imread(self.filepath + file)
            resizedChip = cv2.resize(chip, dim)
            cv2.imwrite(self.writepath + file, resizedChip)
            fileCnt+=1
        return fileCnt

parser = argparse.ArgumentParser()

parser.add_argument('--imagepath', default='./JPEGImages/', type=str,
                    help='path to folder that contains chips')

parser.add_argument('--writepath', default='./resizedChips64x64/', type=str,
                    help='path to folder that contains chips')

parser.add_argument('--resizeWidth', default=64, type=int,
                    help='Size to resize image width')

parser.add_argument('--resizeHeight', default=64, type=int,
                    help='size to resize image height')

if __name__ == "__main__":
     ##start clock
    tic = time.time()
    
    args = parser.parse_args()
    
    print('\n ************************ Job Description ************************')
    print('Resize Images')
    print('Image Path: ', args.imagepath)
    print('write Path: ', args.writepath)
    print('Resize Width: ', args.resizeWidth)
    print('Resize Height: ', args.resizeHeight)
    print(' *****************************************************************')
    
    if os.path.isdir(args.writepath):
        print('\nWritePath Exists')
    else:
        print('\nCreating Write Path Folder: ', args.writepath)
        os.mkdir(args.writepath)
        
    fileCnt = ResizeImages(args.imagepath, args.writepath, args.resizeWidth, args.resizeHeight).resize()
    
    print('\nNumber of Files Resized: ', fileCnt)
    ##print elapsed time
    tf = round((time.time() - tic), 1)
    print('\nTime to Run (s): ', tf)