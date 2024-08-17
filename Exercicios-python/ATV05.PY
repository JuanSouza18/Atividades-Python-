#Exercício 2: Fibonacci
#Escreva uma função recursiva que calcula o n-ésimo número da sequência de Fibonacci. A sequência de Fibonacci é uma sequência de números inteiros onde cada número é a soma dos dois números anteriores. A sequência começa com 0 e 1.

#Exemplo da sequência de Fibonacci:

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Exemplo de uso:
print(fibonacci(0))  # Saída: 0
print(fibonacci(1))  # Saída: 1
print(fibonacci(6))  # Saída: 8
print(fibonacci(10)) # Saída: 5
