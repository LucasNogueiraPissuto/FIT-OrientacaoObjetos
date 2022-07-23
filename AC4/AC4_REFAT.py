from abc import ABC


class Pessoa(ABC):
    def __init__(self, cpf, rg, nome, data_nascimento, telefone):
        self.__cpf = cpf
        self.__rg = rg
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_rg(self):
        return self.__rg

    def set_rg(self, rg):
        self.__rg = rg


class Atividade():
    def __init__(self, nome):
        self.nome = nome


class Aluno(Pessoa):
    def __init__(self, cpf, rg, nome, data_nascimento, telefone,
                 cod_matricula, dt_matricula, endereco, altura, peso):
        super().__init__(cpf, rg, nome, data_nascimento, telefone)
        self.__cod_matricula = cod_matricula
        self.dt_matricula = dt_matricula
        self.__endereco = endereco
        self.altura = altura
        self.peso = peso
        self.faltas = 0

    def get_cod_matricula(self):
        return self.__cod_matricula

    def set_codigo_matricula(self, codigo_matricula):
        self.__cod_matricula = codigo_matricula

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def adc_faltas(self, qtd_faltas):
        self.faltas += qtd_faltas


class Instrutor(Pessoa):
    def __init__(self, cpf, rg, nome, data_nascimento,
                 telefone, especialidade):
        super().__init__(cpf, rg, nome, data_nascimento, telefone)
        self.especialidade = especialidade


class Turma():
    def __init__(self, hr_aula, duracao_aula, dt_inicial, dt_final, atividade,
                 instrutor, aluno_monitor):
        self.alunos = {}
        self.hr_aula = hr_aula
        self.duracao_aula = duracao_aula
        self.dt_inicial = dt_inicial
        self.dt_final = dt_final
        self.atividade = atividade
        self.instrutor = instrutor
        self.aluno = ''
        self.aluno_monitor = aluno_monitor

    def matricular(self, aluno):
        self.aluno = aluno
        if self.aluno.get_cod_matricula in self.alunos:
            print('Aluno ja cadastrado nessa turma')
        else:
            self.alunos[self.aluno.get_cod_matricula()] = self.aluno.nome
            print(f'''Aluno do RA {self.aluno.get_cod_matricula()}
                    matriculado com sucesso
                    na atividade {self.atividade.nome}!
                    ''')

    def pesquisar_aluno(self, ra='', nome_aluno=''):
        if ra == '' and nome_aluno == '':
            print('Pelo menos um dos parametros precisa ser preenchido')
        elif ra != '':
            if ra in self.alunos:
                print('Informações do aluno')
                print(f'RA:{ra}')
                print(f'Nome:{self.alunos[ra]}')
            else:
                print('RA não encontrado')
        else:
            if nome_aluno in self.alunos.values():
                print('Informações dos alunos correspondentes')
                for item in self.alunos:
                    if nome_aluno == self.alunos.values():
                        print(self.alunos)

    def qtd_alunos(self):
        return len(self.alunos)

    def pesquisar_aluno_monitor(self):
        print(self.aluno_monitor.nome)


atividade1 = Atividade('Zumba')
atividade2 = Atividade('Natação')

aluno1 = Aluno('44360151810', '556585586', 'Lucas', '19/07/2002',
               '11954079052', '1234', '07/08/2020', 'Ruada igualdade 39',
               '1,80', '70kg')

aluno2 = Aluno('1234567', '12365667', 'Praga', '19/07/2005',
               '11954079052', '5678', '07/08/2020', 'Ruada igualdade 49',
               '1,80', '70kg')

instrutor1 = Instrutor('1234567', '1234567', 'Carlos Alberto de Nobrega', 
                       '19/07/2003', '1195462080', 'Natação')

turma1 = Turma(15, 180, '15-02-2020', '15-08-2020',
               atividade1, instrutor1, aluno1)

turma1.matricular(aluno1)
turma1.matricular(aluno2)

print(turma1.alunos)

print(turma1.qtd_alunos())

turma1.pesquisar_aluno('', 'Lucas')
