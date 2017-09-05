#!/usr/bin/python
import os,time
def mytime(type,path):
	filelist = []
	alltime = 0
	for root,dirs,files in os.walk(path):
		for file in files:
			if file.endswith('gz'):
				mytime = file[41:55]
				tu = file,os.stat(os.path.join(root,file)).st_mtime,time.mktime((int(mytime[0:4]),int(mytime[4:6]),int(mytime[6:8]),int(mytime[8:10]),int(mytime[10:12]),int(mytime[12:14]),0,0,0))
				filelist.append(tu)
	filenum = len(filelist)
	for f in filelist:
#		print f[0],(f[1] - f[2])/60.0
		alltime+=(f[1] - f[2])/60.0
	print type,filenum,alltime/filenum

mytime('CSFB','/data02/group/CSFB')
mytime('S11','/data02/group/S11')
mytime('S1U','/data02/group/S1U')
mytime('S1MME','/data02/group/S1MME')
mytime('S6A','/data02/group/S6A')
mytime('SGS','/data02/group/SGS')
mytime('GN','/data02/group/GN')
mytime('GN_C','/data02/group/GN_C')
mytime('GB','/data02/group/GB')
mytime('GB_IUPS','/data02/group/GB_IUPS')
mytime('MC','/data02/group/MC')
mytime('CILOC','/data02/group/CILOC')
mytime('SMS','/data02/group/SMS')
mytime('MMECDR','/data02/group/MMECDR')
