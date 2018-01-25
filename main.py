from time import gmtime,strftime
import time
import csv
from SmartMCP3008 import SmartMCP3008
from SmartDHT22  import SmartDHT22
ADC_Channel = 2 #Channel on ADC chip
DHT_Pin = 4 #GPIO pin, not HW pin, that receives data
#if self == '__init__':
output = []
smartMcp = SmartMCP3008()
smartDHT = SmartDHT22(DHT_Pin)
for i in range(60):
	#get time
	strTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	#get val
	valLight = smartMcp.read(ADC_Channel)
        valTemp = smartDHT.get_temp_fahrenheit()
        valHum = smartDHT.get_humidity()
	#add to output
	output.append([strTime, valLight, valTemp, valHum])
        print(strTime +' '+ str(val))
	#sleep for a minute
	time.sleep(60)

with open('readings.csv','w') as csvfile:
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
yLight = [d[1] for d in data]
yTemp = [d[2] for d in data]
yHum = [d[3] for d in data]
x = [datetime.strptime(x,'%Y-%m-%d %H:%M:%S') for d in x]

plt.plot_date(x,yLight,'b-',label='Light')
plt.plot_date(x,yTemp,'r-',label='Temp C')
plt.plot_date(x,yHum,'g-',label='Humidity %')
plt.xlabel('Time over 1 hour span')
plt.ylabel('Reading of photoresistor circuit and DHT sensor')
plt.legend()
plt.title('Readings of photoresistor circuit and DHT sensor over 1 hour span')
plt.show()
'''







