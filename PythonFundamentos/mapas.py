"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}





print(receita)

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chava in receita:
    print(f'Em {chave} recebi R$: {receita[chave]}')

-----------------Acessando as chaves----------------

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

------------------Acessando os valores----------------

print(receita.values())

for valor in receita.values():
    print(valor)

-------------------Desempacotamento de Dicionários

"""

receita = {'jan': 100, 'fev': 120, 'mar':300}

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')