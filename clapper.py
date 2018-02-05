from time import gmtime,strftime
import time
import csv
from SmartSound import SmartSound
import RPi.GPIO as GPIO
output = []
smartSound = SmartSound(4,3,2)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(18, GPIO.OUT)
while(True):
    if smartSound.get_envelope() > 75:
        GPIO.output(18,GPIO.HIGH)
    else:
        GPIO.output(18,GPIO.LOW)

'''for i in range(60):
	#get time
	strTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	#get val
	#valLight = smartMcp.read(ADC_Channel)
        #valTemp = smartDHT.get_temp_fahrenheit()
        #valHum = smartDHT.get_humidity()
	valAudio = smartSound.get_audio()
        valEnv   = smartSound.get_envelope()
        valGate  = smartSound.get_gate()
        #add to output
	output.append([strTime, valAudio, valEnv, valGate])
        print(output[-1])
	#sleep for a minute
	time.sleep(1)

with open('readingsSound2.csv','w') as csvfile:
	csvWriter = csv.writer(csvfile)
	for o in output:
		csvWriter.writerow(o)

'''
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







