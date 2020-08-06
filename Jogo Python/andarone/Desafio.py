from random import randint
def desafio():
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
            print('Você ganhou mais 30 pontos de XP')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('A resposta correta era 1')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida

        return resultado

    if questao == 2:
        resultado = 0
        print('-'*30)
        print('Um móvel em M.R.U gasta 10h para percorrer 1100 km com velocidade constante. Qual a distância percorrida após 3 horas da partida?')
        print('-'*20)
        print('1-"2"')
        print('2-"1"')
        print('3-"0"')
        print('4-"triangulo"')
        print('-'*20)
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




    if questao == 3:
        resultado = 0
        print('-'*30)
        print('Uma corrente consistindo de sete anéis, cada um de massa 200 gramas, está sendo puxada verticalmente, para cima, com aceleração constante de 2,0 m/s². A força para cima no anel do meio é:')
        print('-'*20)
        print('1-16,8N')
        print('2-9,6N')
        print('3-8,4N')
        print('4-2,4N')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você ganhou mais 30 pontos de XP')
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
        print('Um homem tenta levantar uma caixa de 5kg, que está sobre uma mesa, aplicando uma força vertical de 10N. Nessa situação, o valor da força que a mesa aplica na caixa é: (g=10m/s2).')
        print('-'*20)
        print('1-0N')
        print('2-5N')
        print('3- 10N')
        print('4-40N')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você ganhou mais 30 pontos de XP')
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
        print('Dentro de um elevador, um objeto de peso 100 N está apoiado sobre uma superfície. O elevador está descendo e freando com aceleração vertical e para cima de 0,1 m/s2. Considere a aceleração da gravidade como 10 m/s2. Durante o tempo de frenagem, a força que sustenta o objeto vale, em newtons:')
        print('-'*20)
        print('1-101')
        print('2-99')
        print('3-110')
        print('4-90')
        print('-'*20)
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



    if questao == 6:
        resultado = 0
        print('-'*30)
        print('Um objeto, que se desloca horizontalmente com velocidade v0, é submetido à ação de uma força constante de intensidade F que o acelera, levando-o a atingir a velocidade v em um intervalo de tempo t. Nessas condições, é correto afirmar que a massa do objeto vale:')
        print('-'*20)
        print('1-(v – v0) ÷ F.t')
        print('2-F.t ÷ (v – v0)')
        print('3-F.(v – v0) ÷ t')
        print('4-(F – v) ÷ v0.t')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você ganhou mais 30 pontos de XP')
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
        print('Existem dispositivos que podem ser utilizados para medir a intensidade de uma força, como o:')
        print('-'*20)
        print('1-decibelímetro')
        print('2-manômetro')
        print('3-termômetro')
        print('4-dinamômetro')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você ganhou mais 30 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 4')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1
        return resultado



    if questao == 8:
        resultado = 0
        print('-'*30)
        print('De acordo com a Dinâmica, dizemos que um corpo está em equilíbrio quando:')
        print('-'*20)
        print('1-sua velocidade é nula')
        print('2-seu movimento é retilíneo')
        print('3-sua aceleração é constante')
        print('4-sua aceleração é nula')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você ganhou mais 30 pontos de XP')
            resultado = 30
        else:
            print('Você errou!')
            print('A resposta correta era 4')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1

        return resultado


