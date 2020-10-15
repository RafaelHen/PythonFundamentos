"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa,
desde que comece com asterísco. 

Exemplo:

*xis

Mas por convenção, usamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em ua tupla.
Então desde já lembre-se que tuplas são imutavéis.

#Exemplos

def soma_todos_numeros(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(4, 6))
print(soma_todos_numeros(4, 6, 9, 5))

# Entendendo o Args

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
"""

