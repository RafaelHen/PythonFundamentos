"""
 Listas 

É POSSÍVEL SOMAR AS LISTAS

Listas em Python funcionam como vetores e matrizes (Arrays) em outras linguagens, com a diferença de serem DINÂMICO e 
também podermos colocar QUALQUER tipo de dados.

 Linguagens C/JAVA: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se voce cria um array do tipo int e com tamanho 5,
    este array SEMRPE sera do tipo inteiro e poderá ter no máximo 5 valores.

Em Python:

- Dinâmico: Não possui tamanho fixo: Ou seja, podemos criar a lista e simplesmente ir adicionando elementos:
- Qualquer tipo de dado: As listas não possuem tipo de dados fixos; podemos colocar qualquer tipo de dado.


lista1 = list(range(11232))
lista2 = [1, 1, 1, 2, 3, 6, 32, 17, 22, 69, 89, 40, 42, 10, 9, 7, 6, 0]
lista3 = ['r','a','f','a','e','l']
lista4 = ['Rafael','Victor','de','Oliveira']



#Checando valor na lsita:
if 4 in lista1:
   print(f"Encontrei o número {4}")
else:
    print("Não encontrei")

# Ordenando a lista do menor para o maior:
lista2.sort()
print(lista2)

# Contando o número de ocorrência(repetidas) de um valor na lista
print(lista2.count(1)) #Quantos numeros 1 tem na lista 2
print(lista3.count('a')) #Quantos 'a' tem na lista 3

# Adicionar elementos - Só da pra adicionar um elemento por vez.
lista3.append('victor') # Coloca a lista como elemento único.
print(lista3)

lista2.extend([10, 20, 30, 40]) # Coloca elementos da lista como valor adicional. Não aceita valor unico

# Remove o ultimo elemento da lista, da para remover também pelo indice.
lista3.pop(6)
print(lista3)

# Zerar a lista

lista1.clear()

# Inserindo elemento na lista informando posição do indice.
lista1.insert(1, 11)
print(lista1)

# Inverter lista
lista1.reverse()

# Copiar uma lista
lista4 = lista1.copy()

# Lendo o tamanho de uma lista
print(len(lista1))

# Convertendo string em uma lista
# Exemplo 1

curso = 'Fazendo curso de python'
curso = curso.split()
OBS: O SLIPT SEPARA OS ELEMENTOS DA LISTA PELO ESPAÇO ENTRE ELAS.

# Exemplo 2

curso = 'Fazendo,curso,de,python'
curso = curso.split(',')

# Lista em String

# Pega a lista4, coloca espaço entre cada elemento e transforma em String
teste = ' '.join(lista4)
print(teste)


# While em lista

carrinho = []
produto = ''

while produto != 'sair':
    print('Informe o nome do produto, quando acabar digite sair.')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Colocando indices em elementos.
cores = ['verde', 'amarelo', 'azul', 'branco']

for index, cor in enumerate(cores):
    print(index, cor)

print(enumerate(cores))


"""

# Revisão de Slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parâmero 'inicio'
