#encoding=utf-8
import os,sys,time
from stat import *
import os.path
rootdir = "."                                   # 指明被遍历的文件夹

TimeForChange = '2015-05-20 13:14:01'
ConverTime = time.mktime(time.strptime( TimeForChange,'%Y-%m-%d %H:%M:%S') )
times=(ConverTime,ConverTime)

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:                        #输出文件信息
        st=str( os.path.join(parent,filename)) #输出文件路径信息
        r = "/".join(st[1:].split("\\"))
        filename = '.'+r
        os.utime(filename, times)
        #r.replace('ala_api',sss).replace('ALA_API',ttt)
        print filename
        #result.write(r+'\n')

    
#result.close()
