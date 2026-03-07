from functools import reduce
funcionarios = [
    {"nome": "Ana", "cargo": "Desenvolvedora", "salario": 5000},
    {"nome": "Carlos", "cargo": "Analista", "salario": 3500},
    {"nome": "Marcos", "cargo": "Gerente", "salario": 8000},
    {"nome": "Julia", "cargo": "Suporte", "salario": 2500}
]

valor_x = 4000
total_bonus = 0

for funcionario in funcionarios:
    if funcionario["salario"] > valor_x:
        bonus = funcionario["salario"] * 0.10
        total_bonus = total_bonus + bonus

        print("Funcionário:", funcionario["nome"])
        print("Salário:", funcionario["salario"])
        print("Bônus:", bonus)
        print()

print("Total gasto com bônus:", total_bonus)