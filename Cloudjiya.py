#!/usr/bin/python
import os
def cloudjiya(clouddir,prefix):
	diclist=[]
	for dir in os.listdir(clouddir):
		if dir.startswith(prefix):
			pos=dir.index('_')+1
			alldic=dir[pos:]
			diclist.append(alldic)
	print 'The oldest %s in the %s is %s' %(prefix,clouddir,os.path.join(clouddir,'%s%s'%(prefix,min(diclist))))
if __name__=='__main__':
	cloudtmpdir=['/data04/UAR4CloudTmp','/data06/UAR4CloudTmp','/data07/UAR4CloudTmp','/data08/UAR4CloudTmp','/data09/UAR4CloudTmp']
	for tmpdir in cloudtmpdir:
		cloudjiya(tmpdir,'s11_')
		cloudjiya(tmpdir,'gn4_')
		cloudjiya(tmpdir,'s1mme_')
		cloudjiya(tmpdir,'sgs_')
		cloudjiya(tmpdir,'s6a_')
