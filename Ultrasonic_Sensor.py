from gpiozero import DistanceSensor
from time import sleep

f = DistanceSensor(echo= 23, trigger= 4,max_distance= 1, threshold_distance= 0.3)
b = DistanceSensor(echo= 24, trigger= 16, max_distance= 1, threshold_distance= 0.3)


print("threshold_distance: F: {:.2f} m - B: {:.2f} m".format(f.threshold_distance, b.threshold_distance))
print("max_distance: F: {:.1f} m - B: {:.1f} m".format(f.max_distance, b.max_distance))
try:
    while True:
                        
        print('\nFrente')
        for n in range(3):    
            print('Distancia: {:.2f} m - in range =  {}'.format(f.distance, f.in_range))
            sleep(1)

        print('\nCostas')
        for n in range(3):    
            print('Distancia: {:.2f} m - in range =  {}'.format(b.distance, b.in_range))
            sleep(1)
except KeyboardInterrupt:
    print('\n bye')

