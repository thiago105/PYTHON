n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
m = (n1 + n2) / 2

print('sua media é de: {}'.format(m))

if m >= 6.0:
    print('Uau sua media foi boa')
else:
    print('nossa que nota ruim')

print('Parabens' if m >= 6.0 else 'Estude mais' )