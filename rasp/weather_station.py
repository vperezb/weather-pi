#!/usr/bin/python 

import time
import os
import datetime

from sense_hat import SenseHat


sense = SenseHat()
sense.clear()

rasp_dir = os.path.dirname(__file__)

local_directory = os.path.join(rasp_dir, 'data/local-files/')

try:
	while True:
		datetime_now = datetime.datetime.now()
		temp = sense.get_temperature()
		hum = sense.get_humidity()
		temp = round(temp, 1)
		
		day = datetime_now.strftime("%Y/%m/%d")
		csv_row = datetime_now.strftime("%Y/%m/%d,  %H:%M:%S") \
		+ ", " + str(temp) + ", " + str(round(hum,1)) + '\n'
		
		file_name = local_directory + datetime_now.strftime("%Y-%m-%d") + '.csv'
		
		with open(file_name, "a+" ) as fd:
			fd.write(csv_row)

		sense.set_pixel(0, 0, 0,255,0)
		time.sleep(60*30)
except KeyboardInterrupt:
	pass
