#!/usr/bin/python
import os,sys
def bond():
	"""
	create a bond interface which mode is 6
	"""
	alist=['ifenslave']
	ethdic='/tmp/test'
	filepre='ifcfg-'
	bondname=raw_input('Input the bond name you want to create: ')
	ip=raw_input('Input the ip address the bond will use: ')
	mask=raw_input('Input the mask the bond will use: ')
	gateway=raw_input('Input the gateway the bond will use: ')
	alist.append(bondname)
	os.chdir(ethdic)
	towriter='DEVICE=%s\nBONDING_OPTS="mode=6 miimon=100"\nBOOTPROTO=none\nONBOOT=yes\nIPADDR=%s\nNETMASK=%s\nGATEWAY=%s\nUSERCTL=no\n'
	with open(filepre+bondname,'w') as fb:
		fb.write(towriter %(bondname,ip,mask,gateway))
		print 'The bond file was created!'
	slavenum=int(raw_input('Input the number of devices you want to bond to the bond: '))
	write_2_slave='DEVICE=%s\nTYPE=Ethernet\nONBOOT=yes\nNM_CONTROLLED=yes\nBOOTPROTO=none\nMASTER=%s\nSLAVE=yes\nUSERCTL=no\n'
	for slave in range(slavenum):
		slavename=raw_input('Input the %d device name: ' %(slave+1))
		with open(filepre+slavename,'w') as fe:
			fe.write(write_2_slave %(slavename,bondname))
		alist.append(slavename)
	mw='alias %s bonding\noptions %s mode=6 miimon=50\n'
	with open('/etc/modprobe.d/dist.conf','a') as fm:
		fm.write(mw %(bondname,bondname))
	btuple=tuple(alist)
	Len=len(btuple)
	tw='%s '*Len
	with open('/etc/rc.local','a') as ft:
		ft.write(tw %btuple)
	print 'Begin to restart the network service...'
	os.system('service network restart')
	print 'Successfully restart the network service!'
def hostname():
	"""
	setting the system hostname
	"""
	name=raw_input('Please input the hostname for this machine: ')
	netcon='NETWORKING=yes\nHOSTNAME=%s\n'
	print 'Setting the hostname,please wait........'
	with open('/etc/sysconfig/network','w') as wrnet:
		wrnet.write(netcon %name)
def selinux():
	"""
	setting the selinux to disabled
	"""
	selinuxcon='SELINUX=disabled\nSELINUXTYPE=targeted\n'
	print 'Setting the selinux to disable state,please wait......'
	with open('/etc/sysconfig/selinux','w') as wrslin:
		wrslin.write(selinuxcon)
def iptables():
	"""
	disable the iptables and stop it
	"""
	print 'Setting the iptables to not start up when the system start,please wait...'
	os.system('chkconfig iptables off')
	os.system('service iptables stop')
def help():
#	print 'USAGE: %s {bond|selinux|iptables|hostname|all}' %sys.argv[0]
	print """\
	Usage: system_initize.py [OPTIONS]
	-h display this usage message
	bond create the bond
	hostanem set the hostname
	iptables disale the iptables
	selinux  set the selinux to disable
	all do all the things above
	"""
if len(sys.argv)!=2:
	help()
	sys.exit(200)
if sys.argv[1]=='bond':
	bond()
elif sys.argv[1]=='selinux':
	selinux()
elif sys.argv[1]=='hostname':
	hostname()
elif sys.argv[1]=='iptables':
	iptables()
elif sys.argv[1]=='all':
	bond()
	selinux()
	hostname()
	iptables()
else:
	help()
