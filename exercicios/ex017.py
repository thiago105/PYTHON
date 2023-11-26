import math

catOposto = float(input('comprimento do cateto oposto: '))
catAdjacente = float(input('comprimento do cateto adjacente'))

hipo1 = (catOposto ** 2 +catAdjacente ** 2) ** (1/2)
hipo2 = math.hypot(catOposto, catAdjacente)

print('O valor da hipotenusa é {:.2f}'.format(hipo1))
print('O valor da hipotenusa é {:.2f}'.format(hipo2))