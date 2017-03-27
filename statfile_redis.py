#!/usr/bin/python
from datetime import timedelta,date,datetime
import os,redis
expiretime = 604800
server = '10.245.1.16'
host = 'logs17'
r = redis.StrictRedis(host=server,port=6379,db=0)
needhour = timedelta(hours=1)
dirprex = '/data05/databak/pfmBak'
#day = date.today().strftime('%Y%m%d')
curenthour = datetime.now()
day = (curenthour-needhour).strftime('%Y%m%d')
hour = (curenthour-needhour).strftime('%H')
dir = os.path.join(os.path.join(os.path.join(dirprex,day),hour),'lte')
for subdir in os.listdir(dir):
	if subdir == 's11':
		s11=os.listdir(os.path.join(dir,subdir))
	elif subdir == 'sgs':
		sgs=os.listdir(os.path.join(dir,subdir))
	elif subdir == 's6a':
		s6a=os.listdir(os.path.join(dir,subdir))
	elif subdir == 's1_u':
		s1u=os.listdir(os.path.join(dir,subdir))
	elif subdir == 's1_mme':
		s1mme=os.listdir(os.path.join(dir,subdir))
for xdr in ['s11','s1u','s1mme','s6a','sgs']:
	if len(xdr) > 0:
		name = '%s:%s:%s' %(day,hour,host)
		mapping = {xdr:len(xdr)}
	r.hmset(name=name,mapping=mapping)
	r.expire(name=name,time=expiretime)
