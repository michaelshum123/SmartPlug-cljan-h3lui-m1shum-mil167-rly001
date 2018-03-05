import Adafruit_DHT

class SmartDHT22():
	def __init__(self, inPin):
		self.pin = inPin
	def get_temp_celsius(self):
		humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, self.pin )
		if temp is not None:
			return int(temp)
		else:
			return -1

	def get_temp_fahrenheit(self):
		humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, self.pin )
		if temp is not None:
			temp = temp * 9/5.0 + 32
			return int(temp)
		else:
			return -1

	def get_humidity(self):
		humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, self.pin )
		if humidity is not None:
			return int(humidity)
		else:
			return -1
