salarioAntigo = float(input('qual salario do funcionario? R$ '))
salarioNovo = salarioAntigo + (salarioAntigo * 15 / 100)

print('Um funcionario que ganhava R${:.2f}, com 15% de aumento passa receber R${:.2f}'.format(salarioAntigo, salarioNovo))
