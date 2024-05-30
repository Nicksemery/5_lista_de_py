# use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e
# pergunte quais seus números favoritos. Use seus nomes para serem as chaves de cada número
# favorito. Ao final, exiba o nome de cada pessoa e seu número favorito.

dicio = {"Marina":13,
        "Alan":33,
        "Tiago":7,
        "Victor":90,
        "Vlad":88}
for info in dicio:
    print(f'{info}, seu numero favorito é {dicio[info]}')
