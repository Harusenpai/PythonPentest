import sys
import urllib
import urllib2
from  time import sleep

url = 'http://192.168.168.168'
values = ({
          '0MKKey' : '%B5%C7%C2%BC%20Login',
          'DDDDD' : '1100B0100',
          'upass' : '226295'
         })
data = urllib.urlencode(values)
data = data.encode('utf-8')
def usage():
    print('''
Usage:

./drcom i    //log in 
./drcom o    //log out 
            ''')

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        usage()
        sys.exit()
    elif(sys.argv[1] == 'o'):
        l = urllib2.urlopen('http://192.168.168.168/F.htm')
        if (l):
            print('\nyou have loged out!\n')
            sys.exit()
    elif(sys.argv[1] == 'i'):
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        if(response):
            d = response.read()
            #print(d.decode("gb2312"))
            print('\nyou have loged in!!\n ')
            sys.exit()
    else:
        usage()
        sys.exit()
