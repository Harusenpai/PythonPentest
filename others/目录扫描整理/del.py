#-*- coding: UTF-8 -*-
import shutil
import os 

def delrep(source):
 
    destination =  source+'rdv_bak'

    lines_seen = set() 
    outfile = open("temp.xxoo", "w")
    
    for line in open(source, "r"):
        #print(line)
        if line not in lines_seen: 
            outfile.write(line)
            lines_seen.add(line)

    outfile.close()
    os.renames(source,destination)
    os.renames( "temp.xxoo",source)

from os import walk
for dirpath, dirnames, filenames in walk('D:\\workspace\\目录扫描\\url字典\\'):
    #print ('Directory', dirpath)
    for filename in filenames:
        print (' File', dirpath+filename)
        if filename.split('.')[-1]=='txt' or filename.split('.')[-1]=='list':
            
            delrep(dirpath+filename)
        else:
            pass

