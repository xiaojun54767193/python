#!/usr/bin/python
import sys,os,shutil
from datetime import date,timedelta,datetime
def deldir(dir,keepday=30):
	"""
	delete the mr directory which older than a month
	"""
	Today=date.today()
	D_keep=Today-timedelta(days=keepday)
	D_format=D_keep.strftime('%Y%m%d')
	Dir=os.listdir(dir)
	for dic in Dir:
		if dic < D_format:
			shutil.rmtree(os.path.join(dir,dic))
if __name__=='__main__':
	deldir('/data/mr/orig')
	deldir('/data/mr/stat')
	deldir('/data/MR_139/Eric_OMC03/orig')
	deldir('/data/MR_139/Eric_OMC03/stat')
	deldir('/data/MR_139/Nokia_OMC01')
	deldir('/data/MR_139/Zte_OMC01')
