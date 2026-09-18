def mostrar():
    for x in lista:
        print(f"{x}")

def cadastrar():
    item = input("Digite o item que deseja adicionar na lista: ")
    lista.append(item)

def remover():
    item = input("Digite qual item da lista deseja remover: ").lower()
    lista.remove(item)
    

    
lista = ["Pão, Banana, Maçã, Limão, Queijo, Presunto, Refrigerante"]

while True:
    print ("LISTA DE COMPRAS")
    print ("1 - Mostrar lista")
    print ("2 - Cadastrar item na lista")
    print ("3 - Excluir item da lista")
    print ("4 - Modificar item da lista")
    print ("0 - Sair")
    
    opcao = input("Escolha sua opção: ")
    
    if opcao == "1":
        mostrar()
    elif opcao == "2":
        cadastrar()
    elif opcao == "3":
        remover()
    elif opcao == "0":
        print ("Saindo do sistema...")
        break