#!/usr/bin/env python3
import os,mysql.connector,socket
from datetime import timedelta,datetime
def statxdr(interval=1,path='/data02/unicom/groupBak'):
	difftime = timedelta(days=interval)
	xdrdate = (datetime.now() - difftime).strftime('%Y%m%d')
	xdrhour = (datetime.now() - difftime).strftime('%H')
	filelist = []
	dbuser = 'root'
	dbpass = 'root'
	dbbase = 'groupfile'
	server = '10.245.4.11'
	port = 3307
	host = socket.gethostbyname(socket.gethostname())
	xdrpath = os.path.join(path,xdrdate)
	if os.access(xdrpath,os.F_OK):
		for roots,dirs,files in os.walk(xdrpath):
			for file in files:
				if file.endswith('gz'):
					filename = os.path.join(roots,file)
					filelist.append(filename)
					
	try:
		conn = mysql.connector.connect(user=dbuser,password=dbpass,host=server,port=port,database=dbbase)
		cursor = conn.cursor()
		insert_stmt = ("insert into xdr_filename values (%s,%s,%s)")
		for f in filelist:
			data = (host,xdrdate,f)
			cursor.execute(insert_stmt,data)
		conn.commit()
		cursor.close()
		conn.close()
	except mysql.connector.Error as err:
		print('something wrong,the operation is not success,the reason is %s' %err)
if __name__ == '__main__':
	statxdr()
