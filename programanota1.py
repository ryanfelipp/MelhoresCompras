nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media = (nota1+nota2+nota3)/3

if media <=10 and media >= 7:
    print("Aluno Aprovado!")
else:
    exame = float(input('Digite a nota do exame: '))
    media = (media + exame)/2
    if media >= 5:
        print("Aluno Aprovado!")
    else:
        print('Aluno de DP')

