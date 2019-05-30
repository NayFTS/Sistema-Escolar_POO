import dados
import pickle
class pessoa:
    def __init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo):
        self._nome = nome
        self._rg = rg
        self._cpf = cpf
        self._anoNasc = anoNasc
        self._mesNasc = mesNasc
        self._diaNasc = diaNasc
        self._sexo = sexo

    def __new__(cls, *args, **kwargs):
        """previne a classe de ser instanciada diretamente"""
        if cls is pessoa:
            raise TypeError("classe não pode ser instanciada.")
        return object.__new__(cls, *args, **kwargs)

    def __str__(self):
        return f'{self._nome}; RG: {self._rg}'


class funcionario(pessoa):
    def __init__(self):
        super().coletar_dados(nome, rg, cpf, anoNasc, mesNasc, diaNasc)
        self._matricula = matricula
        self._setor = setor
        self._cargo = cargo
        self._nivel = nivel

    def cadastrar_funcionario():
        try:
            with open('dados_pessoas') as pessoas:
                antigos_funcionarios = pickle.load(pessoas)
            with open('dados_pessoas', mode='wb') as dados_pessoas:
                antigos_funcionarios.append(coletar_informacoes())
                novos_funcionarios = pickle.dumps(antigos_funcionarios)
                dados_funcionarios.write(novos_funcionarios)
        except:
            with open('dados_pessoas', mode='wb') as dados_pessoas:
                novos_funcionarios = [dados.cadastrar_pessoas()]
                pessoas = pickle.dumps(novos_funcionarios)
                dados_funcionarios.write(pessoas)

    def exibir_funcionario(self):
        try:
            with open('dados_pessoas', mode='rb') as dados_pessoas:
                lista_funcionarios = pickle.load(dados_pessoas)
                print('pessoas\n')
                for funcionario in lista_funcionarios:
                    print(funcionario['name'])
            print('-' * 20)
        except:
            print('Não encontrado!')
            menu_principal()


class coordenador_adm(funcionario):
    def __init__(self):
        self.__area = area
        self.__plusSalario = plusSalario

    def cadastrar_coordenadoradm(self):
        try:
            with open('dados_pessoas') as pessoas:
                antigos_funcionarios = pickle.load(pessoas)
            with open('dados_pessoas', mode='wb') as dados_pessoas:
                antigos_funcionarios.append(coletar_informacoes())
                novos_funcionarios = pickle.dumps(antigos_funcionarios)
                dados_funcionarios.write(novos_funcionarios)
        except:
            with open('dados_pessoas', mode='wb') as dados_pessoas:
                novos_funcionarios = [dados.cadastrar_pessoas()]
                pessoas = pickle.dumps(novos_funcionarios)
                dados_funcionarios.write(pessoas)

    def exibir_coordenadoradm(self):
        try:
            with open('dados_pessoas', mode='rb') as dados_pessoas:
                lista_funcionarios = pickle.load(dados_pessoas)
                print('pessoas\n')
                for funcionario in lista_funcionarios:
                    print(funcionario['name'])
            print('-' * 20)
        except:
            print('Não encontrado!')
            menu_principal()


    def calcularPlusSalario(self):
        pass


class aluno(pessoa):
    def __init__(self):
        self._codigo = codigo
        self._interesse = interesse
        self._desconto = desconto
        self.matricula = matricula

    def cadastrar_aluno():
        try:
            with open('dados_pessoas') as pessoas:
                antigos_alunos = pickle.load(pessoas)
            with open('dados_pessoas', mode='wb') as dados_pessoas:
                antigos_alunos.append(coletar_informacoes())
                novos_alunos = pickle.dumps(antigos_alunos)
                dados_alunos.write(novos_alunos)
        except:
            with open('dados_pessoas', mode='wb') as dados_pessoas:
                novos_alunos = [coletar_informacoes()]
                pessoas = pickle.dumps(novos_alunos)
                dados_pessoas.write(aluno)

    def exibir_alunos(self):
        pass

    def exibir_aluno_por_matricula(self, matricula):
        pass


class professor():
    def __init__(self):
        super.col
        self.formacao = formacao
        self.nivel = nivel
        self.disciplina = disciplina

    def cadastrar_professor():
        try:
            with open('dados_pessoas') as pessoas:
                antigos_professores = pickle.load(pessoas)
            with open('dados_pessoas', mode='wb') as dados_pessoas:
                antigos_professores.append(coletar_informacoes())
                novos_professores = pickle.dumps(antigos_fprofessores)
                dados_professores.write(novos_professores)
        except:
            with open('dados_pessoas', mode='wb') as dados_pessoas:
                novos_professores = [dados.cadastrar_pessoas()]
                pessoas = pickle.dumps(novos_professores)
                dados_professores.write(pessoas)

    def exibir_professores(self):
        try:
            with open('dados_pessoas', mode='rb') as dados_pessoas:
                lista_professores = pickle.load(dados_pessoas)
                print('pessoas\n')
                for professor in lista_professores:
                    print(professor['nome'])
            print('-' * 20)
        except:
            print('Não encontrado!')
            menu_principal()


class coordenador_professor(professor):
    def __init__(self):
        self.__area = area
        self.__plusSalario = plusSalario

    def cadastrar_coordenadoraprofessor(self):
        pass

    def exibir_coordenadorprofessor(self):
        pass

    def calcularPlusSalario(self):
        pass


class matricula:
    def __init__(self):
        self.id = id
        self.mesMatricula = mesMatricula
        self.anoMatricula = anoMatricula


class curso:
    def __init__(self):
        self.titulo = titulo
        self.descricao = descricao
        self.valor = valor
        self.sala = sala
        self.matricula = matricula
        self.professor = professor

    def cadastrar_curso(self):
        pass

    def exibir_cursos(self):
        pass

    def calcular_minimo_alunos(self):
        pass



