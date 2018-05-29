import RPi.GPIO as gpio
import time #diese Datei muss im demselben Ordner mit main.py sich befinden
#dieses Programm misst die Distanz mittels Ultraschalsensor
def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT) #trigger cable
    gpio.setup(16, gpio.IN) #echo cable
  
    time.sleep(0.3)
    gpio.ouput(12, True)
    time.sleep(0.00001)
    
    gpio.output(12, False)
    while gpio.input(16) == 0:
        nosig = time.time()
    
    while gpio.input(16) == 1:
        sig = time.time()
    
    tl = sig - nosig
    
    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in:
        distance = tl / 0.000148
    else:
        print('Improper choice of measurement: in or cm')
        distance = None
    
    gpio.cleanup()
    return distance
  
print(distance('cm'))
    