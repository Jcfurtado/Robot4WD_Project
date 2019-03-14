import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from time import sleep

# Pin do servo
servo_pin = 18

# Pin Sensor Ultrassonico de distancia (HC-SR04)
fs = DistanceSensor(echo= 23, trigger= 4, max_distance= 2, threshold_distance= 0.1)
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
    
    
def melhor_pos():
    direcao = []  # lista para armazenar posição
    
    # scaneando
    sleep(1)
    angle = 15
    set_angle(angle)
    direita = fs.in_range  # Verificando range direito
    print('Direita {:.2f} m - in range {}'.format(fs.distance, direita))
        
    sleep(1)
    angle = 90
    set_angle(angle)
    frente = fs.in_range  # Verificando range frente
    print('\nFrente {:.2f} m - in range {}'.format(fs.distance, frente))
        
    sleep(1)
    angle = 180
    set_angle(angle)
    esquerda = fs.in_range  # Verificando range esquerdo
    print('\nEsquerda {:.2f} m - in range {}'.format(fs.distance, esquerda))
        
    re = bs.in_range  # Verificando range Traseiro
    print('\nRé {:.2f} m - in range {}'.format(bs.distance, re))
    
    sleep(1)
    angle = 90
    set_angle(angle)
    
    # Escolhendo:
    if frente is False:  # condição para ir em frente
        print('Seguindo em Frente!')
        return frente
    elif direita is False:  # condição para virar a direita
        print('Virando à Direita')
        return direita
    elif esquerda is False:  # condição para virar a esquerda
        print('Virando à Esquerda')
        return esquerda
    elif re is False:  # condição para dar ré
        print('Dando Ré... CUIDADO!')
        return re
    
    else:  # caso as 4 posições estiver dentro do range escolher a maior distancia
        
        direcao = []  # lista para armazenar as posições
        
        # scaneando posição
        sleep(1)
        angle = 15
        set_angle(angle)        
        for direita in range(3):  # Verificando DIREITA - i=0
            direita = []
            direita.append(fs.distance)
            dmaior = max(direita)
            
        direcao.append(dmaior)
        
        sleep(1)
        angle = 90
        set_angle(angle)
        for frente in range(3):  # Verificando FRENTE - i=1
            frente = []
            frente.append(fs.distance)
            fmaior = max(frente)
            
        direcao.append(fmaior)
        
        sleep(1)
        angle = 180
        set_angle(angle)
        for esquerda in range(3):  # Verificando ESQUERDA - i=2
            esquerda = []
            esquerda.append(fs.distance)
            emaior = max(esquerda)
            
        direcao.append(emaior)        
        
        for traseira in range(3):  # Verificando TRASEIRA - i=3
            traseira = []
            traseira.append(bs.distance)
            tmaior = max(traseira)
            
        direcao.append(tmaior)
        
        melhor_dir = max(direcao)  # verificando a maior posição
        i = direcao.index(melhor_dir)  # indexando a posição
        
        return i, direcao[i]
 
 
try:
    for t in range(3):
        melhor_pos()
        
except KeyboardInterrupt:
    print('\n Fui!')
    print("cleaning up")
    pwm.stop()
    GPIO.cleanup()

