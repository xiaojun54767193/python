#!/usr/bin/python
import requests
def delindex(keepday,index):
	r = requests.get('http://10.245.1.17:9200/_cat/indices/%s*?format=json&pretty' %index)
	con = r.json()
	delindex = []
	Index = []
	for Inx in con:
		Index.append(Inx['index'])
	Index.sort()
	indexnum = len(Index)
	for num in range(indexnum-keepday):
		delindex.append(Index[num])	
	for Del in delindex:
		requests.delete('http://10.245.1.17:9200/%s' %Del)
delindex(15,'nokia-logs18')
delindex(15,'nokia-udpi')
delindex(15,'filebeat')
delindex(15,'logstash')
