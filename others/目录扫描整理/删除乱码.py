# -*- coding: utf-8 -*- 
import codecs
#f =  codecs.open('D:\\workspace\\目录扫描\\布神php路径adminphp.txt')
fileHandler = open('D:\\workspace\\目录扫描\\布神php路径adminphp (2).txt', 'r')	#以读写方式处理文件IO
fileHandler.seek(0)


for i in range(1,10000):
        try:
            line = fileHandler.readline(i)
            print (line)
        except UnicodeDecodeError:
            print('xxxxx')
        

fileHandler.close
 
