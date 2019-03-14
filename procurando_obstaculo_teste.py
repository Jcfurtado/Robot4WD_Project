''' Seaching... '''
import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from time import sleep


# Testando o in_range
# Padrão threshold_distance 0.3m
td_f = 0.2
td_b = 0.1
# Padrão max_distance: 1m
md_f = 1.0
md_b = 1.0

# PINs
sFront = DistanceSensor(echo = 23, trigger = 4, threshold_distance = td_f, max_distance = md_f)
sBack = DistanceSensor(echo = 24, trigger = 16, threshold_distance = td_b, max_distance = md_b)

#servo
servo_pin = 18

# AJUSTES DO SERVO
#Ajuste estes valores para obter o intervalo completo do movimento do servo
deg_0_pulse   = 0.5
deg_180_pulse = 2.5
f = 50

# AJUSTES DO SERVO
# Faca alguns calculos dos parametros da largura do pulso
period = 1000/f
k      = 100/period
deg_0_duty = deg_0_pulse * k
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k
 
# Iniciar o pin do gpio
GPIO.setmode(GPIO.BCM)

# Set GPIO ports Servo
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,f)
#pwm.start(0)

# Definindo o ângulo
def set_angle(angle):    
    duty = deg_0_duty + (int(angle)/180.0) * duty_range
    pwm.ChangeDutyCycle(duty)

# SENSOR ULTRASSONICO threshold_distance / max_distance
print("Padrão: threshold_distance: 0.3m / max_distance: 1.0m")
print("Frente: threshold_distance: {}m / max_distance: {}m".format(sFront.threshold_distance, sFront.max_distance))
print("Costas: threshold_distance: {}m / max_distance: {}m".format(sBack.threshold_distance, sBack.max_distance))


pwm.start(0)

for n in range(2):
    #n += 1
    
    print("\nFrente")
    for f in range(1):
        
        angle = 90
        set_angle(angle)
        sleep(1)
        print("Angulo {} - Distancia: {:.2f}m - in_range = {}".format(angle, sFront.distance, sFront.in_range))
        
        angle = 15
        set_angle(angle)
        sleep(1)
        print("Angulo {} - Distancia: {:.2f}m - in_range = {}".format(angle, sFront.distance, sFront.in_range))
                
        angle = 90
        set_angle(angle)
        sleep(1)
        print("Angulo {} - Distancia: {:.2f}m - in_range = {}".format(angle, sFront.distance, sFront.in_range))
        
        angle = 180
        set_angle(angle)
        sleep(1)
        print("Angulo {} - Distancia: {:.2f}m - in_range = {}".format(angle, sFront.distance, sFront.in_range))
                
        angle = 90
        set_angle(angle)
        sleep(1)
        print("Angulo {} - Distancia: {:.2f}m - in_range = {}".format(angle, sFront.distance, sFront.in_range))
                
        angle = 15
        set_angle(angle)
        sleep(1)
        print("Angulo {} - Distancia: {:.2f}m - in_range = {}".format(angle, sFront.distance, sFront.in_range))
        
        angle = 90
        set_angle(angle)
        sleep(1)
        print('Angulo {} - Distancia: {:.2f}m - in_range = {}'.format(angle, sFront.distance, sFront.in_range))
               
    print("\nCostas")    
    for b in range(5):               
        print("Distancia: {:.2f}m - In range =  {}".format(sBack.distance, sBack.in_range))
        sleep(0.5)
        
    if n == 0:
        print("\n ** Mudar a posição do Obstaculo **")
        sleep(15)
    else:
        print("\n Cleaning up")    
        break
pwm.stop()
