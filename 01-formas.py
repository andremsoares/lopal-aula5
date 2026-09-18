def circulo():
    raio = float(input("Qual o valor do raio do círculo? "))
    resultado = 3.14 * raio ** 2
    print (f"A área do círculo é: {resultado}")
    
def triangulo():
    base = float(input("Qual o valor da base do triângulo? "))
    altura = float(input("Qual o valor da altura do triângulo? "))
    resultado = (base * altura) / 2
    print (f"A área do triângulo é {resultado}")
    
def quadrado():
    lado = float(input("Qual o valor do lado do quadrado? "))
    resultado = lado ** 2
    print (f"A área do quadrado é {resultado}")

def retangulo():
    base = float(input("Qual o valor da base do retângulo? "))
    altura = float(input("Qual o valor da altura do retângulo? "))
    resultado = base * altura
    print (f"A área do retângulo é {resultado}")
    
def paralelogramo():
    base = float(input("Qual o valor da base do paralelogramo? "))
    altura = float(input("Qual o valor da altura do paralelogramo? "))
    resultado = base * altura
    print (f"A área do paralelogramo é {resultado}")
    
def losango():
    diagonal_maior = float(input("Qual o valor da diagonal maior do losango? "))
    diagonal_menor = float(input("Qual o valor da diagonal menor do losango? "))
    resultado = (diagonal_maior * diagonal_menor) / 2
    print (f"A área do losango é {resultado}")
    
def trapezio():
    base_maior = float(input("Qual o valor da base maior do trapézio? "))
    base_menor = float(input("Qual o valor da base menor do trapézio? "))
    altura = float(input("Qual o valor da altura do trapézio? "))
    resultado = (base_maior + base_menor) * altura / 2
    print (f"A área do trapézio é {resultado}")

while True:
    print ("CALCULADORA DE ÁREAS DAS FORMAS GEOMÉTRICAS")
    print ("1 - Círculo")
    print ("2 - Triângulo")
    print ("3 - Quadrado")
    print ("4 - Retângulo")
    print ("5 - Paralelogramo")
    print ("6 - Losango")
    print ("7 - Trapézio")
    print ("0 - Sair do sistema")
    
    opcao = input("Escolha sua opção: ")
    
    if opcao == "1":
        circulo()
    elif opcao == "2":
        triangulo()
    elif opcao == "3":
        quadrado()
    elif opcao == "4":
        retangulo()
    elif opcao == "5":
        paralelogramo()
    elif opcao == "6":
        losango()
    elif opcao == "7":
        trapezio()
    elif opcao == "0":
        print ("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")