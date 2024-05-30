# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []

for idade in range(1,31):
    idade = int(input(f'Qual idade do aluno {idade}? '))
    idades.append(idade)

for altura in range(1,31):
    altura = float(input(f"Qual altura do aluno {altura}? "))
    alturas.append(altura)

altura_media = sum(alturas)/len(alturas)

abaixo = 0
for idade, altura in zip(idades, alturas):
    if idade >13 and altura < altura_media:
        abaixo =+ 1
print("alunos abaixo da media de altura pela idade:", abaixo)
        