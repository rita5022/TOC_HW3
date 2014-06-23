# -*- coding:utf8 -*-
# Program:TocHw3
# Description:find the average of all sale prices matching the condition as the arguments
# Example:python TocHw3.py http://www.datagarage.io/api/5365dee31bc6e9d9463a0057 楊梅市 金山街 103

# Name:蘇容德
# Student Number:F74001218

import json
import urllib2
import sys

if(len(sys.argv)==5):
	url = sys.argv[1]
	response = urllib2.urlopen(url)
	data = json.load(response)
	
	data_len = len(data) #data總共大小
	count = 0
	zz='00'
	money = 0
	num = 0

	while count < data_len:
		if(data[count][u"鄉鎮市區"] == unicode(sys.argv[2],"utf-8")):
			if(data[count][u"土地區段位置或建物區門牌"].find(unicode(sys.argv[3],"utf-8"))!=-1):
				year = int(sys.argv[4]+zz)
				if(int(data[count][u"交易年月"]) > year):
					num = num + 1
					money = money + data[count][u"總價元"]
				
		count = count + 1

	if num>=1:
		print money/num
	else:
		print "There's no matching conditions"

else:
	print "The number of input argument is wrong"
