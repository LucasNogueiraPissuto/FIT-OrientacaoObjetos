# ATIVIDADE CONTÍNUA 02

# NOMES DOS ALUNOS (máximo 8 alunos)
# ALUNO 1: Caio Vinicius Ferreira Dolci - RA: 2103002
# ALUNO 2: Henrique Nunes de Almeida - RA: 2101824
# ALUNO 3: Leonardo Armejo Gonçalves - RA: 2101893
# ALUNO 4: Lucas Nogueira Pissuto - RA: 2102366
# ALUNO 5: Ryan Ferreira Bissoni - RA: 2102181

def validaMesAno(mes, ano):
    valida_mes = mes >= 1 and mes <= 12
    ano_str = str(ano)
    valida_ano = len(ano_str) == 4
    if valida_mes:
        if valida_ano:
            return True
        else:
            raise ValueError
    else:
        raise TypeError


class Clube:
    def __init__(self):
        self.socios = []

    def associar(self, socio):
        self.socios.append(socio)

    def numero_de_socios(self):
        return len(self.socios)

    def mes_associacao(self, mes, ano):
        if validaMesAno(mes, ano):
            qtd_socios_mes_e_ano = 0
            for socio in self.socios:
                if socio.mes == mes and socio.ano == ano:
                    qtd_socios_mes_e_ano += 1
        return qtd_socios_mes_e_ano

    def expulsar(self, mes, ano):
        if validaMesAno(mes, ano):
            socios_expulsos = []
            cont = 0
            while cont < len(self.socios):
                socio = self.socios[cont]
                if socio.mes == mes and socio.ano == ano:
                    socios_expulsos.append(socio.nome)
                    self.socios.remove(socio)
                    cont -= 1
                cont += 1
        return sorted(socios_expulsos)


class Socio:
    def __init__(self, nome, cpf, nascimento, mes, ano):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.mes = mes
        self.ano = ano
