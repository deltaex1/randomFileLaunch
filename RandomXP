# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:15:54 2020

@author: Wilson
"""

import os, random

path = "X:\\"
#extension = ('.mp4','.wmv','.mkv','.avi','.flv')
extension = ('jpg','jpeg','png')

count = 0
while count < 5:
    file = (random.choice(os.listdir(path)))
    while file.lower().endswith(extension) is False:
        file = (random.choice(os.listdir(path)))
        print('File selected has an incorect extension, retrying...')   

    print('Opening file: ' + path + file)
    os.startfile(path + file)
    count+=1
