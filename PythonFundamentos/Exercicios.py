
print("Bem vindo à calculadora: \n 1 - Somar \n 2 - Subtrair \n 3 - Multiplicação \n 4 - sair")
opcao = int(input("Digite:"))

if(opcao == 1):
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero1 = numero1 + numero2
    print(numero1)

if(opcao == 2):
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero1 = numero1 - numero2
    print(numero1)
    
if(opcao == 3):
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero1 = numero1 * numero2
    print(numero1)

elif(opcao == 4):
    print("Saindo...")
else:
    print("Favor escolher uma opcão valdia.")