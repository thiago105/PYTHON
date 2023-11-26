import math
from math import radians, sin, cos, tan

angulo = float(input('Digite um valor: '))

seno1 = math.sin(math.radians(angulo))
seno2 = sin(radians(angulo))

cosseno1 = math.cos(math.radians(angulo))
cosseno2 = cos(radians(angulo))

tangente1 = math.tan(math.radians(angulo))
tangente2 = tan(radians(angulo))

print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, seno1))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, seno2))

print('o angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno1))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno2))

print('o angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente1))
print('o angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente2))