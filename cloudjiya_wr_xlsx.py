#!/usr/bin/python
import os,xlsxwriter
from datetime import date
def cloudjiya(clouddir,prefix):
	diclist=[]
	for dir in os.listdir(clouddir):
		if dir.startswith(prefix):
			pos=dir.index('_')+1
			alldic=dir[pos:]
			diclist.append(alldic)
	mindic=os.path.join(clouddir,'%s%s'%(prefix,min(diclist)))
	with open('/root/jiya.txt','a')as fjiya:
		fjiya.write(mindic)
		fjiya.write('\n')
if __name__=='__main__':
	cloudtmpdir=['/data04/UAR4CloudTmp','/data06/UAR4CloudTmp','/data07/UAR4CloudTmp','/data08/UAR4CloudTmp','/data09/UAR4CloudTmp']
	prefixlist=['s11_','gn4_','s1mme_','sgs_','s6a_']
	for tmpdir in cloudtmpdir:
		for pre in prefixlist:
			cloudjiya(tmpdir,pre)

filename=date.today().strftime('%Y%m%d')
suffix='.xlsx'
workbook=xlsxwriter.Workbook(filename+suffix)
worksheet=workbook.add_worksheet()
with open('/root/jiya.txt') as f:
	con=f.readlines()
Len=len(con)
for i in range(Len):
	worksheet.write(i,0,con[i])
workbook.close()
if os.access('/root/jiya.txt',os.F_OK):
	os.remove('/root/jiya.txt')
