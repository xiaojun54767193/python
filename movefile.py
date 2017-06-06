#!/usr/local/python3/bin/python3
import os,time,tarfile,threading,time,logging
from datetime import timedelta,date,datetime
def movefile(xdrtype,localdir,xdrdir):
	"""
	rename the xdr files and compress them with tar.gz fromat
	"""
	fileprefix = 'SC_CD_MOBILE_CNOS_NOKIA_CXDR_RNC003_0005_'
	Time = []
	tag = []
	smallfile = []
	timediff = timedelta(minutes=5)
	xdrdate = (datetime.now() - timediff).strftime('%Y%m%d')
	xdrtime = (datetime.now() - timediff).strftime('%H')
	xdrpath = os.path.join(localdir,xdrdate,xdrtime,xdrdir)
	logging.basicConfig(filename='/var/log/movefile.log',level=logging.DEBUG)
	logging.debug('at %s begin to process %s files',time.ctime(),xdrtype)
	if os.access(xdrpath,os.F_OK):
		for root,dirs,files in os.walk(xdrpath):
			for file in files:
				if file.startswith(xdrtype) and file.endswith('txt'):
					timestart = file.index('0') + 1
					Time.append(file[timestart:-13])
					tag.append(file[-13:])
		if len(tag) != 0:
			for t in zip(Time,tag):
				smallfile.append(t)
#sort the file so that can process them in time
			smallfile.sort()
			for small in smallfile:
				try:
					os.rename(os.path.join(xdrpath,'%s_280' %xdrtype + small[0] + small[1]),os.path.join(xdrpath,fileprefix + small[0] + '_' + xdrtype + '_' + small[1][-13:-4] + '_0' + '.txt'))
					logging.debug('%s: rename file %s to %s',time.ctime(),'%s_280' %xdrtype + small[0] + small[1],fileprefix + small[0] + '_' + xdrtype + '_' + small[1][-13:-4] + '_0' + '.txt')
				except FileNotFoundError as err:
					logging.warning('%s: somefile not found,the error message is %s',time.ctime(),err)
				try:
					with tarfile.open("%s/%s%s_%s_%s_0.tar.gz" %(xdrpath,fileprefix,small[0],xdrtype,small[1][-13:-4]),"w:gz",compresslevel=3) as tar:
						tar.add(os.path.join(xdrpath,fileprefix + small[0] + '_' + xdrtype + '_' + small[1][-13:-4] + '_0' + '.txt'),recursive=False)
					logging.debug('%s: compress file %s',time.ctime(),fileprefix + small[0] + '_' + xdrtype + '_' + small[1][-13:-4] + '_0' + '.txt')
				except tarfile.TarError as tarerr:
					logging.warning('%s: some exceptions occoured when compress the file,and the error message is %s',time.ctime(),tarerr)
			logging.debug('%s: process %s files complete',time.ctime(),xdrtype)
		else:
			logging.warning('%s there are no files in the %s,the program will exit now',time.ctime(),xdrpath)
	else:
		logging.warning('%s the directory %s is not exist',time.ctime(),xdrpath)
threads = []
move_s11_job = threading.Thread(target=movefile,args=('S11','/data04/unicom/group','group_s11'))
threads.append(move_s11_job)
move_s6a_job = threading.Thread(target=movefile,args=('S6a','/data04/unicom/group','group_s6a'))
threads.append(move_s6a_job)
move_sgs_job = threading.Thread(target=movefile,args=('SGs','/data04/unicom/group','group_sgs'))
threads.append(move_sgs_job)
move_mme_job = threading.Thread(target=movefile,args=('S1MME','/data04/unicom/group','group_s1mme'))
threads.append(move_mme_job)

if __name__ == "__main__":
	for job in threads:
		job.start()
	job.join()
