import json
import random

backlog = []


def adicionar_item(descricao):
    """Adiciona um item ao backlog com um ID único e crescente."""
    novo_id = len(backlog) + 1  # Define o próximo ID
    item = {"id": novo_id, "descricao": descricao}
    backlog.append(item)
    print(f'Item "{descricao}" adicionado ao backlog com ID {novo_id}.')
    salvar_backlog()  # Salva o backlog após adicionar um item


def mostrar_backlog():
    """Exibe todos os itens no backlog com seus IDs."""
    if backlog:
        print("Itens no backlog:")
        for item in backlog:
            print(f'{item["id"]}. {item["descricao"]}')
    else:
        print("O backlog está vazio.")


def sortear_item():
    """Seleciona um item aleatório do backlog."""
    if backlog:
        item_selecionado = random.choice(backlog)
        print(
            f'Item sorteado: "{item_selecionado["descricao"]}" (ID: {item_selecionado["id"]})'
        )
        return item_selecionado
    else:
        print("O backlog está vazio. Não é possível sortear.")
        return None


def remover_item(id):
    """Remove um item específico do backlog pelo ID."""
    for item in backlog:
        if item["id"] == id:
            backlog.remove(item)
            print(f'Item "{item["descricao"]}" com ID {id} removido do backlog.')
            salvar_backlog()  # Salva o backlog após remover um item
            return
    print(f"Item com ID {id} não encontrado no backlog.")


def salvar_backlog():
    """Salva o backlog em um arquivo JSON."""
    with open("backlog.json", "w") as arquivo:
        json.dump(backlog, arquivo, indent=4)
    print("Backlog salvo em backlog.json.")


def carregar_backlog():
    """Carrega o backlog de um arquivo JSON, se existir."""
    global backlog
    try:
        with open("backlog.json", "r") as arquivo:
            backlog = json.load(arquivo)
        print("Backlog carregado de backlog.json.")
    except FileNotFoundError:
        print("Arquivo backlog.json não encontrado. Iniciando backlog vazio.")


def menu():
    carregar_backlog()  # Carrega o backlog ao iniciar o programa
    while True:
        print("\nMenu:")
        print("1. Adicionar item ao backlog")
        print("2. Mostrar backlog")
        print("3. Sortear item")
        print("4. Remover item")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            descricao = input("Digite a descrição do item para adicionar ao backlog: ")
            adicionar_item(descricao)
        elif escolha == "2":
            mostrar_backlog()
        elif escolha == "3":
            sortear_item()
        elif escolha == "4":
            try:
                id = int(input("Digite o ID do item para remover do backlog: "))
                remover_item(id)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
