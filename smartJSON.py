from time import gmtime,strftime
import time
import csv
from SmartSound import SmartSound
from SmartMCP3008 import SmartMCP3008
from SmartDHT22  import SmartDHT22
import RPi.GPIO as GPIO
import json

DHT_Pin = 4
ADC_Channel = 1
output = []
smartSound = SmartSound(4,3,2)
smartMcp = SmartMCP3008()
smartDHT = SmartDHT22(DHT_PIN)
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(True)
#GPIO.setup(18, GPIO.OUT)
for i in range(60):
    #get time
    strTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    #get val
    valLight = smartMcp.read(ADC_Channel)
    valTemp = smartDHT.get_temp_fahrenheit()
    valHum = smartDHT.get_humidity()
    valEnv = smartSound.get_envelope()

    #add to output
    output.append([strTime, valTemp, valHum, valEnv])
    print(strTime +' '+ str(val))
    #sleep for a minute
    time.sleep(1)

with open('sensor.json','w') as outFile:
    outFile.write(json.dumps(output))

