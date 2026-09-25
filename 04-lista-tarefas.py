# LISTA DE TAREFAS

# 1 - Mostrar todas tarefas
# 2 - Mostrar tarefas concluídas
# 3 - Mostrar tarefas pendentes
# 4 - Mostrar tarefas por prioridade
# 5 - Cadastrar tarefa nova
# 6 - Finalizar tarefa
# 7 - Remover tarefa
# 0 - Sair do sistema

tarefas = [
    {"titulo": "Estudar", "concluida": "Sim", "prioridade": "Alta"},
    {"titulo": "Ler", "concluida": "Não", "prioridade": "Baixa"},
    {"titulo": "Jogar videogame", "concluida": "Não", "prioridade": "Baixa"},
    {"titulo": "Ir à academia", "concluida": "Não", "prioridade": "Alta"},
    {"titulo": "Lavar louça", "concluida": "Sim", "prioridade": "Baixa"}
]

while True:
    print("LISTA DE TAREFAS")
    print("1 - Mostrar todas tarefas")
    print("2 - Mostrar tarefas concluídas")
    print("3 - Mostrar tarefas pendentes")
    print("4 - Mostrar tarefas por prioridade")
    print("5- Cadastrar tarefa nova")
    print("6 - Finalizar tarefa")
    print("7 - Remover tarefa")
    print("0 - Sair")
    
    opcao = input("Escolha sua opção: ")
    
    if opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opcão inválida. Tente novamente.")