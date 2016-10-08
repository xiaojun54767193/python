#!/usr/bin/python
from datetime import date,datetime,timedelta
import ftplib,os
def mr(srcdir,destdir):
	"""
	get mr file from remote ftp server and put it in the local machine's data directory
	"""
	today=date.today()
	tm=timedelta(days=1)
	yestoday=today-tm
	ytd=yestoday.strftime('%Y%m%d')
	host='10.245.1.249'
	user='nokia_mr'
	Ftppass='nokia@2016'
#	dir1='/data/mr/orig/'+str(ytd)
#	dir2='/data/mr/stat/'+str(ytd)
	if not os.access(os.path.join(destdir,str(ytd)),os.F_OK):
		os.makedirs(os.path.join(destdir,str(ytd)))
	try:
		ftp=ftplib.FTP(host)
		ftp.login(user,Ftppass)
		ftp.cwd(os.path.join(srcdir,str(ytd)))
		file=ftp.nlst()
		for f in file:
			ftp.retrbinary('RETR %s' %f, open('%s/%s' %(os.path.join(destdir,str(ytd)),f), 'wb').write)
	except ftplib.all_errors,e:
		print 'Ftp error occured!'
		print 'The error is: {0}'.format(e)
	finally:
		ftp.quit()
if __name__=="__main__":
	mr('/MR_139/Eric_OMC03/stat','/data/MR_139/Eric_OMC03/stat')
	mr('/MR_139/Eric_OMC03/orig','/data/MR_139/Eric_OMC03/orig')
	mr('/MR_139/Nokia_OMC01','/data/MR_139/Nokia_OMC01')
	mr('/MR_139/Zte_OMC01','/data/MR_139/Zte_OMC01')
	mr('/MR/orig','/data/mr/orig')
	mr('/MR/stat','/data/mr/stat')
