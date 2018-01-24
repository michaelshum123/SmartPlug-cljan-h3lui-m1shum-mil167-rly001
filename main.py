from time import gmtime,strftime
import time
import csv
from SmartMCP3008 import SmartMCP3008

ADC_Channel = 2
#if self == '__init__': 
output = []
smartMcp = SmartMCP3008()
for i in range(60):
	#get time
	strTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	#get val
	val = smartMcp.read(ADC_Channel)

	#add to output
	output.append([strTime, val])
        print(strTime +' '+ str(val))
	#sleep
	time.sleep(1)

with open('readings.csv','wb') as csvfile:
	csvWriter = csv.writer(csvfile)
	for o in output:
		csvWriter.writerow(o)








