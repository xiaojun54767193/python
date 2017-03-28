#!/usr/bin/python
from datetime import timedelta,date,datetime
import os,socket
import mysql.connector
server = '10.245.1.16'
dbuser = 'root'
dbpass = '123456'
dbbase = 'xdr_report'
host = socket.gethostname()
needhour = timedelta(hours=1)
dirprex = '/data05/databak/pfmBak'
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
try:
	conn = mysql.connector.connect(user=dbuser,password=dbpass,host=server,database=dbbase)
	cursor = conn.cursor()
	if len(s11) > 0:
		cursor.execute('insert into s11 values (%s,%s,%s,%s)',[host,day,hour,len(s11)])
	if len(s1u) > 0:
		cursor.execute('insert into s1u values (%s,%s,%s,%s)',[host,day,hour,len(s1u)])
	if len(s1mme) > 0:
		cursor.execute('insert into s1mme values (%s,%s,%s,%s)',[host,day,hour,len(s1mme)])
	if len(sgs) > 0:
		cursor.execute('insert into sgs values (%s,%s,%s,%s)',[host,day,hour,len(sgs)])
	if len(s6a) > 0:
		cursor.execute('insert into s6a values (%s,%s,%s,%s)',[host,day,hour,len(s6a)])
except mysql.connector.Error as err:
	print("Something went wrong: {}".format(err))
finally:
	conn.close()
