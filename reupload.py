#!/usr/bin/python
import os,sys
def findreupload(faildir):
	"""Check if there are files in the uar4 ftp directories
	"""
	filelist = []
	for dir in os.listdir(faildir):
		for file in os.listdir(os.path.join(faildir,dir)):
			filelist.append(file)
	filenum = len(filelist)
	if sys.argv[1] == 'jiya':
		if filenum  > 0:
			print 0
		else:
			print 1
	if sys.argv[1] == 'jiyanum':
		print filenum
if __name__ == '__main__':
	findreupload('/data05/faildata')
