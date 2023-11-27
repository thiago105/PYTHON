frase = '   Curso em Video Python  '

# Fatiando str
print(frase[9]) # pega o valor do indice 9
print(frase[9:13]) # pega o valor do indice 9 ate o indice 12, indice 13 é excluido
print(frase[9:21:2]) # pega o valor do indice 9 ate o indice 20, (indice 21 é excluido) pulando de 2 em 2
print(frase[:5]) # pega o valor do inicio do indice e vai ate o indice 4 (indice 5 é excluido)
print(frase[15:]) # pega valor apartir do indice 15 ate o final, mesmo que [15:21]
print(frase[9::3]) # pega valor apartir do indice 9 ate o final, pulando de 3 em 3, mesmo que [9:21:3]

# analisando str
print(len(frase)) # vem do length ou seja tamanho da variavel frase, qntd de indice
print(frase.count('o')) # vem de contagem ou seja qntd de letras 'o' contem na variavel frase
print(frase.count('o', 0, 13)) # faz uma contagem de letras 'o' ja com fatiamento [0:13] pegando do indice 0 ate o indice 12 (indice 13 é excluido)
print(frase.find('deo')) # pega o indice onde a str 'deo' iniciou, trazendo apenas o indice que iniciou
print('Curso' in frase) # faz um tipo Boolean, existe a palavra 'Curso' na variavel frase

# Transformação str
print(frase.replace('Python', 'Android')) # procura a palavra 'Python' da variavel frase e substitui 'Python' para 'Android' (de forma interna)
print(frase.upper()) # passa tudo para maiusculo
print(frase.lower()) # passa tudo para minusculo
print(frase.capitalize()) # pega toda a frase e passa minuscula, deixando apenas a primeira letra como maiuscula
print(frase.title()) # a cada espaço entre palavras, as primeiras letras de cada palavra é passado para maiuscula
print(frase.strip()) # remove espaços em branco do inicio e do fim da str
print(frase.lstrip()) # remove espaços em branco apenas do inicio da str
print(frase.rstrip()) # remove espaços em branco apenas do final da str

# Divisão str
print(frase.split()) # gera um array, onde cada espaço entre uma palavra e outra é feito uma divisão de palavras e cada palavra recebe um nove indice

# Junção
print('-'.join(frase)) # adiciona - para cada letra e espaço em branco da variavel str