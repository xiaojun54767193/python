#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
for input in sys.stdin:
	v = input.split('|')
	for i in list(enumerate(v,start=1)):
		print i[0],i[1]
