def teste(sala):
    if sala == 'A1': #esquema de sala com duas op
        print('-'*20)
        print('Você está na sala A1')
        print('Escolha para qual sala você deseja ir:')
        print('1-B1')
        print('2-A2')
        resposta = int(input('Digite aqui: '))
        if resposta == 1:
            sala = 'B1'
        if resposta == 2:
            sala = 'A2'
        return sala
    if sala == 'B1': #esquema de sala com 3 op
        print('-'*20)
        print('Você está na sala B1')
        print('Escolha para qual sala você deseja ir:')
        print('1-C1')
        print('2-B2')
        print('3-A1')
        resposta = int(input('Digite aqui: '))
        if resposta == 1:
            sala = 'C1K' #sala que possúi uma chave
        if resposta == 2:
            sala = 'B2'
        if resposta == 3:
            sala = 'A1'
        return sala
    if sala == 'C1K':
        print('-'*20)
        print('Você está na sala C1')
        print('Escolha para qual sala você deseja ir:')
        print('1-B1')
        print('2-C2')
        resposta = int(input('Digite aqui: '))
        if resposta == 1:
            sala = 'B1'
        if resposta == 2:
            sala = 'C2'
        return sala
    if sala == 'A2': #esquema de sala com 3 op
        print('-'*20)
        print('Você está na sala A2')
        print('Escolha para qual sala você deseja ir:')
        print('1-A1')
        print('2-B2')
        print('3-A3')
        resposta = int(input('Digite aqui: '))
        if resposta == 1:
            sala = 'A1'
        if resposta == 2:
            sala = 'B2'
        if resposta == 3:
            sala = 'A3K'
        return sala
    if sala == 'C2': #esquema de sala com 3 op
        print('-'*20)
        print('Você está na sala C2')
        print('Escolha para qual sala você deseja ir:')
        print('1-C1')
        print('2-C3')
        print('3-B2')
        resposta = int(input('Digite aqui: '))
        if resposta == 1:
            sala = 'C1'
        if resposta == 2:
            sala = 'C3K'
        if resposta == 3:
            sala = 'B2'
        return sala
    if sala == 'A3K': #esquema de sala com duas op
        print('-'*20)
        print('Você está na sala A3')
        print('Escolha para qual sala você deseja ir:')
        print('1-B3')
        print('2-A2')
        resposta = int(input('Digite aqui: '))
        if resposta == 1:
            sala = 'B3'
        if resposta == 2:
            sala = 'A2'
        return sala
    if sala == 'B3': #esquema de sala com 3 op
        print('-'*20)
        print('Você está na sala B3')
        print('Escolha para qual sala você deseja ir:')
        print('1-A3')
        print('2-C3')
        print('3-B2')
        resposta = int(input('Digite aqui: '))
        if resposta == 1:
            sala = 'A3K'
        if resposta == 2:
            sala = 'C3K'
        if resposta == 3:
            sala = 'B2'
        return sala
    if sala == 'C3K': #esquema de sala com duas op
        print('-'*20)
        print('Você está na sala C3')
        print('Escolha para qual sala você deseja ir:')
        print('1-B3')
        print('2-C2')
        resposta = int(input('Digite aqui: '))
        if resposta == 1:
            sala = 'B3'
        if resposta == 2:
            sala = 'C2'
        return sala
    if sala == 'B2': #esquema de sala com 4 op
        print('-'*20)
        print('Você está na sala B2')
        print('Escolha para qual sala você deseja ir:')
        print('1-A2')
        print('2-C2')
        print('3-B1')
        print('4-B3')
        resposta = int(input('Digite aqui: '))
        if resposta == 1:
            sala = 'A2'
        if resposta == 2:
            sala = 'C2'
        if resposta == 3:
            sala = 'B1'
        if resposta == 4:
            sala = 'B3'
        return sala
