from random import randint
def desafio():
    questao = randint(1,8)
    
    if questao == 1:
        resultado = 0
        print('-'*30)
        print('Os ácidos HClO4, H2MnO4, H3PO3, H4Sb2O7, quanto ao número de hidrogênios ionizáveis, podem ser classificados em: ')
        print('-'*20)
        print('1-monoácido, diácido, diácido, tetrácido.')
        print('2-monoácido, diácido, triácido, tetrácido.')
        print('3-monoácido, diácido, triácido, triácido.')
        print('4-monoácido, monoácido, diácido, triácido.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 1:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 1')
            print('Você perdeu um ponto de vida!')
            resultado = 1

        return resultado

    if questao == 2:
        resultado = 0
        print('-'*30)
        print('Para combater a acidez estomacal causada pelo excesso de ácido clorídrico, costuma-se ingerir um antiácido. Das substâncias abaixo, encontradas no cotidiano das pessoas, a mais indicada para combater a acidez é:')
        print('-'*20)
        print('1-vinagre.')
        print('2-leite de magnésia.')
        print('3-refrigerante.')
        print('4-suco de laranja.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 2')
            print('Você perdeu um ponto de vida!')
            resultado = 1
        return resultado



    if questao == 3:
        resultado = 0
        print('-'*30)
        print('Uma base forte deve ter ligado ao grupo OH-:')
        print('-'*20)
        print('1-um elemento muito eletronegativo.')
        print('2-um elemento muito eletropositivo.')
        print('3-um semimetal.')
        print('4-um metal que dê 3 elétrons.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 2')
            print('Você perdeu um ponto de vida!')
            resultado = 1
        return resultado




    if questao == 4:
        resultado = 0
        print('-'*30)
        print('Átomos neutros de um certo elemento representativo M apresentam dois elétrons em sua camada de valência. As fórmulas corretas para seu óxido normal e brometo são, respectivamente:(Dados: O= 6A e Br = 7A.)')
        print('-'*20)
        print('1-M2O e MBr2')
        print('2-MO2 e MBr2')
        print('3- M2O e MBr')
        print('4-MO e MBr2')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 4')
            print('Você perdeu um ponto de vida!')
            resultado = 1
        return resultado


    if questao == 5:
        resultado = 0
        print('-'*30)
        print('Dadas as espécies químicas a seguir, qual delas pode ser classificada como um ácido de Arrhenius?')
        print('-'*20)
        print('1-HCl')
        print('2-Na2CO3')
        print('3-KOH')
        print('4-Na2O')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 1:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 1')
            print('Você perdeu um ponto de vida!')
            resultado = 1
        return resultado



    if questao == 6:
        resultado = 0
        print('-'*30)
        print('Tendo conhecimento sobre a teoria ácido-base de Lewis e considerando as possíveis reações que podem ocorrer entre as espécies, indique quantas das espécies a seguir agem como um ácido ou uma base:H3O+, H2O, OH– e H+')
        print('-'*20)
        print('1-Dois ácidos e duas bases.')
        print('2-Um ácido e duas bases.')
        print('3-Um ácido e uma base.')
        print('4-Dois ácidos e uma base.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 2')
            print('Você perdeu um ponto de vida!')
            resultado = 1
        return resultado



    if questao == 7:
        resultado = 0
        print('-'*30)
        print('Segundo Brönsted-Lowry, um ácido é uma base conjugada, diferem entre si por:')
        print('-'*20)
        print('1-uma ligação covalente')
        print('2-um par de elétrons')
        print('3-uma hidroxilia')
        print('4-um próton')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 4')
            print('Você ganhou mais 5 pontos de XP')
            resultado = 1
        return resultado



    if questao == 8:
        resultado = 0
        print('-'*30)
        print('“Ácido é uma substância capaz de receber 1 par de elétrons”.A definição acima corresponde à proposta de:')
        print('-'*20)
        print('1-Arrhenius')
        print('2-Brönsted')
        print('3-Lavoisier')
        print('4-Lewis')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 4')
            print('Você ganhou mais 5 pontos de XP')
            resultado = 1
        return resultado

