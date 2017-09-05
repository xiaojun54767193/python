#!/usr/bin/python
import os,random,shutil
def randomget(path,destpath):
	if not os.access(destpath,os.F_OK):
		os.makedirs(destpath)
	for root,dirs,files in os.walk(path):
		print files
	if len(files) >= 100:
		for i in random.sample(xrange(len(files)),100):
			shutil.copy(os.path.join(path,files[i]),destpath)

#randomget('/data02/group/CILOC','/data02/groupmv/CILOC')	
#randomget('/data02/group/CSFB','/data02/groupmv/CSFB')	
randomget('/data02/group/GB','/data02/groupmv/GB')	
randomget('/data02/group/GB_IUPS','/data02/groupmv/GB_IUPS')	
#randomget('/data02/group/GN_C','/data02/groupmv/GN_C')	
#randomget('/data02/group/MC','/data02/groupmv/MC')	
#randomget('/data02/group/MMECDR','/data02/groupmv/MMECDR')	
#randomget('/data02/group/S11','/data02/groupmv/S11')	
#randomget('/data02/group/S6A','/data02/groupmv/S6A')	
#randomget('/data02/group/SGS','/data02/groupmv/SGS')	
#randomget('/data02/group/SMS','/data02/groupmv/SMS')	
#randomget('/data02/group/S1MME','/data02/groupmv/S1MME')
