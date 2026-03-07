from import math 
class Funcionario:

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

# Pagamento de bônus para funcionários que ganham acima de um valor X
class FolhaPagamento:

    def __init__(self, funcionarios):
        self.funcionarios = funcionarios

    def calcular_bonus_total(self, valor_x):
        total = 0

        for funcionario in self.funcionarios:
            if funcionario.salario > valor_x:
                bonus = funcionario.calcular_bonus()
                total += bonus

                print("Funcionário:", funcionario.nome)
                print("Salário:", funcionario.salario)
                print("Bônus:", bonus)
                print()

        return total


funcionarios = [
    Funcionario("Ana", "Desenvolvedora", 5000),
    Funcionario("Carlos", "Analista", 3500),
    Funcionario("Marcos", "Gerente", 8000),
    Funcionario("Julia", "Suporte", 2500)
]

folha = FolhaPagamento(funcionarios)

total = folha.calcular_bonus_total(4000)

print("Total gasto com bônus:", total)