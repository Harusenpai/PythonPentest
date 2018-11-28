#encoding=utf8
import urllib
import urllib2
import cookielib
import Cookie
from cookielib import Cookie as libcookie

def parse(rawstr,url):
	url = '.'+'.'.join(url.split('.')[1:])
	c = Cookie.SimpleCookie()
	c.load(rawstr)
	ret = []
	for k in c:
		#get v as Morsel Object
		v = c[k]
		ret.append(libcookie(
					name=v.key,
					value = v.value,
					version=0,
					port=None,
					port_specified = False,
					domain=url, 
					domain_specified=True, 
					domain_initial_dot=True, 
					path='/', 
					path_specified=True, 
					secure=False, 
					expires=None, 
					discard=False, 
					comment=None, 
					comment_url=None, 
					rest={'HttpOnly': None}, 
					rfc2109=False,
		))
	return ret




###登录页的url
#lgurl = 'http://.com/ogi09'


###用cookielib模块创建一个对象，再用urlllib2模块创建一个cookie的handler
cookie = cookielib.CookieJar()
cs = parse("JSESSIONID=DC0B117570736F7120EF4679B1C06797",".com")
for c in cs:
	cookie.set_cookie(c)
print cookie
cookieProc = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookieProc)
urllib2.install_opener(opener)

###有些网站反爬虫，这里用headers把程序伪装成浏览器
hds = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36' }  

###登录需要提交的表单
 
 
#req = urllib2.Request(url = lgurl,headers = hds) #伪装成浏览器，访问该页面，并POST表单数据，这里并没有实际访问，只是创建了一个有该功能的对象
#opener = urllib2.build_opener(cookie_handler) #绑定handler，创建一个自定义的opener
#response = opener.open(req)#请求网页，返回句柄
#page = response.read()#读取并返回网页内容

f =  open('data.txt', 'a')
for i in range(1,3956):
    print i
    dataurl = "http://l" % i
    req1 = urllib2.Request(url = dataurl,data = '',headers = hds)
    resp = opener.open(req1)
    page = resp.read()
    f.write(page)
    f.write("\n")
    print "\n"
    
f.close()
#print page #打印到终端显示
