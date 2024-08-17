#Exercício 4: Andando em uma lista encadeada
#Dada o nó inicial, escreva uma função recursiva que imprime todos os elementos da lista.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(node):
    if node is None:
        return
    print(node.data)
    print_list(node.next)

# Criando uma lista encadeada: 1 -> 2 -> 3 -> 4 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

#Imprimindo a lista encadeada
print_list(head)
