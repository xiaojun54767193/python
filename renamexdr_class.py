#!/usr/local/python3/bin/python3
#author: gouxiaojun
#date: 2017-07-27
#version: 1.0
#QQ: 547671930
#mail: xiaojun.gou@nnct-nsn.com
import time,os,tarfile,logging
from datetime import timedelta,datetime
from multiprocessing import Process
class groupfile:
	"""rename and compress file
	"""
	difftime = timedelta(minutes=5)
	xdrdate = (datetime.now() - difftime).strftime('%Y%m%d')
	xdrhour = (datetime.now() - difftime).strftime('%H')

	def renamefile(self,xdrtype,xdrdir,localdir='/data04/unicom/group',suffix='txt'):
		"""rename the original files to the specified filename format
		"""
		self.xdrtype = xdrtype
		self.xdrdir = xdrdir
		self.localdir = localdir
		self.suffix = suffix
		fileprefix = 'SC_CD_MOBILE_CNOS_NOKIA_CXDR_RNC003_0005_'
		xdrpath = os.path.join(localdir,self.xdrdate,self.xdrhour,xdrdir)
		logtime = time.ctime()
		filetime = []
		tag = []
		smallfile = []
		logging.basicConfig(filename='/var/log/group.log',level=logging.DEBUG)
		if os.access(xdrpath,os.F_OK):
			for root,dirs,files in os.walk(xdrpath):
				for file in files:
					if file.startswith(xdrtype) and file.endswith(suffix):
						timestart = file.index('0') + 1
						filetime.append(file[timestart:-13])
						tag.append(file[-13:])
			if len(tag) != 0:
				for t in zip(filetime,tag):
					smallfile.append(t)
				smallfile.sort()
				for small in smallfile:
					try:
						filename = fileprefix + small[0] + '_' + xdrtype.replace('_','') + '_' + small[1][-13:-4] + '_0' + '.txt'
						os.rename(os.path.join(xdrpath,'%s_280' %xdrtype + small[0] + small[1]),os.path.join(xdrpath,filename)) #rename the file
					except FileNotFoundError as err:
						logging.error('%s: somefile not found,the error message is %s',time.ctime(),err)
#			else:
#				logging.warning('%s there are no files in the %s,the program will exit now',time.ctime(),xdrpath)
#		else:
#			logging.warning('%s the directory %s is not exist',time.ctime(),xdrpath)

	def compress(self,path,destpath):
		"""compress the files with gzip and after compress them rename the orignal files to another format filename
		"""
		self.path = path
		self.destpath = destpath	
		comppath = os.path.join(path,self.xdrdate,self.xdrhour,destpath)
		for roots,dir,File in os.walk(comppath):
			for f in File:
				if f.startswith('SC') and f.endswith('txt'):
					os.chdir(comppath)
					try:
						with tarfile.open('%s.tar.gz.tmp' % os.path.join(comppath,f.replace('.txt','')),"w:gz",compresslevel=1) as tar:
							tar.add(f)
					except tarfile.TarError as tarerr:
						logging.error('%s: some exceptions occoured when compress the file,and the error message is %s',time.ctime(),tarerr)
					except tarfile.ReadError as readerr:
						logging.error('%s: can not read the file,the error message is %s',time.ctime(),readerr)
					except tarfile.CompressionError as compresserr:
						logging.error('%s: can not compress the file,the error message is %s',time.ctime(),compresserr)
					except tarfile.StreamError as streamerr:
						logging.error('%s: can not compress the file,the error message is %s',time.ctime(),streamerr)
					try:
						os.rename(f,'%s.orig' %f)
					except FileNotFoundError as err:
						logging.error('%s while rename the file to processed occoured error,the error messages is %s',time.ctime(),err)

	def renametmp(self,tmppath,tmpdestpath):
		"""rename the tmp gzip file to tar.gz so that the ftp can upload it
		"""
		self.tmppath = tmppath
		self.tmpdestpath = tmpdestpath
		filepath = os.path.join(tmppath,self.xdrdate,self.xdrhour,tmpdestpath)
		for root,dir,files in os.walk(filepath):
			for file in files:
				if file.startswith('SC') and file.endswith('tmp'):
					try:
						os.chdir(filepath)
						os.rename(file,file.replace('.tmp',''))
					except FileNotFoundError as err:
						logging.error('%s while rename the tmp file,some file not found,the error message is %s',time.ctime(),err)


def main():
	"""the main function to execute the script
	"""
	a = groupfile()
	p1 = Process(target=a.renamefile,args=('GnC','group_gnc'))
	p2 = Process(target=a.renamefile,args=('CILOC','special/ciloc'))
	p3 = Process(target=a.renamefile,args=('MMECDR','special/mmecdr'))
	p4 = Process(target=a.renamefile,args=('S11','group_s11'))
	p5 = Process(target=a.renamefile,args=('S6a','group_s6a'))
	p6 = Process(target=a.renamefile,args=('SGs','group_sgs'))
	p7 = Process(target=a.renamefile,args=('IuCS','group_iucs'))
	p8 = Process(target=a.renamefile,args=('Gn_EMAIL','group_gn/gn_email'))
	p9 = Process(target=a.renamefile,args=('Gn_OTHERS','group_gn/gn_others'))
	p10 = Process(target=a.renamefile,args=('Gn','group_gn/gn_gen'))
	p11 = Process(target=a.renamefile,args=('Gn_FTP','group_gn/gn_ftp'))
	p12 = Process(target=a.renamefile,args=('Gn_P2P','group_gn/gn_p2p'))
	p13 = Process(target=a.renamefile,args=('Gn_MMS','group_gn/gn_mms'))
	p14 = Process(target=a.renamefile,args=('Gn_DNS','group_gn/gn_dns'))
	p15 = Process(target=a.renamefile,args=('Gn_HTTP','group_gn/gn_http'))
	p16 = Process(target=a.renamefile,args=('Gn_VOIP','group_gn/gn_voip'))
	p17 = Process(target=a.renamefile,args=('Gn_RTSP','group_gn/gn_rtsp'))
	p18 = Process(target=a.renamefile,args=('S1U_EMAIL','group_s1u/s1u_email'))
	p19 = Process(target=a.renamefile,args=('S1U_OTHERS','group_s1u/s1u_others'))
	p20 = Process(target=a.renamefile,args=('S1U','group_s1u/s1u_gen'))
	p21 = Process(target=a.renamefile,args=('S1U_FTP','group_s1u/s1u_ftp'))
	p22 = Process(target=a.renamefile,args=('S1U_P2P','group_s1u/s1u_p2p'))
	p23 = Process(target=a.renamefile,args=('S1U_MMS','group_s1u/s1u_mms'))
	p24 = Process(target=a.renamefile,args=('S1U_DNS','group_s1u/s1u_dns'))
	p25 = Process(target=a.renamefile,args=('S1U_HTTP','group_s1u/s1u_http'))
	p27 = Process(target=a.renamefile,args=('S1U_VOIP','group_s1u/s1u_voip'))
	p28 = Process(target=a.renamefile,args=('S1U_RTSP','group_s1u/s1u_rtsp'))
	processlist = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p27,p28]
	for p in processlist:
		p.start()
	p.join()

if __name__ == '__main__':
	main()
