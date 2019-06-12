import requests
import threading
from multiprocessing.pool import ThreadPool
import time
import sys
import os

URL = "http://192.168.219.133:80/facerec"
webcamStreamURL="192.168.219.200:8090/?action=snapshot"
jsonParams = {'username':'parkjaehyun','stream_url':webcamStreamURL}

res = requests.get(URL,params=jsonParams)
jsonData=res.json()
result = jsonData["face_rec"]
if result=="True":
    os.system('mosquitto_pub -u hass -P 0000 -t homeassistant/faceid -m "pass"')
else:
    os.system('mosquitto_pub -u hass -P 0000 -t homeassistant/faceid -m "fail"')
	
	
	
	
	





