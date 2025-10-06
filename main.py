import os
import platform

opcoes_menu = ["Adicionar tarefas", "Exibir tarefas", "Remover tarefas"]
lista_de_tarefas = []

def menu_principal(): # alterar nome da função 
    titulo = "Bem-vindo(a) ao PyTask"
    borda = (len(titulo)+2)*"-"

    print(borda)
    print(titulo)
    print(f"{borda}\n\n")

def listar_menu_principal():
    for i, opcao in enumerate(opcoes_menu, start=1):
        print(f"{[i]} - {opcao}")

def selecionar_opcao_menu():
    opcao_selecionada = int(input("\n O que deseja fazer? "))
    return opcao_selecionada

def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def adicionar_tarefa():
    limpar_tela()

    titulo = "Adicionando tarefas"
    borda = (len(titulo) + 2)*"-"

    print(f"\n{borda}")
    print(titulo)
    print(f"{borda}\n\n")

    titulo_tarefa = input("Título tarefa: ")

    tarefa = {
        "titulo_tarefa":titulo_tarefa,
        "status":False
    }

    lista_de_tarefas.append(tarefa)

    # temporário

    limpar_tela()

def listar_tarefas():
    limpar_tela()

    titulo = "Lista de tarefas"
    borda = (len(titulo) + 2)*"-"

    print(f"\n{borda}")
    print(titulo)
    print(f"{borda}\n\n")

    for i, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"{[i]} - {tarefa}")

    # temporário

    # limpar_tela()

def remover_tarefas():
    limpar_tela()

    titulo = "Remover tarefas"
    borda = (len(titulo) + 2)*"-"

    print(f"\n{borda}")
    print(titulo)
    print(f"{borda}\n\n")

    for i, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"{[i]} - {tarefa}")

    indice_tarefa = int(input("\nQual tarefa você quer remover? "))

    indice_tarefa = indice_tarefa - 1

    lista_de_tarefas.pop(indice_tarefa)

    print("Tarefa removida com sucesso!")

while True:
    menu_principal()

    listar_menu_principal()

    resposta = selecionar_opcao_menu()

    if resposta == 1:
        adicionar_tarefa()
    elif resposta == 2:
        listar_tarefas()
    elif resposta == 3:
        remover_tarefas()
    else:
        print("Encerrando Sistema")