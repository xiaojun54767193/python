#!/usr/bin/python
import os,random,shutil,glob
from multiprocessing import Process
def randomget(type,destpath):
	if not os.access(destpath,os.F_OK):
		os.makedirs(destpath)
	files = glob.glob('/data02/group/%s/*2017083011*.gz' %type)
	for file in files:
		shutil.copy(file,destpath)

p1 = Process(target=randomget,args=('S1U','/data02/groupmv/S1U'))
p2 = Process(target=randomget,args=('CILOC','/data02/groupmv/CILOC'))
p3 = Process(target=randomget,args=('CSFB','/data02/groupmv/CSFB'))
p5 = Process(target=randomget,args=('GB','/data02/groupmv/GB'))
p7 = Process(target=randomget,args=('GB_IUPS','/data02/groupmv/GB_IUPS'))
p8 = Process(target=randomget,args=('GN','/data02/groupmv/GN'))
p9 = Process(target=randomget,args=('GN_C','/data02/groupmv/GN_C'))
p10 = Process(target=randomget,args=('MC','/data02/groupmv/MC'))
p11 = Process(target=randomget,args=('MMECDR','/data02/groupmv/MMECDR'))
p12 = Process(target=randomget,args=('S11','/data02/groupmv/S11'))
p13 = Process(target=randomget,args=('S1MME','/data02/groupmv/S1MME'))
p14 = Process(target=randomget,args=('S6A','/data02/groupmv/S6A'))
p15 = Process(target=randomget,args=('SGS','/data02/groupmv/SGS'))
p16 = Process(target=randomget,args=('SMS','/data02/groupmv/SMS'))

processlist = [p1,p2,p3,p5,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16]
for p in processlist:
	p.start()
p.join()
