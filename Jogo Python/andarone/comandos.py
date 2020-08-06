
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
    #salas---------------
    exsalas['A2'] = ''
    exsalas['A1'] = 'OK'
    exsalas['B1'] = ''
    exsalas['C1K'] = ''
    exsalas['C2'] = ''
    exsalas['A3K'] = ''
    exsalas['B3'] = ''
    exsalas['C3K'] = ''
    exsalas['B2'] = ''
    #salas--------------
    ficha['nível'] = 1
    ficha['XP'] = 0
    ficha['vida'] = 5
    ficha['Chaves'] = 0 #número de fragmentos de chave
    contchavecum = 0 #contadores para saber se o jogador já fez o teste de chave daquela sala
    contchavectres = 0
    contchaveatres = 0
    sala = 'A1'
    atual = 'A1'
    while True:
        #análise dos dados do jogador
        if ficha['XP'] >= 100: #analisa se o jogador passou de nível
            ficha['XP'] = 0
            ficha['vida'] += 1
            ficha['nível'] += 1
            resp = str(input('**Você passou de nível!!**(Pressione enter...)'))
            resp = str(input('**Você está no nível {}**(Pressione enter...)'.format(ficha['nível'])))
            resp = str(input('**Você recebeu mais 1(um) de vida**(Pressione enter...)'))
        if ficha['vida'] == 0: #analisa se o jogador está vivo 
            ficha['nível'] = 1
            ficha['XP'] = 0
            ficha['vida'] = 5
            resp = str(input('GAME OVER!')) #fazer o Uriu aparecer e falar que o jogador morreu e dps colocar o que rola
        if ficha['Chaves'] == 3: #caso o jogador tenha os três fragmentos, ele libera a opção do teste de andar
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
                    print('Você foi APROVADO!') #o jogador é aprovado no andar
                    acao = 'APROVADO'
                    break
        else:
            if 'K' in sala: #caso a sala tenha uma chave, o jogador livera a opção para pegar o fragmento
                if sala == 'C3K' and contchaveatres == 0: #isso é para evitar que a mensagem de "tem um fragmento" apareça sem necessidade
                    resp = str(input('**Um fragmento de Chave foi encontrado!**(Pressione enter...)'))
                if sala == 'A3K' and contchaveatres == 0:
                    resp = str(input('**Um fragmento de Chave foi encontrado!**(Pressione enter...)'))
                if sala == 'C1K' and contchavecum == 0:
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
                    if sala == 'A3K':
                        if  contchaveatres == 0: 
                            vida = andarone.Testechave.testechave(sala) #chama o teste de chave
                            if vida == 'OK':
                                ficha['Chaves'] += 1 
                                contchaveatres += 1 #registra que o jogador pegou o fragmento desta sala
                            if vida == 1:
                                ficha['vida'] -= 1
                        else: #caso o jgador tente pegar dois fragmentos de chave na mesma sala
                            resp = str(input('Uriu:Espertinho!Tentou pegar a mesma chave duas vezes!'))
                            resp = str(input('Uriu:Vai perder um ponto de vida para aprender a lição!'))
                            resp = str(input('**Você perdeu um(1) ponto de vida**'))
                            ficha['vida'] -= 1


                    if sala == 'C3K':
                        if  contchavectres == 0:
                            vida = andarone.Testechave.testechave(sala)
                            if vida == 'OK':
                                ficha['Chaves'] += 1 
                                contchavectres += 1
                            if vida == 1:
                                ficha['vida'] -= 1
                        else:
                            resp = str(input('Uriu:Espertinho!Tentou pegar a mesma chave duas vezes!'))
                            resp = str(input('Uriu:Vai perder um ponto de vida para aprender a lição!'))
                            resp = str(input('**Você perdeu um(1) ponto de vida**'))
                            ficha['vida'] -= 1



                    if sala == 'C1K':
                        if contchavecum == 0:
                            vida = andarone.Testechave.testechave(sala)
                            if vida == 'OK':
                                ficha['Chaves'] += 1
                                contchavecum += 1
                            if vida == 1:
                                ficha['vida'] -= 1
                        else:
                            resp = str(input('Uriu:Espertinho!Tentou pegar a mesma chave duas vezes!'))
                            resp = str(input('Uriu:Vai perder um ponto de vida para aprender a lição!'))
                            resp = str(input('**Você perdeu um(1) ponto de vida**'))
                            ficha['vida'] -= 1


            else:
                #menu de ações do jogador (menu normal)
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
            if vida == 30: #vitória no desafio
                ficha['XP'] += vida
                resp = str(input('**Você está com {} de XP agora.**(Pressione enter...)'.format(ficha['XP'])))
            else: #derrota no desafio
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
        if acao == 4: #desliga o jogo em qualquer lugar
            acao = 'DESLIGAR'
            break
        else:
            print('OPS!!Você tentou usar um comando inválido!')


    return acao
