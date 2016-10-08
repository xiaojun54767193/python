#!/usr/bin/python
import requests,sys
from requests.auth import HTTPBasicAuth
r=requests.get('http://localhost:8080/api/v1/clusters/udpihadoop/',auth=HTTPBasicAuth('admin','admin'))
con=r.json()
if len(sys.argv)!=2:
	print '{0}:you must specify an argument,etiher critical_num or warn_num'.format(sys.argv[0])
	sys.exit()
if sys.argv[1]=='critical_num':
	print con['alerts_summary']['CRITICAL']
elif sys.argv[1]=='warn_num':
	print con['alerts_summary']['WARNING']
