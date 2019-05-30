import dados
import geral
import pickle

def menu_principal():
    print(20 * "-=")
    print("       Menu")
    print(20 * "-=")

    print("--------------------\n"
          "1 - Cadastrar Pessoas\n"
          "2 - Listar \n"
          "3 -Sair\n"
          "--------------------")

    while True:
        escolha = int(input("Escolha a opção desejada: "))
        if escolha == 1:
            print('1 - Casdastrar Funcionario\n'
                  '2 - Cadastrar Aluno\n')
            escolha1 = int(input('Escolha qual deseja cadastrar:'))
            if escolha1 == 1:
                geral.funcionario.cadastrar_funcionario()
        elif escolha == 2:
            print('1 - Listar Funcionario\n'
                  '2 - Listar Aluno\n')
            escolha2 = int(input('Escolha qual deseja cadastrar:'))
            if escolha2 == 1:
                geral.funcionario.exibir_funcionario()
            dados.listar_pessoas()
        elif escolha == 3:
            break
        else:
            print("Opção inválida!\n")

print(menu_principal())
