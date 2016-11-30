#!/usr/bin/python
import os
def ftpjiya(PlatDir):
	"""Find which directory had jiya
	"""
	filelist = []
	faildir = '/data05/faildata'
	for file in os.listdir(os.path.join(faildir,str(PlatDir))):
		filelist.append(file)
	filenum = len(filelist)	
	if filenum > 0:
		print '{0} had {1} files'.format(PlatDir,filenum)
if __name__ == '__main__':
	for dic in os.listdir('/data05/faildata'):
		ftpjiya(dic
