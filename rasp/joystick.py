from . import registry_uploader

from sense_hat import SenseHat
import time
sense = SenseHat()


while True:
    for event in sense.stick.get_events():
        if (event.direction == 'up' & event.action == 'pressed'):
            sense.set_pixel(7, 7, 0, 255, 255)
            registry_uploader.upload_to_storage()
            sense.clear(124,252,0)
            time.sleep(2)
            sense.clear()
        print (event.direction, event.action)
