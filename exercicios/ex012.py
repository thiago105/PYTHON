preco = float(input('qual preço do produto? R$ '))
desconto = preco - (preco * 5 / 100)

print('O produto que custava R${:.2f} na promoção de 5% passa custar R${:.2f}'.format(preco, desconto))

