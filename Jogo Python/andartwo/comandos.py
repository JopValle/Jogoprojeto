
import andarone.Treino
import andarone.Desafio
import andarone.Testedesala
from time import sleep
import andarone.Testechave
import andarone.testedeandar
import andarone.exsala
def comandos():
    exsalas = dict()
    ficha = dict()
    exsalas['A2'] = ''
    exsalas['A1'] = 'OK'
    exsalas['B1'] = ''
    exsalas['C1K'] = ''
    exsalas['C2'] = ''
    exsalas['A3K'] = ''
    exsalas['B3'] = ''
    exsalas['C3K'] = ''
    exsalas['B2'] = ''
    ficha['nível'] = 1
    ficha['XP'] = 0
    ficha['vida'] = 5
    ficha['Chaves'] = 0
    contchavebum = 0
    contchavecdois = 0
    contchavebtres = 0
    sala = 'A1'
    atual  = 'A1'
    while True:
        #análise dos dados do jogador
        if ficha['XP'] >= 100: #analisa se o jogador passou de nível
            ficha['XP'] = 0
            ficha['vida'] += 1
            ficha['nível'] += 1
            resp = str(input('**Você passou de nível!!**(Pressione enter...)'))
            resp = str(input('**Você está no nível {}**(Pressione enter...)'.format(ficha['nível'])))
            resp = str(input('**Você recebeu mais 1(um) de vida**(Pressione enter...)'))
        if ficha['vida'] == 0:
            ficha['nível'] = 1
            ficha['XP'] = 0
            ficha['vida'] = 5
            resp = str(input('GAME OVER!')) #fazer o Uriu aparecer e falar que o jogador morreu e dps colocar o que rola
        if ficha['Chaves'] == 3:
            sleep(2)
            print('-'*20)
            print('Você está na sala {}{}'.format(sala[0], sala[1]))
            print('-'*20)
            print('1-Treino')
            print('2-Desafio')
            print('3-Teste da sala')
            print('4-Sair do jogo')
            print('5-Teste de Andar')
            print('-'*20)
            print('O que você deseja fazer?')
            acao = int(input('Movimento: '))
            if acao == 5:
                vida = andarone.testedeandar.testedeandar()
                if vida == 1:
                    ficha['vida'] -= 1
                else:
                    print('Você foi APROVADO!')
                    acao = 'APROVADO!'
                    break
        else:
            if 'K' in sala:
                if sala == 'B1K' and contchavebum == 0:
                    resp = str(input('**Um fragmento de Chave foi encontrado!**(Pressione enter...)'))
                if sala == 'C2K' and contchavecdois == 0:
                    resp = str(input('**Um fragmento de Chave foi encontrado!**(Pressione enter...)'))
                if sala == 'B3K' and contchavebtres == 0:
                    resp = str(input('**Um fragmento de Chave foi encontrado!**(Pressione enter...)'))
                sleep(2)
                print('-'*20)
                print('Você está na sala {}{}'.format(sala[0], sala[1]))
                print('-'*20)
                print('1-Treino')
                print('2-Desafio')
                print('3-Teste da sala')
                print('4-Sair do jogo')
                print('5-Teste de Chave')
                print('-'*20)
                print('O que você deseja fazer?')
                acao = int(input('Movimento: '))
                if acao == 5:
                    if sala == 'B3K':
                        if  contchavebtres == 0:
                            vida = andarone.Testechave.testechave(sala)
                            if vida == 'OK':
                                ficha['Chaves'] += 1 
                                contchavebtres += 1
                            if vida == 1:
                                ficha['vida'] -= 1
                        else:
                            resp = str(input('Uriu:Espertinho!Tentou pegar a mesma chave duas vezes!'))
                            resp = str(input('Uriu:Vai perder um ponto de vida para aprender a lição!'))
                            resp = str(input('**Você perdeu um(1) ponto de vida**'))
                            ficha['vida'] -= 1


                    if sala == 'C2K':
                        if  contchavecdois == 0:
                            vida = andarone.Testechave.testechave(sala)
                            if vida == 'OK':
                                ficha['Chaves'] += 1 
                                contchavecdois += 1
                            if vida == 1:
                                ficha['vida'] -= 1
                        else:
                            resp = str(input('Uriu:Espertinho!Tentou pegar a mesma chave duas vezes!'))
                            resp = str(input('Uriu:Vai perder um ponto de vida para aprender a lição!'))
                            resp = str(input('**Você perdeu um(1) ponto de vida**'))
                            ficha['vida'] -= 1



                    if sala == 'B1K':
                        if contchavebum == 0:
                            vida = andarone.Testechave.testechave(sala)
                            if vida == 'OK':
                                ficha['Chaves'] += 1
                                contchavebum += 1
                            if vida == 1:
                                ficha['vida'] -= 1
                        else:
                            resp = str(input('Uriu:Espertinho!Tentou pegar a mesma chave duas vezes!'))
                            resp = str(input('Uriu:Vai perder um ponto de vida para aprender a lição!'))
                            resp = str(input('**Você perdeu um(1) ponto de vida**'))
                            ficha['vida'] -= 1


            else:
                #menu de ações do jogador 
                sleep(2)
                print('-'*20)
                print('Você está na sala {}{}'.format(sala[0], sala[1]))
                print('-'*20)
                print('1-Treino')
                print('2-Desafio')
                print('3-Teste da sala')
                print('4-Sair do jogo')
                print('-'*20)
                print('O que você deseja fazer?')
                acao = int(input('Movimento: '))


        if acao == 1: #estrutura do treino
            sleep(1)
            xp = andarone.Treino.treino() #verificar se posso juntar essa linha com a linha de baixo
            ficha['XP'] = ficha['XP'] + xp
            resp = str(input('**Você está com {} de XP agora.**(Pressione enter...)'.format(ficha['XP'])))
            acao = 0
        if acao == 2: #estrutura do desafio
            sleep(1)
            vida = andarone.Desafio.desafio()
            if vida == 30:
                ficha['XP'] += vida
                resp = str(input('**Você está com {} de XP agora.**(Pressione enter...)'.format(ficha['XP'])))
            else:
                ficha['vida'] -= vida
                resp = str(input('**Você está com {} de vida agora**(Pressione enter...)'.format(ficha['vida'])))
            acao = 0
        if acao == 3: #troca de sala feita pelo jogador
            sleep(1)
            atual = sala
            sala = andarone.Testedesala.teste(sala)
            if exsalas[sala] != 'OK':
                vida = andarone.exsala.exsala(sala)
                if vida == 1:
                    ficha['vida'] -= vida
                    sala = atual
                else:
                    exsalas[sala] = 'OK'
            acao = 0
        if acao == 4:
            acao = 'DESLIGAR'
            break
        else:
            print('OPS!!Você tentou usar um comando inválido!')


    return acao
