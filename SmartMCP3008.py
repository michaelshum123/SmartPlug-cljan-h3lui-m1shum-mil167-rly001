import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

class SmartMCP3008:
	def __init__(self):
		self.SPI_PORT = 0
		self.SPI_DEVICE = 0
		self.mcp = Adafruit_MCP3008.MCP3008( spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEVICE) )

	def read(self,pin_num):
		if 0 <= pin_num and pin_num <= 7:
			return self.mcp.read_adc(pin_num)
		else:
			return -1
