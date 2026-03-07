from functools import reduce

https://github.com/Francisco-alt-coder/Algoritmo-Em-Paradigma/commits/main
funcionarios = [
    {"nome": "Ana", "cargo": "Desenvolvedora", "salario": 5000},
    {"nome": "Carlos", "cargo": "Analista", "salario": 3500},
    {"nome": "Marcos", "cargo": "Gerente", "salario": 8000},
    {"nome": "Julia", "cargo": "Suporte", "salario": 2500}
]

valor_x = 4000

# Organizar os funcionários que ganham acima do valor X
filtrados = list(filter(lambda f: f["salario"] > valor_x, funcionarios))

# Calcular bônus de cada individuo que recebe acima do valor X
bonus = list(map(lambda f: f["salario"] * 0.10, filtrados))

# Somar todos os bônus utilizando reduce
total_bonus = reduce(lambda total, b: total + b, bonus, 0)

print("Funcionários que recebem bônus:")
for f in filtrados:
    print(f["nome"], "-", f["salario"])

print("Total gasto com bônus:", total_bonus)