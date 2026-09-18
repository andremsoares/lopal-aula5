def circulo():
    raio = float(input("Qual o valor do raio do círculo?"))
    resultado = 3.14 * raio ** 2
    print (f"A área do círculo é: {resultado}")

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
    