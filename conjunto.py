"""
Conjunto 

- CONJUNTOS em qulquer linguagem de programação, estamso fazendo referência á teoria dos conjuntos da
matemática.

 - Conjuntos são chamados de Sets.

 Dito isto, da mesma forma que na matemática:

 - Sets (conjuntos) não possuem valores duplicados;
 - Sets (conjuntos) não possuem valores ordenados;
 - Elementos não são acessados via indice, ou seja, conjuntos não são indexaods;

 Conjuntos são bons para se utilizar quando precisamos armazenar elementos
 mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves,
 valores e itens duplicados.

 Os conjuntos (sets) são referenciados em Python com chaves {}

 Difença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

S = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3,}) # repare nos valos repetidos

print(type(S))
print(S)

# Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo será ignorado
# Sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

# Além de não ter valores duplicados, não temos ordem

# Assim como todo outro conjunto Python podemos colocar tipos de dados mistruados no Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for bosta in s:
    print(bosta) 

# Usos interessantes com Sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# Informam manualmente a cidade onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que uma lista podemos adicionar novos elementos
# e podemos ter repetição


cidades = ['Belo Horizonte', 'São paulo', 'Belo Horizonte', 'Espirito Santo']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos.
# Podemos usar o set para isso:

print(len(set(cidades)))


# Adicionando elementos em um conjunto
s = {1,2,3}

s.add(4)
print(s)

# Forma 1
s.remove(3) # Não é indice, é valor
print(s)

# Forma 2

s.discard(2)
print(s)

# Se o valor não for encontrado, nenhum erro é gerado


estudantes_python = {'Rafael', 'Fabio', 'Gabriel', 'Wesley'}
estudantes_java = {'Gustavo','Fabio','Marcos','Matheus'}

# Alguns estudantes de python também estudam java, mas eu preciso gerar um conjunto
# com nomes de estudantes únicos

# Forma 1 - usando union (União)

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - usando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Alguns estudantes de python também estudam java, mas eu preciso gerar um conjunto
# de estudantes que estão em ambos os cursos

# Forma 1 - Usando o intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - usando o &¨

ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

"Dicionarios = " # Não aceitam valores duplicados 
"Conjuntos = " # Não aceitam valores duplicados também


estudantes_python = {'Rafael', 'Fabio', 'Gabriel', 'Wesley'}
estudantes_java = {'Gustavo','Fabio','Marcos','Matheus'}
