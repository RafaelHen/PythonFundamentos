"""

# Diferença entre Parâmetros e Argumentos

# Parametros são variáveis declaradas na definição de uma função;
# Argumento são dados passados durante a execução de uma função;


Funções com Parâmetro (de entrada)

- Funções que recebem dados ara serem processados dentro da mesma:

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:

- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função

def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

# Refatorando a função

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}')

cantar_parabens('Patricia')

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em um função quantos parâmetros forem necessários; Eles são separados por vírgula.

# Exemplo
        #parametro "a", parametro "b"
def soma(a,b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2
           
def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(3, 2, 'Python '))

# Se agente informar um numero errado de parâmetro ou argumentos teremos TypeError

# print(soma(2, 3, 4)) #TypeError . Pssando argumento a mais
# print(soma(4))  #TypeError - Passando argumentos a menos

"""

