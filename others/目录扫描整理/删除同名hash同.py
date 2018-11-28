# -*- coding: utf-8 -*- 

import os
import hashlib
from functools import partial
from os import walk

def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

hashl=list()


for dirpath, dirnames, filenames in walk('D:\\workspace\\目录扫描\\'):
    #print ('Directory', dirpath)
    for filename in filenames:
        print (' File', dirpath+filename) 
        try:
            md=md5sum(dirpath+filename)
            if md in hashl:
                os.remove(dirpath+filename)
            else:
                hashl.append(md)
                print(md)
        except FileNotFoundError:
            pass
        
            
        
            
        

        
                




#print(md5sum('c:\\windows\\IME\\SPTIP.DLL'))
