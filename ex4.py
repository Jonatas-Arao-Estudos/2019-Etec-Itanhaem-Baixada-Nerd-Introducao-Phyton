prova1 = float(input('Digite o valor da nota da 1ª prova: '))
prova2 = float(input('Digite o valor da nota da 2ª prova: '))
prova3 = float(input('Digite o valor da nota da 3ª prova: '))

media = (prova1 + prova2 + prova3) /3

if float(media) >= 7:
    print('\nVocê foi aprovado!')
else:
    exame = float(input('\nDigite o valor da nota do exame: '))
    mediaEM = (media + exame)/2
    if float(mediaEM)>=5:
        print('\nVocê foi finalmente aprovado!')
    else:
        print('\nVocê foi definitivamente reprovado!')    
