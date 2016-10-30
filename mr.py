#!/usr/bin/python
from datetime import date,timedelta,datetime
import sys,os,shutil,ftplib
class mrservice:
	'''
	Class for mr service,now,it is include get mr files from remote ftp server
	and delete mr directories which older than a month
	'''
	def getmr(self,remotedic,localdic):
		"""
		get mr file from remote ftp server and put it in the local machine's data directory
		"""
		self.remotedic=remotedic
		self.localdic=localdic
		today=date.today()
		tm=timedelta(days=1)
		yestoday=today-tm
		ytd=yestoday.strftime('%Y%m%d')
		host='10.245.1.249'
		user='nokia_mr'
		passwd='nokia@2016'
		if not os.access(os.path.join(localdic,str(ytd)),os.F_OK):
			os.makedirs(os.path.join(localdic,str(ytd)))
		try:
			ftp=ftplib.FTP(host)
			ftp.login(user,passwd)
			ftp.cwd(os.path.join(remotedic,str(ytd)))
			file=ftp.nlst()
			for f in file:
				ftp.retrbinary('RETR %s' %f, open('%s/%s' %(os.path.join(localdic,str(ytd)),f), 'wb').write)
		except ftplib.all_errors,e:
			print 'Ftp error occured!'
			print 'The error is: {0}'.format(e)
		finally:
			ftp.quit()
	def delmr(self,dir,keepday=30):
		"""
		delete the mr directory which older than a month
		"""
		self.dir=dir
		self.keepday=keepday
		Today=date.today()
		D_keep=Today-timedelta(days=keepday)
		D_format=D_keep.strftime('%Y%m%d')
		Dir=os.listdir(dir)
		for dic in Dir:
			if dic < D_format:
				shutil.rmtree(os.path.join(dir,dic))
if __name__=='__main__':
	Get=mrservice()
	Del=mrservice()
	Get.getmr('/MR_139/Zte_OMC01','/data/MR_139/Zte_OMC01')
	Get.getmr('/MR_139/Eric_OMC03/stat','/data/MR_139/Eric_OMC03/stat')
	Get.getmr('/MR_139/Eric_OMC03/orig','/data/MR_139/Eric_OMC03/orig')
	Get.getmr('/MR_139/Nokia_OMC01','/data/MR_139/Nokia_OMC01')
	Get.getmr('/MR/orig','/data/mr/orig')
	Get.getmr('/MR/stat','/data/mr/stat')
	Del.delmr('/data/MR_139/Zte_OMC01')
	Del.delmr('/data/mr/orig')
	Del.delmr('/data/mr/stat')
	Del.delmr('/data/MR_139/Eric_OMC03/orig')
	Del.delmr('/data/MR_139/Eric_OMC03/stat')
	Del.delmr('/data/MR_139/Nokia_OMC01')
