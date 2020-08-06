def testedeandar():
    resultado = 0
    print('-'*30)
    print('O ácido fórmico, oficialmente conhecido como ácido metanoico, de fórmula bruta CH2O2, é o responsável pela irritação causada na pele humana, provocada pela picada das formigas. Qual das substâncias abaixo poderia ser aplicada na pele a fim de atenuar esse efeito irritante por neutralização?')
    print('-'*20)
    print('1-Mg(OH)2 ')
    print('2-C2H5 - OH')
    print('3- NH4Cl')
    print('4-H3PO4')
    print('-'*20)
    resp = int(input('Reposta: '))
    if resp == 1:
        print('Você acertou!')
        print('Você passou no teste!')
        resultado = 'APROVADO'
    else:
        print('Você errou!')
        print('Você perdeu um ponto de vida')
        resultado = 1
    return resultado

