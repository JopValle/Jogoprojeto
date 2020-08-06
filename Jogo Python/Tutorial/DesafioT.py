def desafioT():
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
        print('Você ganhou mais 30 pontos de XP')
        resultado = 30
    else:
        print('Você errou!')
        print('A resposta correta era 1')
        print('Você perdeu um ponto de vida!')
        resultado = 1

    return resultado