#carro custa R$60/dia e R$0,15 km rodados

dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))

valorCarro = 60
valorKm = 0.15

soma = (valorCarro * dias) + (valorKm * km)

print('total a pagar é R${:.2f}'.format(soma))
