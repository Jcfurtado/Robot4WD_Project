import RPi.GPIO as gpio
from gpiozero import DistanceSensor
from time import sleep

# Pin
servo_pin = 18

fs = DistanceSensor(echo= 23, trigger= 4, max_distance= 1, threshold_distance= 0.2)
bs = DistanceSensor(echo= 24, trigger= 16, max_distance= 1, threshold_distance= 0.1)

''' Ponte H / Fio / BCM / BOARD:
ni1 - verde         (5)   (29)  
ni2 - amarelo       (6)   (31)  
ni3 - azul          (7)   (24)  
ni4 - roxo          (8)   (26)  
'''
ni_1 = 5
ni_2 = 6
ni_3 = 7
ni_4 = 8

#Iniciar o pino gpio
gpio.setmode(gpio.BCM)
gpio.setup(servo_pin, gpio.OUT)


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
pwm = gpio.PWM(servo_pin,f)
pwm.start(0)



# definindo o Angulo
def set_angle(angle):    
    duty = deg_0_duty + (int(angle)/180.0) * duty_range
    pwm.ChangeDutyCycle(duty)    



# Ligando os motores
def init_motores():
    """ Ligando os Motores """
    gpio.setmode(gpio.BCM)
    gpio.setup(ni_1, gpio.OUT)
    gpio.setup(ni_2, gpio.OUT)
    gpio.setup(ni_3, gpio.OUT)
    gpio.setup(ni_4, gpio.OUT)


def forward():
    """ Motores para frente """
    init_motores()
    gpio.output(ni_1, False)
    gpio.output(ni_2, True)
    gpio.output(ni_3, False)
    gpio.output(ni_4, True)
    sleep(1)
    

def reverse():
    """ Motores dando Ré """
    init_motores()
    gpio.output(ni_1, True)
    gpio.output(ni_2, False)
    gpio.output(ni_3, True)
    gpio.output(ni_4, False)
    sleep(1)
    

def turn_right():
    """ Motores virando a Direita """
    init_motores()
    gpio.output(ni_1, True)
    gpio.output(ni_2, False)
    gpio.output(ni_3, False)
    gpio.output(ni_4, True)
    sleep(1)
    
    
def turn_left():
    """ Motores virando a Esquerda """
    init_motores()
    gpio.output(ni_1, False)
    gpio.output(ni_2, True)
    gpio.output(ni_3, True)
    gpio.output(ni_4, False)
    sleep(1)
    
    
def stop():
    """ Motores Parados """
    init_motores()
    gpio.output(ni_1, False)
    gpio.output(ni_2, False)
    gpio.output(ni_3, False)
    gpio.output(ni_4, False)    
    gpio.cleanup()
    
    
# Inicializando Direção / Sensor de Distancia
def init():
    """ Inicializando Servo e Sensor HC-SR04 """
    angle = 90
    set_angle(angle)
    for f,b in range():
        f = fs.distance
        b = bs.distance
    return f, b
        


def obs_frente():
    """ Procurando Obstáculo na Frente """
    init()
    angle = 90
    set_angle(angle)
    fs.distance
    
    


def obs_re():
    """ Procurando Obstáculo Atrás """
    init()
    bs.distance
    sleep(0.5)
    
    
        

def melhor_pos():
    direcao = []  # lista para armazenar posição
    
    # scaneando
    sleep(1)
    angle = 15
    set_angle(angle)
    direita = fs.in_range  # Verificando range direito
    
    sleep(1)
    angle = 90
    set_angle(angle)
    frente = fs.in_range  # Verificando range frente
    
    sleep(1)
    angle = 180
    set_angle(angle)
    esquerda = fs.in_range  # Verificando range esquerdo
    
    re = bs.in_range  # Verificando range Traseiro
    
    if frente is not True:  # condição para ir em frente
        print('Seguindo em Frente!')
        return frente
    elif direita is not True:  # condição para virar a direita
        print('Virando à Direita')
        return direita
    elif esquerda is not True:  # condição para virar a esquerda
        print('Virando à Esquerda')
        return esquerda
    elif re is not True:  # condição para dar ré
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
    
    while True:        
        init()
        if fs.in_range is False:  # enquando verdade andar p/ frente
            print('run forward')
            obs_frente()
            forward()

        else:
            melhor_pos()  # procurando...
                        
            # virando para a melhor posição
            if l == 0 or melhor_pos() is False:
                turn_right()
                print('l=0 ', melhor_pos())
            
            elif l == 1 or melhor_pos() is False:
                forward()
                print('l=1 ', melhor_pos())
                
            elif l == 2 or melhor_pos() is False:
                turn_left()
                print('l=2 ', melhor_pos())
                
            elif l == 3 or melhor_pos() is False:
                reverse()
                print('l=3 ', melhor_pos())

            ''' continuar...

            
        else:
            print('stop')
            stop()
                
    else:
        print('erro')
                
        
except KeyboardInterrupt:
    print('\n Fui!')    
    pwm.stop()
    gpio.cleanup()
    print("cleaning up")    
'''