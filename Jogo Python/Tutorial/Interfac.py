import Tutorial.TreinoT
import Tutorial.DesafioT
import Tutorial.TestedesalaT
import Tutorial.Chave
def tutorial(ficha):
    ficha['vida'] = 5
    vida = 0
    ficha.clear
    nome = str(input('Digite o nome do jogador: ')).capitalize().strip()
    resp = str(input('Pressione "Enter" para continuar...'))
    resp = str(input('**Enquanto alguns estudam para o vestibular...**'))
    resp = str(input('**Outro estudam para subir o mais alto possivel na Grande Torre...**'))
    resp = str(input('**Você será capaz de chegar até o topo?**'))
    resp = str(input('Desconhecido:Bem vindo à Torre, {}!'.format(nome)))
    resp = str(input('**Você abre os olhos mas não encherga nada. Apenas uma completa escuridão e um vazio sem fim.**'))
    resp = str(input('**É possivel ver apenas uma pequena esfera de luz que vem em sua direção.Crescendo cada vez mais...**'))
    resp = str(input('Desconhecido:Meu nome é Uriu e eu estou aqui para guia-lo no início da sua escalada na Torre.'))
    resp = str(input('**A esfera de luz para de se mover e fica estática na sua frente...**'))
    resp = str(input('Uriu:Vou te ensinar o básico para subir a Torre e te ajudarei a entender o sistema daqui.'))
    resp = str(input('Uriu:Vamos começar logo!'))
    resp = str(input('Uriu:Os andares das Torres são divididos em salas, que juntas formam um quadrado 3x3.'))
    resp = str(input('Uriu:As salas possuem alguns tipos de treinos e alguns desafios que lhe ajudarão a estudar e ganhar experiência(XP).'))
    resp = str(input('Uriu:O XP serve para você passar de nível e assim ganhar mais vida.'))
    resp = str(input('Uriu:Eu montei um andar bônus para que você possa aprender antes de subir a Torre.'))
    print('-'*20)
    print('1-Treino')
    print('2-Desafio')
    print('3-Teste da sala')
    print('-'*20)
    resp = str(input('Uriu:Este é o seu menu de ações("Enter" para continuar...)'))
    resp = str(input('Uriu:Nele você pode escolher que ação deseja tomar em cada andar.'))
    resp = str(input('Uriu:Vamos começar com uma Treino'))
    print('Uriu:Digite "1" para iniciar um treino')
    resp = str(input('Digite aqui: '))
    ficha['XP'] = Tutorial.TreinoT.TreinoT()
    if ficha['XP'] == 10:
        resp = str(input('Uriu:Muito bem!'))
        resp = str(input('Uriu:Você conseguiu vencer o primeiro treino!'))
        resp = str(input('Uriu:Os treinos são perguntas mais fáceis para você ganhar XP e aprender algumas coisas.'))
        resp = str(input('Uriu:Fique tranquilo se você falhar nos treinos.'))
        resp = str(input('Uriu:Os treinos não irão fazer com que você perca vida, mas caso falhe, ganhará menos XP'))
    else:
        resp = str(input('Uriu:Que pena que não conseguiu!'))
        resp = str(input('Uriu:Fique tranquilo.'))
        resp = str(input('Uriu:Os treinos não fazem você perder pontos de vida.'))
        resp = str(input('Uriu:Mas caso você conclua-os com exito, você receberá mais pontos de XP.'))
    print('-'*20)
    print('Uriu:Voltando ao menu de ações')
    print('-'*20)
    print('1-Treino')
    print('2-Desafio')
    print('3-Teste da sala')
    print('-'*20)
    resp = str(input('Uriu:Agora vamos fazer um desafio'))
    resp = str(input('Uriu:Digite o número 2 para iniciar um desafio'))
    resp = int(input('Digite aqui: '))
    vida = Tutorial.DesafioT.desafioT()
    if vida  == 1:
        ficha['vida'] = ficha['vida'] - vida
        resp = str(input('**Você possúi {} pontos de vida**'.format(ficha['vida'])))
        vida = 0
        print('Uriu:Foi por pouco!')
        resp = str(input('Uriu:Falhar em um desafio significa perder pontos de vida!'))
        resp = str(input('Uriu:Mas caso venha a acerta-los, receberá muito mais XP do que nos treinos.'))
    else:
        ficha['XP'] = ficha['XP'] + Tutorial.DesafioT.desafioT()
        vida = 0
        print('Uriu:Muito bem!')
        resp = str(input('Uriu:Sabia que você ia se sair bem no desafio!'))
        resp = str(input('Uriu:Ao ganhar um desafio você receberá mais XP do que em um treino.'))
        resp = str(input('Uriu:Mas tenha cuidado. Falhar em um desafio fará com que você perca pontos de vida!'))
    print('-'*20)
    resp = str(input('Uriu:Agora no menu de ações, vamo selecionar a opção "Teste de sala".'))
    print('-'*20)
    print('1-Treino')
    print('2-Desafio')
    print('3-Teste da sala')
    print('-'*20)
    resp = int(input('Digite aqui:'))
    resp = str(input('Uriu:Os testes de sala permitem que você abra as portas das salas adjacentes.'))
    resp = str(input('Uriu:Com as portas abertas você poderá ir e retornar livremente para as salas com as portas destrancadas.'))
    resp = str(input('Uriu:Mas para destranca-las você precisa ser bem sucedido no teste.'))
    vida = Tutorial.TestedesalaT.testedesala()
    if vida == 1:
        ficha['vida'] = ficha['vida'] - 1
        resp = str(input('**Você possúi {} pontos de vida**'.format(ficha['vida'])))
        vida = 0
        print('Uriu:Foi por pouco!')
        resp = str(input('Uriu:Não se preocupe, eu abrirei a porta para você.'))
    else:
        print('Uriu:Parabéns!')
        resp = str(input('Uriu:Você agora pode ir para a próxima sala'))
        resp = str(input('Uriu:Sempre que você passar no teste de sala, você será levado para a próxima sala'))
        resp = str(input('Uriu:Na Torre você poderá escolher para qual sala você quer se mover.'))
    resp = str(input('**Seu persoangem se dirige a uma porta para passar para a próxima sala**'))
    resp = str(input('Uriu:Esta é nossa última parada antes de você começar a subir a Torre.'))
    resp = str(input('Uriu:Veja seu meno de ações novamente.'))
    print('-'*20)
    print('1-Treino')
    print('2-Desafio')
    print('3-Teste da sala')
    print('4-Teste de chave')
    print('-'*20)
    resp = str(input('Uriu:Veja que há uma nova opção no seu menu'))
    resp = str(input('Uriu:A opção de teste de andar é liberada quando você entra em uma sala que possúi uma das chaves do andar. '))
    resp = str(input('Uriu:Selecione a opção "Tesde de chave".'))
    resp = int(input('Digite aqui:'))
    vida = Tutorial.Chave.testechave()
    if vida == 1:
        ficha['vida'] = ficha['vida'] - vida
        resp = str(input('**Você possúi {} pontos de vida**'.format(ficha['vida'])))
        vida = 0
        resp = str(input('Uriu:Foi por pouco!'))
        resp = str(input('Uriu:Mesmo você tendo falhado, lhe darei a chave como um presente meu para você'))
        resp = str(input('Uriu:Normalmente nos testes de chave, você receberá um gragmento da chave do andar'))
        resp = str(input("**Você recebeu uma chave!!**"))
    else:
        resp = str(input('Uriu:Parabén por ter sido aprovado no teste da chave!'))
        resp = str(input('Uriu:Normalmente nos testes de chave, você receberá um gragmento da chave do andar'))
        reps = str(input('Uriu:Como estamos em treinamento, lhe darei os outros fragmentos da chave'))
        resp = str(input('**Você recebeu outros 2 gragmentos de chave!**'))
    resp = str(input('Uriu:Agora você está pronto para subir a Torre!'))
    resp = str(input('Uriu:Eu restaurei todos os seus status de jogo, agora você está no nível 1.'))


    


    return nome
