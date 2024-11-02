import json

# Inicializamos o backlog como uma lista vazia
backlog = []


def adicionar_item(item):
    """Adiciona um item ao backlog."""
    backlog.append(item)
    print(f'Item "{item}" adicionado ao backlog.')


def mostrar_backlog():
    """Mostra todos os itens no backlog."""
    if backlog:
        print("Itens no backlog:")
        for i, item in enumerate(backlog, start=1):
            print(f"{i}. {item}")
    else:
        print("O backlog está vazio.")


import random


def sortear_item():
    """Seleciona um item aleatório do backlog."""
    if backlog:
        item_selecionado = random.choice(backlog)
        print(f'Item sorteado: "{item_selecionado}"')
        return item_selecionado
    else:
        print("O backlog está vazio. Não é possível sortear.")
        return None


def remover_item(item):
    """Remove um item específico do backlog, se estiver presente."""
    if item in backlog:
        backlog.remove(item)
        print(f'Item "{item}" removido do backlog.')
    else:
        print(f'Item "{item}" não encontrado no backlog.')


def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar item ao backlog")
        print("2. Mostrar backlog")
        print("3. Sortear item")
        print("4. Remover item")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            item = input("Digite o item para adicionar ao backlog: ")
            adicionar_item(item)
        elif escolha == "2":
            mostrar_backlog()
        elif escolha == "3":
            sortear_item()
        elif escolha == "4":
            item = input("Digite o item para remover do backlog: ")
            remover_item(item)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
