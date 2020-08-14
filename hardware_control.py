import RPi.GPIO as GPIO

import time

# set the deault board numbering# BCM ---- GPIO5, GPIO6 like this
GPIO.setmode(GPIO.BOARD)

'''
GPIO5 and GPIO6  ---- Pertrol  i,e pin 29 and 31

GPIO13 and GPIO19 used for diesal  i,e pin33 and 35

'''

channel_list = (29, 31, 33, 35)


def RESET_ALL_PINS_LOW():
    global channel_list
    GPIO.output(channel_list, GPIO.LOW)
    
    

# setup these pins as output
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

def fill_petrol(amount, petrol_price):
    global channel_list
    
    
    litres_of_petrol = amount / petrol_price
    # rounding to 2 decimal places
    litres_of_petrol = round(litres_of_petrol, 2)
    
    # assume we fill 1L of fuel in 30 sec
    time_to_fill =  int((30 * litres_of_petrol))
    
    print('Litres of Petrol -> ', litres_of_petrol, 'TIme to fill', time_to_fill) 
    
    # reset all pins to LOW
    RESET_ALL_PINS_LOW()
    
    # turn on petrol pin numbers for time = tine_to_fill
    GPIO.output(channel_list, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW))
    
    print('-----------Filling Petrol-----------')
    # delay
    time.sleep(time_to_fill)
    
    # rest all pins
    RESET_ALL_PINS_LOW()

def fill_deisel(amount, deisel_price):
    
    
    litres_of_deisel = amount / deisel_price
    # rounding to 2 decimal places
    litres_of_deisel = round(litres_of_deisel, 2)
    
    # assume we fill 1L of fuel in 30 sec
    time_to_fill =  int((30 * litres_of_deisel))

    print('Litres of Deisel -> ', litres_of_deisel, 'TIme to fill', time_to_fill)
    # reset all pins to LOW
    RESET_ALL_PINS_LOW()
    
    # turn on petrol pin numbers for time = tine_to_fill
    GPIO.output(channel_list, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW))
    
    # delay
    print('-----------Filling Deisel-----------')
    time.sleep(time_to_fill)
    
    # rest all pins
    RESET_ALL_PINS_LOW()
    


#fill_petrol(100, 70)
#fill_deisel(100, 65)

#GPIO.cleanup()

    

    
    
    



