#!/usr/bin/env python
# encoding: utf-8
# 根据ip range和 header判断，合成的轮子。
# 使用方法./cdn_identify.py http://jiasule.com


from requests import session
from base64 import b64decode
import netaddr
from netaddr import IPNetwork, IPAddress
import socket
from urlparse import urlparse 

class Fingerprint(object):
    def __init__(self):
        self.s = session()
        self.s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'

    def detect(self, url):
        cdn_list = {'ips_cdn_cloudflare':['199.27.128.0/21','173.245.48.0/20','103.21.244.0/22','103.22.200.0/22','103.31.4.0/22','141.101.64.0/18','108.162.192.0/18','190.93.240.0/20','188.114.96.0/20','197.234.240.0/22','198.41.128.0/17','162.158.0.0/15','104.16.0.0/12'],
'ips_cdn_360': ['183.136.133.0-183.136.133.255','220.181.55.0-220.181.55.255','101.226.4.0-101.226.4.255','180.153.235.0-180.153.235.255','122.143.15.0-122.143.15.255','27.221.20.0-27.221.20.255','202.102.85.0-202.102.85.255','61.160.224.0-61.160.224.255','112.25.60.0-112.25.60.255','182.140.227.0-182.140.227.255','221.204.14.0-221.204.14.255','222.73.144.0-222.73.144.255','61.240.144.0-61.240.144.255','113.17.174.0-113.17.174.255','125.88.189.0-125.88.189.255','125.88.190.0-125.88.190.255','120.52.18.1-120.52.18.255'],
'ips_cdn_jiasule':['119.188.35.0-119.188.35.255','61.155.222.0-61.155.222.255','218.65.212.0-218.65.212.255','116.211.121.0-116.211.121.255','103.15.194.0-103.15.194.255','61.240.149.0-61.240.149.255','222.240.184.0-222.240.184.255','112.25.16.0-112.25.16.255','59.52.28.0-59.52.28.255','211.162.64.0-211.162.64.255','180.96.20.0-180.96.20.255','103.1.65.0-103.1.65.255'],
'ips_cdn_anquanbao' :['220.181.135.1-220.181.135.255','115.231.110.1-115.231.110.255','124.202.164.1-124.202.164.255','58.30.212.1-58.30.212.255','117.25.156.1-117.25.156.255','36.250.5.1-36.250.5.255','183.60.136.1-183.60.136.255','183.61.185.1-183.61.185.255','14.17.69.1-14.17.69.255','120.197.85.1-120.197.85.255','183.232.29.1-183.232.29.255','61.182.141.1-61.182.141.255','182.118.12.1-182.118.12.255','182.118.38.1-182.118.38.255','61.158.240.1-61.158.240.255','42.51.25.1-42.51.25.255','119.97.151.1-119.97.151.255','58.49.105.1-58.49.105.255','61.147.92.1-61.147.92.255','69.28.58.1-69.28.58.255','176.34.28.1-176.34.28.255','54.178.75.1-54.178.75.255','112.253.3.1-112.253.3.255','119.167.147.1-119.167.147.255','123.129.220.1-123.129.220.255','223.99.255.1-223.99.255.255','117.34.72.1-117.34.72.255','117.34.91.1-117.34.91.255','123.150.187.1-123.150.187.255','221.238.22.1-221.238.22.255','125.39.32.1-125.39.32.255','125.39.191.1-125.39.191.255','125.39.18.1-125.39.18.255','14.136.130.1-14.136.130.255','210.209.122.1-210.209.122.255','111.161.66.1-111.161.66.255'],
'ips_cdn_incapsula':['199.83.128.0/21','198.143.32.0/19','149.126.72.0/21','103.28.248.0/22','45.64.64.0/22','185.11.124.0/22 ','192.230.64.0/18'],
'ips_cdn_yunjiasu':['222.216.190.0-222.216.190.255','61.155.149.0-61.155.149.255','119.188.14.0-119.188.14.255','61.182.137.0-61.182.137.255','117.34.28.0-117.34.28.255','119.188.132.0-119.188.132.255','42.236.7.0-42.236.7.255','183.60.235.0-183.60.235.255','117.27.149.0-117.27.149.255','216.15.172.0/24']}

        cc = []
        try:
                ips = socket.gethostbyname_ex(url.split('/')[2])
        except socket.gaierror:
                ips=[]
        for ip_addr in ips[2]:
            for cdn in cdn_list:
                for cidr in cdn_list[cdn]:
                    if '-' in cidr:
                        l = cidr.split('-')
                        ip_range = netaddr.iter_iprange(l[0],l[1])
                        ip_range = netaddr.cidr_merge(ip_range)  
                        for i  in ip_range:
                            if ip_addr in i:
                                cc.append(cdn)
                            else:
                                pass 
                    else:
                        if ip_addr in cidr:
                            cc.append(cdn)
        print '------------cidr--------------'
        print cc
        resp = self.s.get(url, allow_redirects=False, verify=False)
        if resp.history:
            headers = resp.history[0].headers
            cookies = resp.history[0].cookies
        else:
            headers = resp.headers
            cookies = resp.cookies

        result = []
        for prop in dir(self):
            if prop.startswith('finger_'):
                func = getattr(self, prop)
                r = func(headers, cookies)
                if r:
                    result.append(r)
        print '------------header------------'
        print result            
        return result
    



        
    def finger_jiasule(self, headers, cookies):
        if '__jsluid' in cookies.keys():
            return 'jiasule'

    def finger_cloudflare(self, headers, cookies):
        if '__cfduid' in cookies.keys():
            return 'cloudflare'
        elif 'cloudflare' in headers.get('server', ''):
            return 'cloudflare'
        
    def finger_360webscan(self, headers, cookies):
        if 'webscan.360.cn' in headers.get('x-safe-firewall', ''):
            return '360webscan'

    def finger_360wzb(self, headers, cookies):
        if headers.get('x-powered-by-360wzb') != None:
            return '360wzb'

    def finger_anquanbao(self, headers, cookies):
        if headers.get('x-powered-by-anquanbao') != None:
            return 'anquanbao'

    def finger_incapsula(self, headers, cookies):
        if 'incapsula' in headers.get('x-cdn', '').lower():
            return 'incapsula'
        if any(map(lambda item: item.startswith(('incap_ses', 'visid_incap_')), cookies.keys())):
            return 'incapsula'

    def finger_yunjiasu(self, headers, cookies):
        x_server = headers.get('x-server', '')
        try:
            if b64decode(x_server).endswith('.fhl'):
                return 'yunjiasu'
        except:
            return

if __name__ == '__main__':
    from sys import argv

    f = Fingerprint()
    f.detect(argv[1]) 
