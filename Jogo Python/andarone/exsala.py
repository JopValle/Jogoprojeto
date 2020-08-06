def exsala(sala):
    if sala == 'A2':
        resultado = 0
        print('-'*30)
        print('Se o somatório das forças externas sobre um sistema de partículas de massa constante é zero, é CORRETO afirmar ser constante a: ')
        print('-'*20)
        print('1-energia potencial do sistema.')
        print('2-energia mecânica do sistema.')
        print('3-temperatura do sistema.')
        print('4-quantidade de movimento do sistema.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você passou no teste!')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado



    if sala == 'B1':
        resultado = 0
        print('-'*30)
        print('Quando estamos dentro de um carro e o motorista vai fazer uma curva para a direita, nosso corpo imediatamente é prensado para o lado esquerdo do veículo, apontando para fora da trajetória circular feita no momento da curva. Das alternativas abaixo, indique a que explica corretamente a situação descrita. ')
        print('-'*20)
        print('1-Somos lançados para fora da curva por uma força denominada de força centrífuga.')
        print('2-Somos lançados para fora da curva em virtude da inércia.')
        print('3-Somos lançados para fora da curva em virtude de uma força denominada de força centrípeta.')
        print('4-A força gravitacional é responsável por nos empurrar para fora da trajetória.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você passou no teste!')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado

    if sala == 'C1K':
        resultado = 0
        print('-'*30)
        print('Quando o astronauta Neil Armstrong desceu do módulo lunar e pisou na Lua, em 20 de julho de 1969, a sua massa total, incluindo seu corpo, trajes especiais e equipamento de sobrevivência, era de aproximadamente 300 kg. O campo gravitacional lunar é cerca de 1/6 do campo gravitacional terrestre. Se a aceleração da gravidade na Terra é aproximadamente 10,0 m/s2, podemos afirmar que ')
        print('-'*20)
        print('1-A massa total de Armstrong na Lua é de 300 kg e seu peso é 500 N.')
        print('2-A massa total de Armstrong na Terra é de 50,0 kg e seu peso é 3000 N.')
        print('3-A massa total de Armstrong na Terra é de 300 kg e seu peso é 500 N.')
        print('4-A massa total de Armstrong na Lua é de 50,0 kg e seu peso é 3000 N')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 1:
            print('Você acertou!')
            print('Você passou no teste!')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado


    if sala == 'C2':
        resultado = 0
        print('-'*30)
        print('Sobre a superfície da Terra, onde g = 10 m/s2, um astronauta apresenta peso igual a 700 N. Em uma expedição à Lua, onde g = 1,6 m/s2, a massa desse astronauta será igual a: ')
        print('-'*20)
        print('1-70 kg e ele pesará 700 N.')
        print('2-70 kg e ele pesará 112 N.')
        print('3-112 kg e ele pesará 112 N.')
        print('4-112 kg e ele pesará 700 N.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você passou no teste!')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado

    if sala == 'A3K':
        resultado = 0
        print('-'*30)
        print('Um objeto que pesa 650 N na Terra tem peso igual a 1625 N em Júpiter. Determine a gravidade desse planeta, em m/s2, sabendo que a gravidade da Terra é de 10 m/s2. ')
        print('-'*20)
        print('1-15')
        print('2-22')
        print('3-25')
        print('4-28')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 3:
            print('Você acertou!')
            print('Você passou no teste!')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado


    if sala == 'B3':
        resultado = 0
        print('-'*30)
        print('O peso de um corpo é uma grandeza física: ')
        print('-'*20)
        print('1-cuja unidade é medida em quilograma')
        print('2-caracterizada pela quantidade de matéria que o corpo encerra')
        print('3-que mede a intensidade da força de reação de apoio')
        print('4-cuja intensidade é o produto da massa do corpo pela aceleração da gravidade local.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você passou no teste!')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado

    if sala == 'C3K':
        resultado = 0
        print('-'*30)
        print('Assinale a proposição correta: ')
        print('-'*20)
        print('1-a massa de um corpo na Terra é menor do que na Lua')
        print('2-o peso mede a inércia de um corpo')
        print('3-A massa de um corpo na Terra é maior do que na Lua')
        print('4-O sistema de propulsão a jato funciona baseado no princípio da ação e reação.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você passou no teste!')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado


    if sala == 'B2':
        resultado = 0
        print('-'*30)
        print('Um astronauta com o traje completo tem uma massa de 120 kg. Ao ser levado para a Lua, onde a aceleração da gravidade é igual a 1,6m/s2, a sua massa e seu peso serão, respectivamente:')
        print('-'*20)
        print('1-75 kg e 120 N')
        print('2-120 kg e 192 N')
        print('3-192 kg e 192 N')
        print('4-120 kg e 120 N')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você passou no teste!')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado
