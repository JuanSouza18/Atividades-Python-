# Exercício 1

# Crie um programa que leia o nome e a idade de 3 alunos e mostre a média de idade deles.
# 
# Use o diciionário abaixo de teste

alunos = [
    {
        "nome": "João",
        "idade": 20
    },
    {
        "nome": "Maria",
        "idade": 22
    },
    {
        "nome": "José",
        "idade": 21
    }
]
# Inicializar a variável para somar as idades
soma_idades = 0

# Contar o número de alunos
num_alunos = len(alunos)

# Somar as idades
for aluno in alunos:
    soma_idades += aluno["idade"]

# Calcular a média
media_idade = soma_idades / num_alunos

# Mostrar o resultado
print(f"A média de idade dos alunos é: {media_idade:.2f}")
