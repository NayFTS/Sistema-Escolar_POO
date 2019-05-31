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
        if cls is pessoa:
            raise TypeError("classe não pode ser instanciada.")
        return object.__new__(cls, *args, **kwargs)


class funcionario(pessoa):
    def __init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)
        self._matricula = matricula
        self._setor = setor
        self._cargo = cargo
        self._nivel = nivel
        Funcionario = [str(input('Nome:')), str(input('RG:')), str(input('CPF:')),
                       int(input('Ano de Nascimento')), int(input('Mes de Nascimento')),
                       int(input('Dia de Nascimento')), str(input('Sexo:')),
                    int(input('matricula')), str(input('setor')), str(input('cargo')),
                    int(input('nivel'))]


    def cadastrar_funcionario(Funcionario):
        pass
    def exibir_funcionario(self):
        pass

    def salario(self):
        self.salarioBruto = ''
        self.salarioLiquido = ''
        self.inss = ''
        self.irff = ''
        self.planoSaude = ''

    def calcularSalario(self):
        pass

class coordenadorAdmin(funcionario):
    def __init__(self, nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo, area, plusSalario):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, matricula, setor, cargo)
        self.area = area
        self.plusSalario = plusSalario
