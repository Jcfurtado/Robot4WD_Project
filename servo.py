import RPi.GPIO as GPIO
from time import sleep
 
servo_pin = 18
 
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
 
#Iniciar o pino gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,f)
pwm.start(0)

def set_angle(angle):    
    duty = deg_0_duty + (int(angle)/180.0) * duty_range
    pwm.ChangeDutyCycle(duty)
    

angle = 90                
set_angle(angle)
 
try:
    r = str(input('Escolha entre modo Manual [M] e Automático [A] - '))
    resp = r.lower()
    
    while resp == 'a' or resp == 'm':        
        if resp == 'm':            
            angle = int(input('Entre com o Ângulo (0 a 180): '))
            
            while angle < 181:                
                set_angle(angle)
                angle = int(input('Entre com o Ângulo (0 a 180): '))
            else:
                print('Bye!')
                break
                    
        else:
            c = int(input('Digite a quantidade de movimentos: '))
            if c > 0:
                for v in range(c):
                    angle = 15
                    set_angle(angle)
                    sleep(1.5)
                    
                    angle = 45
                    set_angle(angle)
                    sleep(1.5)
                    
                    angle = 90                
                    set_angle(angle)
                    sleep(1.5)
                    
                    angle = 135
                    set_angle(angle)
                    sleep(1.5)
                    
                    angle = 180
                    set_angle(angle)
                    sleep(1.5)
                    
                    angle = 135
                    set_angle(angle)
                    sleep(1.5)
                    
                    angle = 90
                    set_angle(angle)
                    sleep(1.5)
                    
                    angle = 45
                    set_angle(angle)
                    sleep(1.5)
                
            else:
                pwm.stop()
                print('Bye!')
                break
finally:
    print("cleaning up")
    pwm.stop()
    GPIO.cleanup()
    