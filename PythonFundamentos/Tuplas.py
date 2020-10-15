"""
Tuplas

Tuplas são parecidos com listas.

1 - As tuplas são representadas por parêtneses ()

2 - As tuplas são imutáveis: Ela não muda. Toda as operações em uma tupla gera 
uma nova tupla

#   As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

tupla3 = (4) # Isso não é uma tupla

tupla4 = (4,) # Isso é uma tupla!

# Podemos concluir que tuplas são definidas pela vérgula e não pelo uso do parênteses.

# Pode se gerar uma tupla dinamicamento com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)


# DESEMPACOTGAMENTO DE TUPLA

tupla = ('Rafael', 'Foda')

nome, aspecto = tupla
print(nome)
print(aspecto)

# Metoods de adição e remoção de elementos não existem na tupla. dado o fato das tuplas serem imutáveis.

# Soma*, valor Máximo*, Valor Minimo e Tamanho.
sum
max __  Só se os valores forem inteiros e reais.
min /
len/

# Iterando sobre uma tupla 

tupla = (1, 2, 3)

for n in tupla:
    print(n)

# MOSTRAR O INDICE E O VALOR DA TUPLA

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando os elementos de uma tupla

tupla = ('r','a','f','a','e','l')

print(tupla.count('a'))

# Devemos usar tupla SEMPRE que não precisamos modificar os dados contidos em uma coleção.

#Exemplo 1 



i = 0

while i < len(meses):
    print(meses[i])
    i += 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Novembro','Dezembro')

# Verificamos em qual indice um elemento está na tupla
print(meses.index('Junho'))

"""

# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que as litas.
# - Tuplas deixam o código mais seguro. Trabalhar com elementos imutáveis trás segurança para o código