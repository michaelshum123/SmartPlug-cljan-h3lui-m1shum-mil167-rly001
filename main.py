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
	#sleep for a minute
	time.sleep(60)

with open('readings.csv','wb') as csvfile:
	csvWriter = csv.writer(csvfile)
	for o in output:
		csvWriter.writerow(o)


'''
#too lazy to do vnc/ssh -x on our friedpi
from datetime import datetime
import matplotlib.pyplot as plt
data = []
with open('readings.csv','r') as csvfile:
	csvReader = csv.reader(csvfile)
	for row in csvReader:
		data.append(row)

x = [d[0] for d in data]
y = [d[1] for d in data]
x = [datetime.strptime(x,'%Y-%m-%d %H:%M:%S') for d in x]

plt.plot_date(x,y,'b-')
plt.xlabel('time over 1 hour span')
plt.ylabel('ADC reading of photoresistor in makerspace lab')
plt.title('ADC Readings of photoresistor over 1 hour span')
plt.show()
'''







