# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:15:54 2020

@author: Wilson
"""

import os, secrets

path = "./"
#extension = ('.mp4','.wmv','.mkv','.avi','.flv')
extension = ('jpg','jpeg','png')

count = 0
while count < 5:
    file = (secrets.choice(os.listdir(path)))
    while file.lower().endswith(extension) is False:
        file = (secrets.choice(os.listdir(path)))
        print('File selected has an incorect extension, retrying...')   

    print('Opening file: ' + path + file)
    os.startfile(path + file)
    count+=1
