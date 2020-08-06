from random import randint
def treino():
    questao = randint(1,8)
    
    if questao == 1:
        resultado = 0
        print('-'*30)
        print('Na equação da velocidade V = S/T. O que siginifica "V"? ')
        print('-'*20)
        print('1-Velocidade')
        print('2-Distância')
        print('3-Volume')
        print('4-Tempo')
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

        return resultado

    if questao == 2:
        resultado = 0
        print('-'*30)
        print('Um bloco de massa 20 kg é puxado horizontalmente por um barbante. O coeficiente de atrito entre o bloco e o plano horizontal de apoio é 0,25. Adota-se g = 10 m/s2. Sabendo que o bloco tem aceleração de módulo igual a 2,0 m/s2, concluímos que a força de tração no barbante tem intensidade igual a:')
        print('-'*20)
        print('1-40N')
        print('2-50N')
        print('3-60N')
        print('4-90N ')
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

    if questao == 3:
        resultado = 0
        print('-'*30)
        print('Calcule a velocidade média de um corpo, em m/s, que percorre uma avenida de 18 km, durante um intervalo de tempo de 6 minutos ')
        print('-'*20)
        print('1-"45m/s"')
        print('2-"50m/s"')
        print('3-"30m/s"')
        print('4-"54m/s"')
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
        print('Um corpo de massa igual a 10 kg move-se pela ação de uma força resultante F, com aceleração de 2,5 m/s². O módulo da força resultante sobre esse corpo deve ser igual a')
        print('-'*20)
        print('1-"4N"')
        print('2-"25N"')
        print('3-"0.25N"')
        print('4-"10N"')
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
        print('Um corpo de 5,0 kg move-se com velocidade de 72 m/h. Determine o módulo de sua energia cinética em Joules.')
        print('-'*20)
        print('1-100J')
        print('2-360J')
        print('3-1000J')
        print('4-20J')
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


    if questao == 6:
        resultado = 0
        print('-'*30)
        print('Para que um corpo extenso se encontre em condição de equilíbrio estático ou cinético é necessário que:')
        print('-'*20)
        print('1-a soma de todos os momentos das forças deve ser nula.')
        print('2-a soma de todas as forças externas deve ser nula.')
        print('3-a soma das forças e a soma dos momentos das forças devem ser nulos.')
        print('4-o centro de massa do corpo deve coincidir com o seu centro geométrico.')
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
        print('Suponha que sobre uma mesa haja um livro. Qual será a força que a mesa exerce sobre o livro, sabendo que a força com que a Terra o atrai é de 10 N?')
        print('-'*20)
        print('1-5N')
        print('2-10N')
        print('3-15N')
        print('4-20N')
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
        print('Indique a alternativa que apresenta unidades que são usadas exclusivamente para a definição de Força:')
        print('-'*20)
        print('1-onça fluida, Joule')
        print('2-Newton, quilograma-força')
        print('3- Newton, quilogrâmetro')
        print('4-grama-força, decímetro')
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
