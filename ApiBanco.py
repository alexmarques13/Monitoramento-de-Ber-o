import requests
import json


url = 'http://ec2-54-94-245-133.sa-east-1.compute.amazonaws.com:3000/ambiente'

teste=123
teste2=123
teste3=123


#print r.headers['content-type']



# GET
#r = requests.get(url)

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON 

r = requests.post(url, json={'idBebe':'512', 'tempAmbiente': '232', 'umidade': '312'})

# Response, status etc
#r.text
#r.status_code
