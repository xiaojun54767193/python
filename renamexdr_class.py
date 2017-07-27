#!/usr/local/python3/bin/python3
#author: gouxiaojun
#date: 2017-07-27
#version: 1.0
#QQ: 547671930
#mail: xiaojun.gou@nnct-nsn.com
import time,os,tarfile,logging
from datetime import timedelta,datetime
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
		logging.basicConfig(filename='/var/log/movefile.log',level=logging.DEBUG)
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
						filename = fileprefix + small[0] + '_' + xdrtype + '_' + small[1][-13:-4] + '_0' + '.txt'
						os.rename(os.path.join(xdrpath,'%s_280' %xdrtype + small[0] + small[1]),os.path.join(xdrpath,filename)) #rename the file
					except FileNotFoundError as err:
						logging.error('%s: somefile not found,the error message is %s',time.ctime(),err)
			else:
				logging.warning('%s there are no files in the %s,the program will exit now',time.ctime(),xdrpath)
		else:
			logging.warning('%s the directory %s is not exist',time.ctime(),xdrpath)

	def compress(self,path,destpath):
		"""compress the files with gzip and after compress them rename the orignal files to another format filename
		"""
		self.path = path
		self.destpath = destpath	
		logging.basicConfig(filename='/tmp/compress.log',level=logging.DEBUG)
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
	a.renamefile('S1MME','group_s1mme','/tmp/unicom/group')
	a.compress('/tmp/unicom/group','group_s1mme')
	a.renametmp('/tmp/unicom/group','group_s1mme')
	a.renamefile('IuPS','group_iups','/tmp/unicom/group')
	a.compress('/tmp/unicom/group','group_iups')
	a.renametmp('/tmp/unicom/group','group_iups')
	a.renamefile('S1U_IM','group_s1u/s1u_im','/tmp/unicom/group')
	a.compress('/tmp/unicom/group','group_s1u/s1u_im')
	a.renametmp('/tmp/unicom/group','group_s1u/s1u_im')

if __name__ == '__main__':
	main()
