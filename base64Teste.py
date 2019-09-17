import base64
import requests
import json


url = 'http://ec2-54-94-245-133.sa-east-1.compute.amazonaws.com:3000/babyDetection'
#Converte
image = open('IMG_20190717_203617.jpg', 'rb') #open binary file in read mode 
image_read = image.read() 
image_64_encode = base64.b64encode(image_read)

print (image_64_encode)

imageFormatted = "%s" % (image_64_encode,)
x = imageFormatted.split("b'")[1]
y=x.split("'")


#r = requests.post(url, json={'idBebe':'123456789', 'arquivo': ("{}").format(image_64_encode)})
r = requests.post(url, json={'idBebe':'12345', 'image': "%s" % (y[0],)})

print (r.text)

#arq = open("videobase64.txt", "w")
#arq.write ("%s" % (y[0],))
#arq.close()



print ('foi')

#Desconverte

#decoded_string = base64.b64decode(image_64_encode) 

#with open('/video.mp4', 'wb') as wfile:
 #  wfile.write(decoded_string)