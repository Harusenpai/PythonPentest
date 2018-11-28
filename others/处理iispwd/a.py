import re
import http.client

def getResponseCode(url):
    conn = http.client.HTTPConnection(url,80,timeout=10)
    
    try:
        conn.request("GET", "/")
        r1 = conn.getresponse()
        return r1.status
    except:
        pass
    return 0
    
    
    
 
 

def Readiispwd(filename,domainlist):
    
    f = open(filename)
    for line in f:
        #print (line)
        line = line.split(' ')
        #print (line)
        try:
            
            if len(line)<4:
                pass
            else:
                homelocate=line[len(line)-1]
                #print (homelocate)
                
                domainstring=line[len(line)-2].split(':')
                #print(domainstring)
                for j in domainstring:
                    if len(j)<3:
                        pass
                    else:
                        j=j.split('.')
                        if len(j)==2:
                            domainname='.'.join(j)
                            domainname=domainname.split(',')[0]
                            
                            #print('%s\t%s'%(domainname,homelocate))
                            domainlist.append(domainname)
                            domainlist.append(homelocate)
                            
                            
                        else:
                            pass
            
            
        except IndexError:
            pass
    f.close()
############################################
domainlist=[]
Readiispwd('njwinweb10iispwd.txt',domainlist)
#print (domainlist)
print('200 response && domain domain location')
result=open("result.txt",'a')
for i in range(0,len(domainlist)-2,2):
    #print (i)
    if getResponseCode(domainlist[i])==200:
        result.write('%s\t%s\n'%(domainlist[i],domainlist[i+1]))
        print('%s\t%s'%(domainlist[i],domainlist[i+1]))
        
    
result.close()

