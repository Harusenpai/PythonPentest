#encoding=utf-8
import os
import os.path
import sys
rootdir = "."                                   # 指明被遍历的文件夹
sufix='.txt'
thiefile=sys.argv[0][sys.argv[0].rfind(os.sep)+1:]

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:
        if thiefile!=filename:
            print filename
            st=str( os.path.join(parent,filename)) #输出文件路径信息
            r = "/".join(st[1:].split("\\"))
            sorpath="."+r
            os.rename(sorpath,sorpath+".txt")
 
    
