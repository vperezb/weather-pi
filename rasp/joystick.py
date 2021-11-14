from sense_hat import SenseHat
sense = SenseHat()


while True:
    for event in sense.stick.get_events():
        if (event.direction) == 'up':
            sense.set_pixel(7, 7, 0, 255, 255)
        print (event.direction, event.action)
