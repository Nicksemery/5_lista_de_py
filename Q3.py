# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
# cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

aprovados = 0
alunos_aprovados = []
for alunos in range(1,11):
    notas = []
    print(f'para o aluno {alunos}')
    for nota in range(1,5):
        nota = float(input(f'Nota {nota} '))
        notas.append(nota)
    media = sum(notas)/len(notas)
    print(f'media do aluno {alunos}: {media}')
    if media >= 7.0:
        alunos_aprovados.append(media)

print('total de aprovados:',(len(alunos_aprovados)))