from os import system
from time import sleep
from random import randint

def titulo():
    print('--'*20)
    print(f"{'Jogo do galo':^40}")
    print('--'*20)
    print()

def limparTabuleiro(tabuleiro):
    '''
    -> Função que limpa o tabuleiro após um jogo
    '''
    tam = len(tabuleiro)
    for l in range(0,tam):
        for c in range(0,tam):
            tabuleiro[l][c] = ' '

def Menu():

    '''
        -> Função que mostra na tela as opções que o utilizador tem
        -> O utilizador pode escolher jogar com outro jogadro (Humanos)
        -> O utilizador também pode escolher jogar contra a máquina
        -> ou simplesmente sair do programa.
    
    '''
    print('--'*20)
    print('[1] - Himano vs Humano')
    print('[2] - Humano vs Máquina')
    print('[3] - Sair')
    print('--'*20)

def contador(tabuleiro):
    '''
        -> Função contador que conta a quantidade de X e O dentro do tabuleiro
        -> return: Retorna a soma entre x e o se o valor desse retorno for 9 então houve um empate
    '''
    x = 0
    o = 0
    for l in range(3):
        for c in range(3):
            if tabuleiro[l][c] == 'X':
                x+=1
            elif tabuleiro[l][c] == 'O':
                o+=1
    return (x+o)

def mostrarTabuleiro(tabuleiro):
    '''
        Função que mostra o tabuleiro na tela
    '''
    tam = len(tabuleiro)
    print(' 1    2    3')
    for l in range(0,tam):
        if l >= 0:
            print(f'{"--"}'*7,l+1,end=' ')
        print()
        for c in range(0,tam):
            if c < tam:
                print(f'{tabuleiro[l][c]} | ',end=' ')
        print()
   
def validarJogada(linha,coluna, tabuleiro):

    '''
        -> Função que valida a jogada antes de preencher algum espaço no tabuleiro
        -> primeiro verifica se os números estão no intervalo de 1 e 3
        -> Depois verifica se já existe alguma jogada no espaço onde o jogador quer jogar
        -> return: False para jogada inválida True para jogada válida
    '''
    if linha > 3 or linha < 1 or coluna > 3 or coluna < 1:
        return False
    elif tabuleiro[linha-1][coluna-1] !=' ':
        return False
    return True

def vencedor(tabuleiro,simbolo):
    '''
        Função vencedor verifica se há um vencedor por linhas,
        por coluna ou pelas duas diagonais
    '''
    valores = [0,0,0]
    diag = 0
    diagSeg = 2

    if tabuleiro[0].count(simbolo) == 3 or tabuleiro[1].count(simbolo) == 3 or tabuleiro[2].count(simbolo) == 3:
        return 1
    elif contador(tabuleiro) == 9:
        return 0
    else:

        for c in range(3):
            if tabuleiro[c][0] == simbolo:
                valores[0] += 1
            if tabuleiro[c][1] == simbolo:
                valores[1] += 1
            if tabuleiro[c][2] == simbolo:
                valores[2] += 1

        for l in range(0,3):
            for c in range(0,3):
                if l == c:
                    if tabuleiro[l][c] == simbolo:
                        diag += 1
        if diag == 3:
            return 1
        for l in range(0,3):
            if tabuleiro[l][diagSeg] == simbolo:
                diagSeg -= 1

        if diagSeg == -1:
            return 1
        if 3 in valores:
            return 1
        
tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
simbolo = ''
vez = 0

Menu()
opc = int(input("Escolha uma opção: "))

match (opc):
    case 1:
        while True:
            titulo()
            mostrarTabuleiro(tabuleiro)
            if vez % 2 == 0:
                simbolo = 'X'
            else:
                simbolo = 'O'

            print(f'Vez do jogador <{simbolo}>')
            linha = int(input(('Escolha a linha: ')))
            coluna = int(input("Escolhe a coluna: "))
            
            if not validarJogada(linha,coluna,tabuleiro):
                print('Jogada inválida, faça uma jogada válida')
                sleep(1)
                continue
            else:
                tabuleiro[linha-1][coluna-1] = simbolo
            
            if vencedor(tabuleiro,simbolo) == 1:
                system('cls')
                mostrarTabuleiro(tabuleiro)
                print(f"\033[32m O jogador <{simbolo}> ganhou \033[m")
                if input("Quer jogar novament?[S/N]: ") in 'nN':
                    break
                else: limparTabuleiro(tabuleiro)

            if vencedor(tabuleiro,simbolo) == 0:
                system('cls')
                mostrarTabuleiro(tabuleiro)
                print('\032[33m < EMPATE > \033[m')
                if input("Quer jogar novament?[S/N]: ") in 'nN':
                    break
                else: limparTabuleiro(tabuleiro)
            vez += 1
            system('cls')
    case 2:
        while True:
            titulo()
            mostrarTabuleiro(tabuleiro)
            if vez % 2 == 0:
                simbolo = 'X'
                linha = int(input(('Escolha a linha: ')))
                coluna = int(input("Escolhe a coluna: "))
            else:
                simbolo = 'O'
                linha = randint(0,3)
                coluna = randint(0,3)
        
            if not validarJogada(linha,coluna,tabuleiro):
                print('Jogada inválida, faça uma jogada válida')
                sleep(1)
                continue
            else:
                tabuleiro[linha-1][coluna-1] = simbolo
            
            if vencedor(tabuleiro,simbolo) == 1:
                system('cls')
                mostrarTabuleiro(tabuleiro)
                print(f"\033[32m O jogador <{simbolo}> ganhou \033[m")
                
                if input("Quer jogar novament?[S/N]: ") in 'nN':
                    break
                else: limparTabuleiro(tabuleiro)

            if vencedor(tabuleiro,simbolo) == 0:
                system('cls')
                mostrarTabuleiro(tabuleiro)
                print('\032[33m < EMPATE > \033[m')

                if input("Quer jogar novament?[S/N]: ") in 'nN':
                    break
                else: limparTabuleiro(tabuleiro)
            vez += 1
            system('cls')

