boletim = []

def coletar_nota(qtd_notas):
    for i in range (1,4):
        nota = float(input(f'Digite a sua {i} nota: '))
        while nota >10 or nota< 0:
            nota = float(input(f'Nota Invalida a sua {i} nota: '))
        boletim.append(nota)
    print(f"Suas notas foram\n{boletim}")

coletar_nota(3)   

media = (boletim[0]+boletim[1]+boletim[2])/3

if media <=10 and media >= 7:
    print("Aluno Aprovado!")
else:
    exame = float(input('Digite a nota do exame: '))
    media = (media + exame)/2
    if media >= 5:
        print("Aluno Aprovado!")
    else:
        print('Aluno de DP')

