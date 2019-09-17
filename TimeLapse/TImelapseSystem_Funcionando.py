import os
import time
import base64
import json
import requests
#from datetime import datetime


url = 'http://ec2-54-94-245-133.sa-east-1.compute.amazonaws.com:3000/timelapse'
#Horas_Timelapse = 3



FRAMES = 300
FPS_IN = 10
FPS_OUT = 24
TIMEBETWEEN = 20
FILMLENGTH = float(FRAMES / FPS_IN)
conta =1
frameCount = 1
print (frameCount)
os.system("sudo wget http://raspberrypi:8088/?action=snapshot -q")
os.system("sudo mv index.html?action=snapshot /home/pi/TCC/TimeLapse/image0000000.jpg")
while frameCount < FRAMES:
    imageNumber = str(frameCount).zfill(7)
    os.system("sudo wget http://raspberrypi:8088/?action=snapshot -q")
    #os.system("raspistill -o image%s.jpg"%(imageNumber))
    
    os.system("sudo mv index.html?action=snapshot.%s /home/pi/TCC/TimeLapse/image%s.jpg"%(conta, imageNumber))
        

    print (imageNumber)        
    frameCount += 1
    
    time.sleep(TIMEBETWEEN) #Takes roughly 6 seconds to take a picture

    

os.system("avconv -r %s -i image%s.jpg -r %s -vcodec libx264 -crf 20 -g 15 -vf crop=1280:720,scale=640:480 timelapse.mp4"%(FPS_IN,'%7d',FPS_OUT))
os.system("sudo rm *.jpg")
#Converte
image = open('timelapse.mp4', 'rb') #open binary file in read mode 
image_read = image.read() 
image_64_encode = base64.b64encode(image_read)

#print (image_64_encode)


imageFormatted = "%s" % (image_64_encode,)
x = imageFormatted.split("b'")[1]
y=x.split("'")

#r = requests.post(url, json={'idBebe':'123456789', 'arquivo': "%s" % (y[0],)})

print ('Enviado para AWS')

