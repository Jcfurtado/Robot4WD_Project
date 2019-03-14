import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from time import sleep

# Pin
servo_pin = 18
fs = DistanceSensor(echo= 23, trigger= 4, max_distance= 1, threshold_distance= 0.2)
bs = DistanceSensor(echo= 24, trigger= 16, max_distance= 1, threshold_distance= 0.1)

#Iniciar o pino gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

#Ajuste estes valores para obter o intervalo completo do movimento do servo
deg_0_pulse   = 0.5
deg_180_pulse = 2.5
f = 50.0
 
# Faca alguns calculos dos parametros da largura do pulso
period = 1000/f
k      = 100/period
deg_0_duty = deg_0_pulse * k
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k
 
#Iniciar o pwm
pwm = GPIO.PWM(servo_pin,f)
pwm.start(0)

def set_angle(angle):    
    duty = deg_0_duty + (int(angle)/180.0) * duty_range
    pwm.ChangeDutyCycle(duty)    
    

def init():
    """ Inicializando Servo e Sensor HC-SR04 """
    angle = 90
    set_angle(angle)
    fs.distance    
    bs.distance
    


def frente():
    init()
    angle = 90
    set_angle(angle)
    fs.distance
    print('run forward')
    


def re():
    init()
    bs.distance
    print('\n Ré')
    sleep(0.5)
    print('\n stop')
    sleep(0.5)
        

def melhor_pos():
    z = 3  # range do for
    direcao = []  # lista para armazenar posição
    # scaneando posição
    angle = 15
    set_angle(angle)
    for x in range(z):
        direita = []
        fs.distance
        sleep(1)
        direita.append(fs.distance)                
        dmenor = min(direita)
        
    direcao.append(dmenor)
        
    angle = 90
    set_angle(angle)                
    sleep(0.5)
    
    angle = 180
    set_angle(angle)
    for y in range(z):
        esquerda = []
        fs.distance
        sleep(1)
        esquerda.append(fs.distance)                
        emenor = min(esquerda)
        
    direcao.append(emenor)
    
    # verificando a melhor posição
    melhor_dir = min(direcao)
    i = direcao.index(melhor_dir)  # indexando a melhor posição
    return i

            
try:
    init()
    while True:
        init()
        if fs.in_range is False:  # enquando verdade andar p/ frente
            frente()
            sleep(0.5)
            
        # recuando
        if bs.in_range is False:                    
            re()
            
        l = melhor_pos()
                    
        # virando para a melhor posição
        if l == 0:
            vd = 'Direita'
            print(vd)                
        
        if l == 1:
            ve = 'Esquerda'
            print(ve)
        else:
            print('frente')
            frente()       
        
except KeyboardInterrupt:
    print('\n Fui!')
    print("cleaning up")
    pwm.stop()
    GPIO.cleanup()
    