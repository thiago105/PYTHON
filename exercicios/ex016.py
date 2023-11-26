from math import floor
import math

valor = float(input('Digite um valor: '))

prop1 = floor(valor)
prop2 = math.trunc(valor)
prop3 = int(valor)

print('o valor digitado foi {} e sua proporção inteira é {}'.format(valor, prop1))
print('o valor digitado foi {} e sua proporção inteira é {}'.format(valor, prop2))
print('o valor digitado foi {} e sua proporção inteira é {}'.format(valor, prop3))
