# -*- coding: utf-8 -*-
import os

os.chdir('d:\\')       # 指定目录
if not os.path.exists('pp.txt'): # 看一下这个文件是否存在
    exit(-1)                             #，不存在就退出

lines = open('pp.txt').readlines()  #打开文件，读入每一行

fp = open('pp2.txt','w')  #打开你要写得文件pp2.txt
for s in lines:
       fp.write( s.replace('love','hate').replace('yes','no'))   #替换两次
fp.close() 
