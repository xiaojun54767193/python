#!/usr/bin/env python3
#author: gouxiaojun
#date: 2017-12-25
#version: 2.0
#QQ: 547671930
#mail: xiaojun.gou@nnct-nsn.com
#add a switch to keep the original files or delete them
#remove the rename function,use queue to process the compress and rename tmp file,so that it can mitigate the io load,add timestamp to the log file
import time,os,tarfile,logging,sys,queue
from datetime import timedelta,datetime
from multiprocessing import Process,Queue
mq = Queue(-1)
class groupfile:
	"""rename and compress file
	"""
	difftime = timedelta(minutes=1)
	xdrdate = (datetime.now() - difftime).strftime('%Y%m%d')
	xdrhour = (datetime.now() - difftime).strftime('%H')

	def compress(self,path,destpath,keepfile=False):
		"""compress the files with gzip and after compress them rename the orignal files to another format filename
		"""
		self.path = path
		self.destpath = destpath	
		logging.basicConfig(filename='/var/log/group3.log',format='%(asctime)s %(message)s',level=logging.DEBUG)
		comppath = os.path.join(path,self.xdrdate,self.xdrhour,destpath)
		for roots,dir,File in os.walk(comppath):
			for f in File:
				if f.startswith('SC') and f.endswith('txt'):
					os.chdir(comppath)
					try:
						tmpfile = '%s.tar.gz.tmp' % os.path.join(comppath,f.replace('.txt',''))
						with tarfile.open(tmpfile,"w:gz",compresslevel=1) as tar:
							tar.add(f)
						qfile = os.path.join(comppath,tmpfile)
#put the compressed file into the queue
						mq.put(qfile)
#						print('put file in queue: ',qfile)
					except tarfile.TarError as tarerr:
						logging.error('some exceptions occoured when compress the file,and the error message is %s',tarerr)
					except tarfile.ReadError as readerr:
						logging.error('can not read the file,the error message is %s',readerr)
					except tarfile.CompressionError as compresserr:
						logging.error('can not compress the file,the error message is %s',compresserr)
					except tarfile.StreamError as streamerr:
						logging.error('can not compress the file,the error message is %s',streamerr)
					try:
						if not keepfile:
							os.remove(os.path.join(comppath,f))
						else:
							os.rename(f,'%s.orig' %f)
					except FileNotFoundError as err:
						logging.error('while rename the file to processed occoured error,the error messages is %s',err)

	def renametmp(self):
		"""rename the tmp gzip file to tar.gz so that the ftp can upload it
		"""
#get the messages from the queue to rename the files to tar.gz directly
		while True:
			try:
				refile = mq.get(timeout=10)
				os.rename(refile,refile.replace('.tmp',''))
#				print('get file out from queue: ',refile)
			except queue.Empty:
				sys.exit(11)

def main():
	"""the main function to execute the script
	"""
	cp = groupfile()
	path = '/data02/unicom/group'
	p1 = Process(target=cp.compress(path,'group_gn/gn_email'))
	p2 = Process(target=cp.compress(path,'group_gn/gn_others'))
	p3 = Process(target=cp.compress(path,'group_gn/gn_gen'))
	p4 = Process(target=cp.compress(path,'group_gn/gn_ftp'))
	p5 = Process(target=cp.compress(path,'group_gn/gn_p2p'))
	p6 = Process(target=cp.compress(path,'group_gn/gn_mms'))
	p7 = Process(target=cp.compress(path,'group_gn/gn_dns'))
	p8 = Process(target=cp.compress(path,'group_gn/gn_http'))
	p9 = Process(target=cp.compress(path,'group_gn/gn_voip'))
	p10 = Process(target=cp.compress(path,'group_gn/gn_rtsp'))
	p11 = Process(target=cp.compress(path,'group_gn/gn_im'))
	p12 = Process(target=cp.compress(path,'group_gn/gn_streaming'))
	p13 = Process(target=cp.compress(path,'group_s1u/s1u_email'))
	p14 = Process(target=cp.compress(path,'group_s1u/s1u_others'))
	p15 = Process(target=cp.compress(path,'group_s1u/s1u_gen'))
	p16 = Process(target=cp.compress(path,'group_s1u/s1u_ftp'))
	p17 = Process(target=cp.compress(path,'group_s1u/s1u_p2p'))
	p18 = Process(target=cp.compress(path,'group_s1u/s1u_mms'))
	p19 = Process(target=cp.compress(path,'group_s1u/s1u_dns'))
	p20 = Process(target=cp.compress(path,'group_s1u/s1u_http'))
	p21 = Process(target=cp.compress(path,'group_s1u/s1u_voip'))
	p22 = Process(target=cp.compress(path,'group_s1u/s1u_rtsp'))
	p23 = Process(target=cp.compress(path,'group_s1u/s1u_im'))
	p24 = Process(target=cp.compress(path,'group_s1u/s1u_streaming'))
	p25 = Process(target=cp.compress,args=(path,'group_s11'))
	p26 = Process(target=cp.compress,args=(path,'group_s6a'))
	p27 = Process(target=cp.compress,args=(path,'group_sgs'))
	p28 = Process(target=cp.compress,args=(path,'group_iucs'))
	p29 = Process(target=cp.compress,args=(path,'group_gnc'))
	p30 = Process(target=cp.compress,args=(path,'specail/ciloc'))
	p31 = Process(target=cp.compress,args=(path,'specail/mmecdr'))
	p32 = Process(target=cp.compress,args=(path,'specail/udpisms'))
	p33 = Process(target=cp.compress,args=(path,'specail/csfb'))
	p34 = Process(target=cp.compress,args=(path,'group_s1mme'))
	p35 = Process(target=cp.compress,args=(path,'group_iups'))
	p36 = Process(target=cp.compress,args=(path,'group_gb'))
	processlist = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,
	p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,
	p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36]

	for p in processlist:
		p.start()
	p.join()
	r1 = Process(target=cp.renametmp())
	r1.start()

if __name__ == '__main__':
	main()
