num = int(input('Digite um numero de 0 a 9999: '))

# versao com str
n = str(num)
print('Analizando numero {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centenas: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

# versao matematica
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analizando numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))