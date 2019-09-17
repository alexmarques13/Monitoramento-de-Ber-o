import base64


#Converte
image = open('7h_15seg.mp4', 'rb') #open binary file in read mode 
image_read = image.read() 
image_64_encode = base64.encodestring(image_read)

print (image_64_encode)



#Desconverte

decoded_string = base64.b64decode(image_64_encode) 

with open('/video.mp4', 'wb') as wfile:
   wfile.write(decoded_string)