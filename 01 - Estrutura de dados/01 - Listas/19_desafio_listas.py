#desafio: gerenciar lista de compras
"""
Crie um programa que simule uma lista de compras, onde o usuário pode:
Adicionar um item à lista
Remover um item da lista
Ver todos os itens
Verificar se um item está na lista
Sair do programa

Requisitos obrigatórios:
Use pelo menos os métodos: append(), remove(), sort() e o operador in.

"""
lista_compras = []

while True:
    print("\n--- Lista de Compras ---")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Verificar item")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item a ser adicionado: ")
        lista_compras.append(item)
        print(f"{item} adicionado com sucesso!")

    elif opcao == "2":
        item = input("digite o item a ser removido: ")
        if item in lista_compras:
         lista_compras.remove(item)
         print(f"{item} item removido com sucesso!")
        else:
            print(f"`{item} não está na lista!")

    elif opcao == "3":
        lista_compras.sort()
        print("aqui está sua lista completa: ")
        for item in lista_compras:
            print(item)
            
    elif opcao == "4":
        item = input("digite o item que deseja verfificar se está na lista de compras:")
        if item in lista_compras:
            print("está na lista!")
        else:
            print(f"{item} não está na lista")

    elif opcao == "5":
        break

