#!/usr/bin/python 

import time
import os
import datetime

from sense_hat import SenseHat


sense = SenseHat()
sense.clear()

try:
	while True:
		datetime_now = datetime.datetime.now()
		temp = sense.get_temperature()
		hum = sense.get_humidity()
		temp = round(temp, 1)
		
		day = datetime_now.strftime("%Y/%m/%d")
		csv_row = datetime_now.strftime("%Y/%m/%d,  %H:%M:%S") \
		+ ", " + str(temp) + ", " + str(round(hum,1)) + '\n'
		
		file_name = 'data/unclouded-files/' + datetime_now.strftime("%Y-%m-%d") + '.csv'
		
		exist=os.path.exists(file_name)
		with open(file_name, "a" if exist else "w") as fd:
			fd.write(csv_row)

		sense.set_pixel(0, 0, 255, 255, 255)
		time.sleep(60*30)
except KeyboardInterrupt:
	pass
