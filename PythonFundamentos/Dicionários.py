"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conehecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
        - Chave e valor são separados por dois pontos 'chave:valor'
        - Tanto chave quanto vvalor podem ser de qualquer tipo de dado:
        - Podemos misturar tipos de dados;


# Criação de dicionários
# Forma 1 [Mais comum]
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

-------------- Acessando elementos ------------------

# Forma 1 - Acessando via chave, da mesma forma que lsita/tupla
print(paises['br'])
print(paises['py'])

# Forma 2 - Via get - Recomendada.

print(paises.get('br'))
print(paisses.get('uk'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError


# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

localidades = {
        (35.8568, 39.6987): 'Escritório no Rio de Janeiro',
        (44.8568, 40.667): 'Escritório no Espirito Santo',
        (69.5668, 20.6987): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar':300}

# forma 1 (mais comum)
receita['abr'] = 350
print(receita)

# forma 2 

novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)


----------------- Atualizando dados em um dicionário --------- 

# fomra 1

receita['mai'] = 550
print(receita)

# forma 2

receita.update({'Mai' = 600})
print(receita)

# Conclusão: A forma de adicionar elementos ou atualzar dados em um dicionário é a mesma.
# Conclusão2: Em dicionários, NÃO podemos ter chaves repetidas.


--------------- REMOVENDO ITENS -----------------------
# Forma 1:
ret = receita.pop('mar')
print(ret)

print(receita)

# OBS: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev']
print(receita)

"""
  # Imagina que você tem um comércio eletrónico, aonde temos um carrinho de compras na qual adicionamos produtos.

"""
Carrinho de Compras:
        Produto 1:
                -nome;
                -quantidade;
                -preço
        Produto 2:
                -nome;
                -quantidade;
                -preço
"""
"""

# Da pra fazer por lista? Sim

carrinho = []

produto1 = ['Playstation 5', 1, 2300.00]
produto2 = ['Dayz', 1, 150.00]


carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriámos que saber qual é o indice de cada informação no produto.
# 2 - Poderíamos utlizar uma tupla para isso? SIM

produto1 = ['Playstation 5', 1, 2300.00]
produto2 = ['Dayz', 1, 150.00]

carrinho = (produto1, produto2)
print(carrinho)

# Teriámos que saber qual é o indice de cada informação no produto.

carrinho = []

produto1 = {'nome': 'Playstation 5', 'Quantidade': 1, 'Valor': 2500.00}
produto2 = {'nome': 'Dayz', 'Quantidade': 1, 'Valor': 250.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho em cada produto
# podemos ter a certeza sobre cada informação.


# Metódos do dicionário

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Copiando um dicionário para o outro

# Forma 1 # Deep Copy

novo = d.copy()  
print(novo)

novo['d'] = 4

print(d)
print(novo)

# Metódos do dicionário

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Forma 2 # Shallow Copy

novo = d
print(novo)
novo['d'] = 4

print(d)
print(type(d))
"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys({'a','b'}

print(outro)
print(type(outros))

usuario = {}.fromkeys{['nome', 'pontos', 'email', 'profile'], 'desconhecido'}
print(usuario)
print(type(usuario))

# O método FromKeys recebe dois parámetros: interável e um valor.
# Ele vai gerar para cada valor do interável uma chave e irá atribuir a esta chave o valor inferior informado.
