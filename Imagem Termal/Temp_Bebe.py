import serial, time
import datetime as dt
import numpy as np
import cv2
import requests
import json

url = 'http://ec2-54-94-245-133.sa-east-1.compute.amazonaws.com:3000/temperatura'

# function to get Emissivity from MCU
def get_emissivity():
	ser.write(serial.to_bytes([0xA5,0x55,0x01,0xFB]))
	read = ser.read(4)
	return read[2]/100

# function to get temperatures from MCU (Celsius degrees x 100)
def get_temp_array(d):

	# getting ambient temperature
	T_a = (int(d[1540]) + int(d[1541])*256)/100

	# getting raw array of pixels temperature
	raw_data = d[4:1540]
	T_array = np.frombuffer(raw_data, dtype=np.int16)
	
	return T_a, T_array



########################### Main cycle #################################
# Color map range
Tmax = 40
Tmin = 20

print ('Configuring Serial port')
ser = serial.Serial ('/dev/serial0')
ser.baudrate = 115200
#ser.baudrate = 9800


# set frequency of module to 4 Hz
ser.write(serial.to_bytes([0xA5,0x25,0x01,0xCB]))
time.sleep(0.1)

# Starting automatic data colection
ser.write(serial.to_bytes([0xA5,0x35,0x02,0xDC]))
t0 = time.time()

i=0
temperatura = 0

try:
        while True:
	
                # waiting for data frame
                
                
                
                data = ser.read(1544)
                
                # The data is ready, let's handle it!
                Ta, temp_array = get_temp_array(data)
                
                #ta_img = td_to_image(temp_array)

                #text = 'Tmin = {:+.1f} Tmax = {:+.1f} FPS = {:.2f}'.format(temp_array.min()/100, temp_array.max()/100, 1/(time.time() - t0))
                #r = requests.post(url, json={'idBebe':'123456789', 'tempBebe': ('{0:0.1f} ').format(temp_array.max()/100)})
                if (i==100):
                        temperatura = temperatura/100
                        r = requests.post(url, json={'idBebe':'123456789', 'tempBebe': ('{0:0.1f} ').format(temperatura)})
                        print ('Temperatura Enviada: {0:0.1f}'.format(temperatura))
                        time.sleep(30)
                        i=0

                temperatura = temperatura + (temp_array.max()/100)
                i += 1
                print (i)
                print ('Tmin = {:+.1f} Tmax = {:+.1f} '.format(temp_array.min()/100, temp_array.max()/100))
                
                
                #time.sleep(0.5)

except KeyboardInterrupt:
	# to terminate the cycle
	ser.write(serial.to_bytes([0xA5,0x35,0x01,0xDB]))
	ser.close()
	
	print(' Stopped')

# just in case
ser.close()

