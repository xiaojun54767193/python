#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: gouxiaojun
#date: 2016-9-4
#version: 1.0
#mail: 547671930@qq.com
#qq: 547671930
#This script is used for createing a mode 6 bonding on RedHat 6 and Centos 6 series has tested on RedHat 6.6
import os
alist=['ifenslave']
ethdic='/etc/sysconfig/network-scripts/'
filepr='ifcfg-'
bondname=raw_input('Input the bond name you want to create: ')
ip=raw_input('Input the ip address the bond will use: ')
mask=raw_input('Input the mask the bond will use: ')
gateway=raw_input('Input the gateway the bond will use: ')
alist.append(bondname)
os.chdir(ethdic)
towriter='''
DEVICE=%s
BONDING_OPTS="mode=6 miimon=100"
BOOTPROTO=none
ONBOOT=yes
IPADDR=%s
NETMASK=%s
GATEWAY=%s
USERCTL=no
'''
with open(filepr+bondname,'w') as fb:
	fb.write(towriter %(bondname,ip,mask,gateway))	
	print 'the bond file was created!'

num=int(raw_input('Input the number of devices you want to bond to the bond: '))
wr='''
DEVICE=%s
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=none
MASTER=%s
SLAVE=yes
USERCTL=no
'''
for i in range(num):
	ethname=raw_input('Input the %d device name: ' %i)
	with open(filepr+ethname,'w') as fe:
		fe.write(wr %(ethname,bondname))
	alist.append(ethname)
mw='''
alias %s bonding
options %s mode=6 miimon=50
'''
with open('/etc/modprobe.d/dist.conf','a') as fm:
	fm.write(mw %(bondname,bondname))

btuple=tuple(alist)
Len=len(btuple)
tw='%s '*Len
with open('/etc/rc.local','a') as ft:
	ft.write(tw %btuple)

print 'Begin to restar the network service...'
os.system('service network restart')
print 'Successfully restart the network service!'
