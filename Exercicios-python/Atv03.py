# Exercício 3 - Foco em funções que retornam mais de um valor

# Crie uma função que receba uma lista de números e retorne o maior e o menor número da lista.

# Exemplo:
# lista = [10, 5, 7, 2, 8, 3]
# maior, menor = maior_menor(lista)]

def maior_menor(lista):
    """
    Recebe uma lista de números e retorna o maior e o menor número dessa lista.
    
    :param lista: Lista de números
    :return: Tupla contendo o maior e o menor número
    """
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    
    maior = max(lista)
    menor = min(lista)
    
    return maior, menor

# Exemplo de uso
lista = [10, 5, 7, 2, 8, 3]
maior, menor = maior_menor(lista)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
