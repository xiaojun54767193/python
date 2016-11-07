#!/usr/bin/python
import os,shutil,threading
from datetime import date,timedelta
def jiya(clouddir,prefix,keepday=3):
	Today=date.today()
	D_keep=timedelta(days=keepday)
	Delday=Today-D_keep
	D_format=Delday.strftime('%Y%m%d')
	diclist=[]
	sday=[]
	ssuffix=[]
	for dir in os.listdir(clouddir):
		if dir.startswith(prefix):
			pos=dir.index('_')+1
			alldic=dir[pos:]
			diclist.append(alldic)
	diclist.sort()
	for a in diclist:
		spos=a.index('_')
		allday=a[:spos]
		alls=a[spos:]
		sday.append(allday)
		ssuffix.append(alls)
	Newlist=zip(sday,ssuffix)
	for file in Newlist:
		if file[0]<D_format:
			if os.access(os.path.join(clouddir,prefix+file[0]+file[1]),os.F_OK):
				shutil.rmtree(os.path.join(clouddir,prefix+file[0]+file[1]))
if __name__=='__main__':
	cloudtmpdir=['/data04/UAR4CloudTmp','/data06/UAR4CloudTmp','/data07/UAR4CloudTmp','/data08/UAR4CloudTmp','/data09/UAR4CloudTmp']
	prefixlist=['s11_','sgs_','s6a_','s1mme_']
	for tmpdir in cloudtmpdir:
		for Pre in prefixlist:
			deltmpjiya=threading.Thread(target=jiya,args=(tmpdir,Pre))
			deltmpjiya.start()
