import RPi.GPIO as GPIO
from time import sleep


''' Ponte H / Fio / BCM / BOARD:
ni1 - verde         (5)   (29)  15
ni2 - amarelo       (6)   (31)  13
ni3 - azul          (7)   (24)  11
ni4 - roxo          (8)   (26)  7
'''
ni_1 = 5
ni_2 = 6
ni_3 = 7
ni_4 = 8

sec = sleep(1)

def init_motores():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ni_1, GPIO.OUT)
    GPIO.setup(ni_2, GPIO.OUT)
    GPIO.setup(ni_3, GPIO.OUT)
    GPIO.setup(ni_4, GPIO.OUT)


def forward(sec):
    init_motores()
    GPIO.output(ni_1, False)
    GPIO.output(ni_2, True)
    GPIO.output(ni_3, False)
    GPIO.output(ni_4, True)
    sleep(sec)
    

def reverse(sec):
    init_motores()
    GPIO.output(ni_1, True)
    GPIO.output(ni_2, False)
    GPIO.output(ni_3, True)
    GPIO.output(ni_4, False)
    sleep(sec)
    

def turn_right(sec):
    init_motores()
    GPIO.output(ni_1, True)
    GPIO.output(ni_2, False)
    GPIO.output(ni_3, False)
    GPIO.output(ni_4, True)
    sleep(sec)
    
    
def turn_left(sec):
    init_motores()
    GPIO.output(ni_1, False)
    GPIO.output(ni_2, True)
    GPIO.output(ni_3, True)
    GPIO.output(ni_4, False)
    sleep(sec)
    
    
def stop():
    init_motores()
    GPIO.output(ni_1, False)
    GPIO.output(ni_2, False)
    GPIO.output(ni_3, False)
    GPIO.output(ni_4, False)    
    GPIO.cleanup()
    

''' Testando '''
try:
        
    while True:
        s = str(input('[F] - [B] - [L] - [R] - [S]: '))
        v = s.upper()
        
        if v == 'F':
            print('F', forward(0.5))
        elif v == 'B':
            print('B', reverse(0.5))
        elif v == 'L':
            print('L', turn_left(0.5))
        elif v == 'R':
            print('R', turn_right(0.5))
        else:
            print('S', stop())        
        
except KeyboardInterrupt:
    stop()    
    print("cleaning up")
