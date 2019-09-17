import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import requests
import json

url = 'http://ec2-54-94-245-133.sa-east-1.compute.amazonaws.com:3000/ambiente'

sensor = Adafruit_DHT.DHT22

GPIO.setmode(GPIO.BOARD)

pino_sensor = 23


def temperatura():
#while (1):

    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)

    if umid is not None and temp is not None:

        print ('Enviado322') 
        #print ('Temperatura = {0:0.1f} Umidade = {1:0.1f}\n').format(temp, umid)
        r = requests.post(url, json={'idBebe':'123456789', 'tempAmbiente': ('{0:0.1f} ').format(temp), 'umidade': ('{0:0.1f} ').format(umid)})
            
        #time.sleep(10)
        return temp, umid
            
    #else:
        #print('Falha ao ler dados do Sensor!!')

    
while(1):
    temperatura()
    #tempe = temperatura(temp)
    #umida = temperatura(umid)

    
