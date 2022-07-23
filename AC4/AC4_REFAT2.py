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

    def mostrar_info_aluno(self):
        print(f'''
            Código da matrícula: {self.__cod_matricula}
            Data da matrícula: {self.dt_matricula}
            Endereço: {self.__endereco}
            Altura: {self.altura}
            Peso: {self.peso}
            Faltas: {self.faltas}
        ''')

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

    def mostrar_info_instrutor(self):
        print(f'''
            
        ''')


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
        self.aluno = None
        self.aluno_monitor = aluno_monitor

    def mostrar_info_turma(self):
        print(f'''
            Hora da aula: {self.hr_aula}
            Duração da aula: {self.duracao_aula}
            Data de início: {self.dt_inicial}
            Data final: {self.dt_final}
            Atividade: {self.atividade}
            Instrutor: {self.instrutor}
            Aluno monitor: {self.aluno_monitor}
        ''')

    def matricular(self, aluno):
        self.aluno = aluno
        if aluno.get_cod_matricula() in self.alunos:
            print('Aluno ja cadastrado nessa turma')
        else:
            self.alunos[aluno.get_cod_matricula()] = aluno.nome
            print(f'''
                    Aluno do RA {aluno.get_cod_matricula()}
                    matriculado com sucesso
                    na atividade {self.atividade.nome}!
                    ''')
        self.aluno = None

    def alterar_instrutor(self, novo_instrutor):
        self.instrutor = novo_instrutor
        print('Instrutor alterado com sucesso')

    def alterar_aluno_monitor(self, novo_aluno_monitor):
        self.aluno_monitor = novo_aluno_monitor
        print('aluno monitor alterado com sucesso')

    def pesquisar_aluno(self, ra):
        if ra in self.alunos:
            print('Informações do aluno')
            print(f'RA:{ra}')
            print(f'Nome:{self.alunos[ra]}')
            print('\n')
        else:
            print('RA não encontrado')
            print('\n')

    def qtd_alunos(self):
        return len(self.alunos)

    def pesquisar_aluno_monitor(self):
        print(self.aluno_monitor.nome)


atividade1 = Atividade('Aeróbico')
atividade2 = Atividade('Natação')
atividade3 = Atividade('Aula de dança')

aluno1 = Aluno('10660976072', '231975144', 'Lucas', '2002-07-19',
               '11954079052', '1234', '2020-08-07',
               'SC-Araranguá-Jardim Cibeli-Rua Brígida Florisbela Nunes 23',
               '1,80', '70kg')

aluno2 = Aluno('42149898055', '504722797', 'Praga', '2005-07-19',
               '11954079052', '5678', '2020-08-07',
               'SP - São Paulo - Liberdade - Rua da igualdade 49',
               '1,93', '108kg')

aluno3 = Aluno('38469875216', '987463158', 'Hebreuson', '2013-08-15',
               '45687459425', '9745', '2020-06-12',
               'SP - Mauá - Prédinhos - Rua da sorte 1343',
               '1,52', '57kg')

aluno4 = Aluno('74598714731', '914745945', 'Perninha sem freio', '2020-10-12',
               '47412356974', '0157', '2020-06-12',
               'AM - Manaus - Rio Jordão - Rua dos pensos 23',
               '1,30', '114kg')

aluno5 = Aluno('96474563124', '987641354', 'Raoni SYSDBA', '2020-02-28',
               '78964521463', '1333', '2021-01-31',
               'SE - Aracaju - Jacumbira - Rua caiu de que cu 57',
               '1,90', '70kg')

instrutor1 = Instrutor('679.683.250-72', '40.011.971-7', 'Perninha Cielo',
                       '2003-07-19', '16922936841', 'Natação')

instrutor2 = Instrutor('04259108069', '504722797', 'Paulo Montanha',
                       '1995-04-19', '13925537756', 'Musculação')

instrutor3 = Instrutor('45863185365', '97458632', 'Mikale Gloria Deus',
                       '1993-01-03', '94856327854', 'Dança')

turma1 = Turma(15, 180, '2020-03-17', '2020-08-15',
               atividade1, instrutor2, aluno1)

turma2 = Turma(13, 152, '2020-04-23', '2020-08-15',
               atividade2, instrutor1, aluno1)

turma3 = Turma(11, 139, '2020-02-15', '2020-08-15',
               atividade3, instrutor3, aluno1)

turma1.matricular(aluno1)
turma1.matricular(aluno2)

turma1.mostrar_info_turma()

turma1.alterar_aluno_monitor(aluno2)
turma1.alterar_instrutor(aluno2)

print(turma1.alunos)

print(turma1.qtd_alunos())  # Mostrando a qunatidade de aluno na turma 1

turma1.pesquisar_aluno('1234')  # Passando RA valido

turma1.pesquisar_aluno('12345')  # Passando RA INvalido