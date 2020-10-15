"""
Funções com Parâmetros Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado():
    return numero ** 2
     
print(quadrado(3))
print(quadrado())

---------------------------------------------------------------------------------------------

def expodencial(numero, potencia = 2):
    return numero ** potencia

print(expodencial(2, 3))
print(expodencial(3, 2))

print(expodencial(3)) # Por padrão eleva ao quadrado
print(expodencial(3, 5)) # Eleva a potencia informada pelo usuário

# Se o usuario passsar somente 1 argumento, este sera atribuido ao mesmo numero. e será calculado o quadrado deste numero.
# Se o usuario passar 2 argumentos, o primeiro sera atribuido ao parametro numero e o segundo a ao parametro potencia.
# Então será calculado a portência

--------------------------------------------------------------------------------------------------------

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração

# Erro!

def teste(num = 2, potencia):
    return num ** potencia

#Outros erros 

def soma(num1=5, num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())   # TypeError

--------------------------------------------------------------------------------------------

def mostra_informacoes(nome='Rafael', instrutor=True):
    if nome == 'Rafael' and instrutor:
        return f'Bem Vindo {nome}, o instrutor!'
    elif nome == 'Rafael':
        return 'Ue, pensei que era o instrutor'
    return f'Olá {nome}'

print(mostra_informacoes())
print(mostra_informacoes(instrutor=True))
print(mostra_informacoes(True))
print(mostra_informacoes('Michael'))
print(mostra_informacoes(nome = 'Marcos'))


# Porque usar parametros com valor defaut?

- Nos permite ser mais flexíveis nas funções
- Evita erros com parametros incorretos
- Nos permite trabalhar com exemplos mais legíveis de código

# Escopo - Evitar problemas e confusões...

#   Variaveis globais
#   Variaveis locais

intrutor  = 'Rafael'  # Variavl Global

def diz_oi():
    instrutor = 'Rafael' # Variavel local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.


# ATENÇÃO COM VARIAVEL GLOBAL (Se puder, EVITE!)

total = 3 
def icremento():
    global total 
    total = total + 1 
    return total

print(icremento())
"""
