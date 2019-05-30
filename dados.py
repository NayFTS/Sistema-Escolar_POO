import pickle
import geral

def coletar_informacoes():
    nome = str(input('Nome: '))
    rg = int(input('Rg:'))
    cpf = int(input('cpf: '))
    anoNasc = int(input('anoNasc: '))
    mesNasc = input('mesNasc: ')
    diaNasc = input('Dia_Nascimento: ')

    dados = dict(name=nome, rg=rg, cpf=cpf, anoNasc=anoNasc, mesNasc=mesNasc, diaNasc=diaNasc)

    return dados


def cadastrar_pessoas():
    try:
        with open('dados_pessoas') as pessoas:
            antigos_pessoas = pickle.load(pessoas)
        with open('dados_pessoas', mode='wb') as dados_pessoas:
            antigos_pessoas.append(coletar_informacoes())
            novos_pessoas = pickle.dumps(antigos_pessoas)
            dados_pessoas.write(novos_pessoas)
    except:
        with open('dados_pessoas', mode='wb') as dados_pessoas:
            novos_pessoas = [coletar_informacoes()]
            pessoas = pickle.dumps(novos_pessoas)
            dados_pessoas.write(pessoas)


def listar_pessoas():
    try:
        with open('dados_pessoas', mode='rb') as dados_pessoas:
            lista_pessoas = pickle.load(dados_pessoas)
            print('pessoas\n')
            for pessoa in lista_pessoas:
                print(pessoa['name'])
        print('-' * 20)
    except:
        print('Não encontrado!')
        menu_principal()

def salario(funcionario):
    if geral.funcionario(nivel) == 'A':
        salario = 1520.25
    elif geral.funcionario(nivel) == 'B':
        salario = 2362.67
