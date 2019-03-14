from random import randint

a = []

p1 = 15
d1 = randint(0, 6)
a.append(d1)
print(p1, ' ', a)

p2 = 90
print(p2)

p3 = 180
d3 = randint(0, 6)
a.append(d3)
print(p3, ' ', a)

a_min = min(a)
a_max = max(a)

print('\n {} / -- / {}'.format(d1, d3))
print('\n min: {} / max: {}'.format(a_min, a_max))

i = a.index(a_min)
print('index: ', i)

if i == 0:
    vd = 'virar p/ direita'
    print(vd)
    

elif i == 1:
    ve = 'virar para esquerda'
    print(ve)
    
else:
    print('erro')
