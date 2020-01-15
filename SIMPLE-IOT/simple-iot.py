import time
import json
import requests
from random import randint, uniform,random

URL = "http://10.11.0.107:7896/iot/d"

querystring = {"k":"4jggokgpepnvsb2uv4s40d59ov","i":"DHT22003"}

headers = {
    'Content-Type': "text/plain",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "898a71a0-0ee3-496a-998b-ee3eb4885342,3ff8a888-6a51-451b-b68d-d257cf34a885",
    'Host': "10.11.0.107:7896",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "11",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

try:
    while True:
        print("Hola Simple IOT")
      

        temp = randint(15,50)
        hum = randint(0,100)

        print("Temperature "+str(temp))
        print("Humidity "+str(hum))

        simple_payload = "t|"+str(temp)+"|h|"+str(hum)

        print("Payload "+simple_payload)

        #simple_iot_response = requests.request("POST",URL, data=simple_payload, headers=headers,params=querystring)
        time.sleep(5)

except KeyboardInterrupt:
    print("Se ha interrumpido la ejecución del script...")    

print("Finalizando ...")

   
