# -*- coding: utf-8 -*-

import os, secrets

path = ".\\"
# extension = ('.mp4','.wmv','.mkv','.avi','.flv')
extension = ('.jpg', '.jpeg', '.png')
data = []

count = 0
while count < 5:
    file = (secrets.choice(os.listdir(path)))
    while file.lower().endswith(extension) is False:
        file = (secrets.choice(os.listdir(path)))
        print('File selected has an incorrect extension, retrying...')   
    
    if file not in data:
        print('Opening file: ' + path + file)
        os.startfile(path + file)
        data.append(file)
        count+=1
    else:
        print('File has already been opened')
        pass
