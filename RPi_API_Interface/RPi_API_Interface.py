import requests
import SmartDHT22
import SmartSound
import SmartMCP3008

def add_dht22(temp, hum):
	url = '127.0.0.1:5000'
	url += "/rest_dht"
	data = {'temp':temp, 'hum':hum}

	resp = requests.post(url, data=data)

	parsed_json = resp.json()
	return parsed_json

def add_sound(audio, env, gate):
	url = '127.0.0.1:5000'
	url += "/rest_sound"
	data = {'audio':audio, 'env':env, 'gate':gate}

	resp = requests.post(url, data=data)

	parsed_json = resp.json()
	return parsed_json

def add_photo(light):
	url = '127.0.0.1:5000'
	url += "/rest_photo"
	data = {'light':light}

	resp = requests.post(url, data=data)

	parsed_json = resp.json()
	return parsed_json

if __name__ == "__main__":
	dht = SmartDHT22(4)
	temp = dht.get_temp_fahrenheit()
	hum  = dht.get_humidity()
        print add_dht22(temp, hum)

	sound = SmartSound(4,3,2)
        audio = sound.get_audio()
        env   = sound.get_envelope()
        gate  = sound.get_gate()
        print add_sound(audio, env, gate)

	photo = SmartMCP3008()
	light = photo.read(1)
	print add_photo(light)
