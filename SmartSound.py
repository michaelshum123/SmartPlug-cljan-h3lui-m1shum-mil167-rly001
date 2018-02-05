import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

class SmartSound:
	def __init__(self, gateChn, envChn, audioChn):
		self.SPI_PORT = 0
		self.SPI_DEVICE = 0
		self.mcp = Adafruit_MCP3008.MCP3008( spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEVICE) )
                self.gateChannel = gateChn
                self.envChannel = envChn
                self.audioChannel = audioChn
	def get_gate(self):
		if 0 <= pin_num and pin_num <= 7:
			return self.mcp.read_adc(self.gateChannel)
		else:
			return -1

	def get_envelope(self):
		if 0 <= pin_num and pin_num <= 7:
			return self.mcp.read_adc(self.evnChannel)
		else:
			return -1

	def get_audio(self):
		if 0 <= pin_num and pin_num <= 7:
			return self.mcp.read_adc(self.audioChannel)
		else:
			return -1
