import Tutorial.Interfac
import andarone.comandos
import andartwo.comandos
from time import sleep
jogador = dict()


#criando a ficha do jogador (nome, nível, andar e vida)
while True:
    resposta = str(input('Você deseja fazer o tutorial? ')).strip().upper()[0]
    if resposta == 'S':
        nome = Tutorial.Interfac.tutorial(jogador)
        ficha['nome'] =  nome
        break
    if resposta == 'N':
        nome = str(input('Digite o nome do jogador: ')).capitalize().strip()
        jogador['nome'] = nome
        break
    else:
        print('Você precisa digitar "sim" ou "não"')
#primeiro andar que o jogador vai enfrentar
resp = str(input('**Você está na sala A1 do andar 1.**(Pressione ENTER...)'))
acao = andarone.comandos.comandos() 
while True:
    if acao == 'Morreu':
        acao = andarone.comandos.comandos()
    else:
        break
if acao == 'DESLIGAR':
    print('Uri:Obrigado por jogar nosso jogo!')
if acao == 'APROVADO':
    print('Uriu:Parabéns por ter passado para o próximo andar!')
    print('**Você agora está no segundo andar!**')
    sleep(2)
    acao = andartwo.comandos.comandos()
    while True:
        if acao == 'Morreu':
            acao = andarone.comandos.comandos()
        else:
            break
        if acao == 'DESLIGAR':
            print('Uri:Obrigado por jogar nosso jogo!')



