class Endereco:
    def __init__(self, rua, numero, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def mostrar_endereco(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado} - CEP: {self.cep}"


class Aluno:
    def __init__(self, nome, matricula, idade, endereco):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.endereco = endereco

    def mostrar_aluno(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco.mostrar_endereco()}")


class Professor:
    def __init__(self, nome, disciplina, matricula):
        self.nome = nome
        self.disciplina = disciplina
        self.matricula = matricula
        self.escolas = []

    def adicionar_escola(self, escola):
        self.escolas.append(escola)

    def mostrar_escolas(self):
        for escola in self.escolas:
            print(f"- {escola.nome}")


class SalaDeAula:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

    def mostrar_sala(self):
        return f"Sala {self.numero} - capacidade para {self.capacidade} alunos"


class Escola:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.salas = []
        self.professores = []

    def adicionar_sala(self, numero, capacidade):
        sala = SalaDeAula(numero, capacidade)
        self.salas.append(sala)

    def adicionar_professor(self, professor):
        self.professores.append(professor)
        professor.adicionar_escola(self)

    def mostrar_escola(self):
        print(f"Escola: {self.nome}")
        print(f"CNPJ: {self.cnpj}")


# Programa principal

print("=" * 50)
print("SISTEMA DE GERENCIAMENTO DE ESCOLA")
print("=" * 50)


# Escola

escola1 = Escola(
    "Colégio Modelo",
    "12.345.678/0001-90"
)

print("\nDADOS DA ESCOLA")
print("-" * 50)

escola1.mostrar_escola()


# Composição: Escola e SalaDeAula

print("\nCOMPOSIÇÃO - ESCOLA E SALA DE AULA")
print("-" * 50)

escola1.adicionar_sala(101, 30)
escola1.adicionar_sala(102, 35)
escola1.adicionar_sala(103, 40)

print(f"Salas da escola {escola1.nome}:")

for sala in escola1.salas:
    print(f"- {sala.mostrar_sala()}")

print("\nA sala de aula faz parte da escola e seu ciclo de vida")
print("está ligado à escola. Por isso, a relação é uma COMPOSIÇÃO.")


# Associação: Escola e Professor

print("\nASSOCIAÇÃO - ESCOLA E PROFESSOR")
print("-" * 50)

professor1 = Professor(
    "Carlos Oliveira",
    "Programação",
    "P001"
)

professor2 = Professor(
    "Ana Souza",
    "Banco de Dados",
    "P002"
)

escola1.adicionar_professor(professor1)
escola1.adicionar_professor(professor2)

print(f"Professores da escola {escola1.nome}:")

for professor in escola1.professores:
    print(f"- {professor.nome} - {professor.disciplina}")

print("\nProfessor e escola possuem existência independente.")
print("Por isso, a relação é uma ASSOCIAÇÃO.")


# Professor em duas escolas

print("\nPROFESSOR EM MAIS DE UMA ESCOLA")
print("-" * 50)

escola2 = Escola(
    "Escola Estadual Central",
    "98.765.432/0001-10"
)

escola2.adicionar_professor(professor1)

print(f"O professor {professor1.nome} trabalha nas escolas:")

professor1.mostrar_escolas()


# Agregação: Aluno e Endereco

print("\nAGREGAÇÃO - ALUNO E ENDEREÇO")
print("-" * 50)

endereco1 = Endereco(
    "Rua Principal",
    250,
    "Parnaíba",
    "PI",
    "64200-000"
)

aluno1 = Aluno(
    "João Silva",
    "A001",
    20,
    endereco1
)

aluno1.mostrar_aluno()

print("\nO endereço está associado ao aluno, mas pode continuar")
print("existindo mesmo depois que o aluno for removido.")
print("Por isso, a relação é uma AGREGAÇÃO.")


# Demonstrando a agregação

print("\nTESTE DA AGREGAÇÃO")
print("-" * 50)

print("Endereço antes da remoção do aluno:")
print(endereco1.mostrar_endereco())

aluno1 = None

print("\nAluno removido.")

print("O endereço continua disponível:")
print(endereco1.mostrar_endereco())


# Resumo

print("\n" + "=" * 50)
print("RESUMO DOS RELACIONAMENTOS")
print("=" * 50)

print("\nEscola -> SalaDeAula")
print("COMPOSIÇÃO")

print("\nEscola <-> Professor")
print("ASSOCIAÇÃO")

print("\nAluno -> Endereco")
print("AGREGAÇÃO")

print("\n" + "=" * 50)
print("FIM DO PROGRAMA")
print("=" * 50)