 # Exercício 2

# Crie uma função que receba um dicionario como o de exemplo, de um aluno, e retorne um dict com as seguintes informações:
# - Nota 1
# - Nota 2
# - Nota 3
# - Média

nota1 = float(input('Primeira Nota'))
nota2 = float(input('Segunda Nota '))
nota3 = float(input('Terceira Nota'))
nota4 = float(input('Quarta Nota '))
media = (nota1 + nota2 + nota3 + nota4) /2

print('Tirando {:.1f} ,{:.1f} , {:.1f} e {:.1f} , a media do aluno é {:.1f} '.format(nota1,nota2,nota3,nota4,media))

7.0