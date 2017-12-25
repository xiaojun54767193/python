#!/usr/bin/env python3
from datetime import date,datetime,timedelta
from multiprocessing import Process
import ftplib,os,logging
def reupload(srcdir):
	today = date.today()
	tm = timedelta(days=3)
	yestoday = today-tm
	ytd = yestoday.strftime('%Y%m%d')
	host = '10.245.1.236'
	user = 'nokia_ftp'
	Ftppass = 'nokia@2016'
	logging.basicConfig(filename='/var/log/upload.log',format='%(asctime)s %(message)s',level=logging.DEBUG)
	try:
		ftp=ftplib.FTP(host)
		ftp.set_debuglevel(0)
		ftp.login(user,Ftppass)
		ftp.cwd(os.path.join(srcdir,str(ytd)))
		with open('/tmp/reupload') as f:
			for file in f:
				fr = file.replace('\n','')
				dir,filename = os.path.split(fr)
				os.chdir(dir)
				ftp.storbinary('STOR %s' %filename,open(filename, 'rb'))
				logging.info('file %s upload success',filename)
	except ftplib.all_errors as e:
		logging.error('error occured,error message is %s',e)
	finally:
		ftp.quit()


if __name__ == '__main__':
	p = Process(target=reupload,args=('/home/XDR_FILE/data/XDR_BUCHUAN',))
	p.start()
	p.join()
