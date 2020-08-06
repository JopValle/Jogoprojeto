def exsala(sala):
    if sala == 'A2':
        resultado = 0
        print('-'*30)
        print('Um ácido de Lewis deve ter:')
        print('-'*20)
        print('1-hidrogênio ionizável')
        print('2-baixa densidade eletrônica')
        print('3-larga densidade eletrônica')
        print('4-baixa densidade eletrônica')
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



    if sala == 'B1K':
        resultado = 0
        print('-'*30)
        print('Ag+ é um ácido: ')
        print('-'*20)
        print('1-de Brönsted')
        print('2-de Lewis')
        print('3-de Arrhenius')
        print('4-Ag+ não é um ácido.')
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

    if sala == 'C1':
        resultado = 0
        print('-'*30)
        print('NH3 é uma base:')
        print('-'*20)
        print('1-de Lewis')
        print('2- de Arrhenius')
        print('3-de Brönsted')
        print('4-nas três teorias')
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


    if sala == 'C2K':
        resultado = 0
        print('-'*30)
        print('As chuvas ácidas podem ter diferentes composições dependendo do local onde são formadas, as mais nocivas são formadas em grandes centros industriais, onde há queima de combustíveis fósseis (gasolina, óleo diesel). Esse tipo de chuva é carregado de poluentes, marque a opção que traz os compostos que a torna nociva à saúde. ')
        print('-'*20)
        print('1-óxidos de carbono (CO, CO2)')
        print('2-óxidos de enxofre (SO2, SO3)')
        print('3- óxidos de cálcio (CaO, CaO2)')
        print('4-óxidos de nitrogênio (NO, NO2).')
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

    if sala == 'A3':
        resultado = 0
        print('-'*30)
        print('Entre os oxiácidos HF, H3BO3, HclO3 e HMnO4, a ordem crescente de força para esses compostos é: ')
        print('-'*20)
        print('1-HClO3,HMnO4, HF e H3BO3')
        print('2-H3BO3, HClO3, HF e HMnO4')
        print('3-H3BO3, HF, HclO3e HMnO4')
        print('4-HMnO4 , HClO3, H3BO3e HF')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 3:
            print('Você acertou!')
            print('Você foi aprovado no teste!')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado


    if sala == 'B3K':
        resultado = 0
        print('-'*30)
        print('Considerando os oxiácidos H2SO3, HClO3 e HClO, podemos dizer que a ordem decrescente de ionização é: ')
        print('-'*20)
        print('1-HClO, H2SO3 e HClO3')
        print('2-HClO3, HClO e H2SO3')
        print('3-HClO, HClO3 e H2SO3 ')
        print('4-HClO3, H2SO3 e HClO')
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

    if sala == 'C3':
        resultado = 0
        print('-'*30)
        print('Após a ionização de um ácido em água, observou-se que o número de moléculas ionizadas era o triplo do número de moléculas não ionizadas. Com base nessa observação, a porcentagem de ionização do referido ácido era:')
        print('-'*20)
        print('1-26%')
        print('2- 40%')
        print('3-70%')
        print('4-75%')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 4:
            print('Você acertou!')
            print('Você ganhou mais 30 pontos de XP')
            resultado = 30 #retorna o ganho em xp
        else:
            print('Você errou!')
            print('Você perdeu um(1) ponto de vida')
            resultado = 1 #retorna um ponto a menos de vida
        return resultado


    if sala == 'B2':
        resultado = 0
        print('-'*30)
        print('Qual das alternativas a seguir indica somente ácidos inorgânicos:')
        print('-'*20)
        print('1-HCl, H2SO4, CH3CH2COOH.')
        print('2-HF, HCN, H2CO3.')
        print('3- H2S, CH3CH2OH, HMnO4.')
        print('4-HI, HClO4, HCNS.')
        print('-'*20)
        resp = int(input('Reposta: '))
        if resp == 2:
            print('Você acertou!')
            print('Você passou no teste!')
            resultado = 'APROVADO'
        else:
            print('Você errou!')
            print('Você perdeu um ponto de vida')
            resultado = 1
        return resultado