from time import gmtime,strftime
import time
import csv


ADC_Channel = 0
#if self == '__init__': 
output = []
SmartMCP3008 smartMcp = SmartMCP3008()
for i in range(60):
	#get time
	strTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	#get val
	val = smartMcp.read(ADC_Channel)

	#add to output
	output.append([strTime, val])

	#sleep
	sleep(60)

with open('readings.csv','wb') as csvfile:
	csvWriter = csv.writer(csvfile)
	for o in output:
		csvWriter.writerow(o)








