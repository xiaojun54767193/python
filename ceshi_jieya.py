#!/usr/local/python3/bin/python3
import glob,os,tarfile,logging
from multiprocessing import Process
def jieya(type):
	logging.basicConfig(filename='/var/log/MYjieyaerror',level=logging.ERROR)
	files = glob.glob('/data02/group/%s/*20170831*.gz' % type)
	for file in files:
		try:
			tar = tarfile.open(file,'r:gz')
			for tarinfo in tar:
				print(tarinfo.name)
		except EOFError:
			logging.error('%s has errors',file)

p1 = Process(target=jieya,args=('CILOC',))
p2 = Process(target=jieya,args=('CSFB',))
p3 = Process(target=jieya,args=('GB',))
p4 = Process(target=jieya,args=('GB_IUPS',))
p5 = Process(target=jieya,args=('GN',))
p6 = Process(target=jieya,args=('GN_C',))
p7 = Process(target=jieya,args=('MC',))
p8 = Process(target=jieya,args=('MMECDR',))
p9 = Process(target=jieya,args=('S11',))
p10 = Process(target=jieya,args=('S1MME',))
p11 = Process(target=jieya,args=('S1U',))
p12 = Process(target=jieya,args=('S6A',))
p13 = Process(target=jieya,args=('SGS',))
p14 = Process(target=jieya,args=('SMS',))

processlist = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14]
for p in processlist:
	p.start()
p.join()
