#encoding=utf8
import re

f = open("../log1.txt")             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
count=1
while line:
    #print count
    #count=count+1
    #print line,                 # 后面跟 ',' 将忽略换行符
    name=re.findall(r"Account Name:\s{2}(.*)\r\r",str(line))
    sourceip=re.findall(r"Source Network Address:\s(.*)\r\r",str(line))
    if sourceip:
        print sourceip
    if name:    
        print name  
    #print type(line)
    # print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()

f.close()
