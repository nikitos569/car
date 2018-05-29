import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk #sensor ist die Datei (sensor.py), in der die Methode zum Messen der Distanz liegt
from sensor import distance #wenn du das nicht brauchst, kommentiere diese Zeile und unten mehrere
#"init" initialisiert die Pins
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT) #IN4
    gpio.setup(11, gpio.OUT)#IN3
    gpio.setup(13, gpio.OUT)#In2
    gpio.setup(15, gpio.OUT)#IN1
#fahr zurueck
def reverse(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
#fahr nach vorne    
def forward(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    
def turn_right(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    
def turn_left(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
#alle Pins False = kein Strom = stop
def stop(tf):
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def key_input(event):
    init()
    print "Key:", event.char
    key_press = event.char
    sleep_time = 0.060
    
    if key_press.lower() == "w":
        forward(sleep_time)
    elif key_press.lower() == "s":
        reverse(sleep_time)
    elif key_press.lower() == "a":
        turn_left(sleep_time)
    elif key_press.lower() == "d":
        turn_right(sleep_time)
    elif key_press.lower() == "p":
        stop(sleep_time) 
    else:
        pass

    curDis = distance("cm") #diese Zeilen brauchen "import distance". diese bis zum naechsten Kommentar inklusiv
    print("Distance:", curDis)
    
    if curDis <15:
        init()
        reverse(0.5) #bis hier sollst du kommentieren

command = tk.TK()
command.bind('<keypress>', key_input)
command.mainloop()