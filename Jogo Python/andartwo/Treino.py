from random import randint
def treino():
    questao = randint(1,8)
    
    if questao == 1:
        resultado = 0
        print('-'*30)
        print('Qual dos ácidos a seguir é o menos volátil?')
        print('-'*20)
        print('1-HCl')
        print('2-HI')
        print('3-H2SO3')
        print('4-H2SO4')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 10
        else:
            print('Você errou!')
            print('A resposta correta era 4')
            print('Você ganhou mais 5 pontos de XP')
            resultado = 5

        return resultado

    if questao == 2:
        resultado = 0
        print('-'*30)
        print('Um comprimido efervescente antiácido é em geral uma mistura sólida de bicarbonato de sódio, carbonato de sódio, ácido cítrico e às vezes ácido acetilsalicílico ou sulfato de magnésio. Ao ser colocado em água, o gás que se desprende durante a efervescência é o:')
        print('-'*20)
        print('1-CO2')
        print('2-OH')
        print('3-H2')
        print('4-CO ')
        print('-'*20)
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

    if questao == 3:
        resultado = 0
        print('-'*30)
        print('A fórmula molecular do ácido cianídrico é: ')
        print('-'*20)
        print('1-HCOOH')
        print('2-HCN')
        print('3-HCNS')
        print('4-HCNO')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 10
        else:
            print('Você errou!')
            print('A resposta correta era 2')
            print('Você ganhou mais 5 pontos de XP')
            resultado = 5


    if questao == 4:
        resultado = 0
        print('-'*30)
        print('Quando se coloca ácido clorídrico sobre uma concha do mar, ela é totalmente dissolvida e há desprendimento de um gás. Esse gás é o mesmo que exalado na respiração animal. Portanto, o sal insolúvel que constitui a carapaça da concha do mar é:')
        print('-'*20)
        print('1-CaSO4')
        print('2-CaCO3')
        print('3-Ca(NO3)2')
        print('4-Ca(OH)2')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 10
        else:
            print('Você errou!')
            print('A resposta correta era 2')
            print('Você ganhou mais 5 pontos de XP')
            resultado = 5


    if questao == 5:
        resultado = 0
        print('-'*30)
        print('Qual o nome do produto de uso doméstico que contém ácido acético?')
        print('-'*20)
        print('1-Vinagre')
        print('2-Detergente')
        print('3-Sabonete')
        print('4-Limpa vidro')
        print('-'*20)
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


    if questao == 6:
        resultado = 0
        print('-'*30)
        print('Uma solução aquosa de H3PO4 é ácida devido à presença de:')
        print('-'*20)
        print('1-água.')
        print('2-hidrogênio.')
        print('3-hidrônio.')
        print('4-fosfato.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 3:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 10
        else:
            print('Você errou!')
            print('A resposta correta era 3')
            print('Você ganhou mais 5 pontos de XP')
            resultado = 5


    if questao == 7:
        resultado = 0
        print('-'*30)
        print('Os ácidos, segundo a teoria de dissociação de Arrhenius, são compostos moleculares que, ao ser dissolvidos em água, geram íons H+(aq). Como é chamado o processo de formação de íons que ocorre quando um ácido é dissolvido em água?')
        print('-'*20)
        print('1-Dissociação iônica.')
        print('2-Ionização.')
        print('3-Eletrólise.')
        print('4-Hidratação.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 10
        else:
            print('Você errou!')
            print('A resposta correta era 2')
            print('Você ganhou mais 5 pontos de XP')
            resultado = 5


    if questao == 8:
        resultado = 0
        print('-'*30)
        print('Entre as afirmativas abaixo, relacionadas com ácidos e bases, a única correta é:')
        print('-'*20)
        print('1- a base conjugada de um ácido forte é base forte;')
        print('2-a base conjugada de um ácido fraco é uma base forte;')
        print('3- um ácido e sua base conjugada reagem para formar sal e água;')
        print('4-o ácido H2O funciona como a sua própria base conjugada;')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você ganhou mais 10 pontos de XP')
            resultado = 10
        else:
            print('Você errou!')
            print('A resposta correta era 2')
            print('Você ganhou mais 5 pontos de XP')
            resultado = 5


       


        return resultado
