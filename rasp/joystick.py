from modules import registry_uploader

from sense_hat import SenseHat
import time
sense = SenseHat()

sense.set_pixel(0, 1, 0,255,0)

while True:
    for event in sense.stick.get_events():
        if ((event.direction == 'up') and (event.action == 'pressed')):
            sense.set_pixel(7, 7, 0, 255, 255)
            succeed = registry_uploader.upload_to_storage()
            if succeed:
                sense.clear(0,255,0)
                time.sleep(2)
                sense.clear()
            else:
                sense.clear(220,20,60)
                time.sleep(2)
                sense.clear()
            sense.set_pixel(0, 1, 0,255,0)
        #print (event.direction, event.action)
