# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:07:32 2019

@author: NewOffice3
"""

#find out what is happening with file read in
import os
from glob import glob
import cv2

train_path = "images/train/"
#print(os.path)
imlist = {}
count = 0 
for each in glob(os.path.join(train_path,"*")):
    word = os.path.split(each)[1]
    print(" #### Reading image category ", word, " ##### ")
    imlist[word] = []
    with os.scandir(os.path.join(train_path,word)) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                print(os.path.join(train_path,word,entry.name))
                im = cv2.imread(os.path.join(train_path,word,entry.name), 0)
                imlist[word].append(im)
                count +=1