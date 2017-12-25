#!/usr/bin/env python3
import tarfile,os,sys,time
path = sys.argv[1]
file = os.walk(path)
for roots,dirs,filename in file:
	for f in filename:
		tar = tarfile.open(os.path.join(roots,f))
		for tarinfo in tar:
			print(tarinfo.name, "is", round(tarinfo.size/1024/1024,2), "mb in size,", "mtime is", time.ctime(tarinfo.mtime))
