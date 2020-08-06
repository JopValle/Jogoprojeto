def testedeandar():
    resultado = 0
    print('-'*30)
    print('Um bloco de massa 50 Kg é empurrado sobre uma superfície horizontal por uma força F = 220 N. Sabendo que o coeficiente de atrito cinético (μc) entre o bloco e a superfície é igual a 0,2, calcule a aceleração sofrida pelo bloco.')
    print('-'*20)
    print('1-2,2m/s²')
    print('2-2,4m/s²')
    print('3-2,6m/s²')
    print('4-2,8m/s²')
    print('-'*20)
    resp = int(input('Reposta: '))
    if resp == 2:
        print('Você acertou!')
        print('Você passou no teste!')
        resultado = 'APROVADO'
    else:
        print('Você errou!')
        print('Você perdeu um ponto de vida!')
        resultado = 1
    return resultado

