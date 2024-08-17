#Exercício 3: Fatorial
# Escreva uma função recursiva que calcula o fatorial de um número

def fatorial(n):
    # Caso base: fatorial de 0 é 1
    if n == 0:
        return 1
    # Chamada recursiva: n * fatorial de (n-1)
    else:
        return n * fatorial(n - 1)

#Testando a função
print(fatorial(5))  # Saída: 120
