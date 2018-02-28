from . import dbtool
from SmartMCP3008 import SmartMCP3008
from SmartDHT22   import SmartDHT22
from SmartSound   import SmartSound
from time import gmtime, strftime
import time
class sensordb:
    def __init__(self):
        self.db = dbtool()
        self.photo = SmartMCP3008()
        self.dht = SmartDHT22(4)
        self.sound = SmartSound(4,3,2)
        self.DHT_TABLE = 'dht'
        self.SOUND_TABLE = 'sound'
        self.PHOTO_TABLE = 'photo'
    # num = number to get from most recent
    # num = -1 means get all
    def makeTables(self):
        self.db.makeDB(self.DHT_TABLE, [['date','varchar(30)'],['temp','int'],['hum','int']])
        self.db.makeDB(self.SOUND_TABLE,[['date','varchar(30)'],['audio','int'],['env','int'],['gate','int']])
        self.db.makeDB(self.PHOTO_TABLE,[['date','varchar(30)'],['light','int']])
            
    def get_DHT22(self,num):
        self.db.getRows(self.DHT_TABLE, num)

    def get_Sound(self,num):
        self.db.getRows(self.SOUND_TABLE, num)

    def get_Photo(self,num):
        self.db.getRows(self.PHOTO_TABLE, num)

    def set_DHT22(self):
        #read DHT and then write to sql
        strTime = self.getTime()
        temp = self.dht.get_temp_fahrenheit()
        hum  = self.dht.get_humidity()
        self.db.insertRow( self.DHT_TABLE, [strTime, temp, hum] )
        return [temp,hum]

    def set_Sound(self):
        strTime = self.getTime()
        audio = self.sound.get_audio()
        env   = self.sound.get_envelope()
        gate  = self.sound.get_gate()
        self.db.insertRow( self.SOUND_TABLE, [strTime,audio,env,gate] )
        return [audio,env,gate]

    def set_Photo(self):
        strTime = self.getTime()
        light = self.photo.read(1)
        self.db.insertRow( self.PHOTO_TABLE, [strTime, light] )
        return light

    def getTime(self):
        return strftime("%Y-%m-%d %H:%M:%S",gmtime())

    def obtainData(self):
        for i in range(60):
            print(self.getTime())
            print(self.set_Sound())
            print(self.set_DHT22())
            print(self.set_Photo())
            time.sleep(1)
