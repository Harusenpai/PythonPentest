# -*- coding: utf-8 -*-
import os

os.chdir('d:\\tuniu.com\\ccc')    

if not os.path.exists('zbx_export_templates.xml'):
    exit(-1)                      

lll =['pay_site_wap','pay_csahier_wap']
for i in lll:
    sss=i
    ttt = sss.upper() 
    lines = open('zbx_export_templates.xml').readlines()

    fp = open(sss+'_export_templates.xml','w')  
    for s in lines:
           fp.write( s.replace('ala_api',sss).replace('ALA_API',ttt)) 
    fp.close() 
