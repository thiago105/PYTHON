tempo = int(input("Quantos anos tem seu carro? "))

if tempo <=3:
  print('carro novo')
else: 
  print('carro velho')

# OU

print('carro novo' if tempo <=3 else 'carro velho')