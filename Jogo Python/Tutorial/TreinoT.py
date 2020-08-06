def TreinoT():
    resultado = 0
    print('-'*30)
    print('Na equação da velocidade V = S/T. O que siginifica "V"? ')
    print('-'*20)
    print('1-Velocidade')
    print('2-Distância')
    print('3-Volume')
    print('4-Tempo')
    print('-'*20)
    print('Uriu:No campo escrito "Resposta" logo abaixo, digite o número que corresponde a resposta desejada')
    resp = int(input('Reposta: '))
    if resp == 1:
        print('Você acertou!')
        print('Você ganhou mais 10 pontos de XP')
        resultado = 10
    else:
        print('Você errou!')
        print('A resposta correta era 1')
        print('Você ganhou mais 5 pontos de XP')
        resultado = 5

    return resultado


