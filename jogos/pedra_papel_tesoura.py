# pedra_papel_tesoura.py

from random import randint
from time import sleep

def jogar():
    # if (__name__ == "__main__"):
    #     jogar()

    itens = ('Pedra', 'Papel', 'Tesoura')

    computador = randint(0, 2)

    print(''' Suas opcoes:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')

    jogador = int(input('Qual e a sua jogada?'))

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!!')

    print('-=' * 11)

    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')

    print('-=' * 11)

    if computador == 0: #Computador jogou PEDRA
        if jogador == 0:
            print('Empatou!')
        elif jogador == 1:
            print('Jogador ganhou!')
        elif jogador == 2:
            print('Computador ganhou')
        else:
            ('JOGADA INVALIDA!')

    if computador == 1: #Computador jogou PAPEL
        if jogador == 0:
            print('Computador ganhou!')
        elif jogador == 1:
            print('Empatou!')
        elif jogador == 2:
            print('Jogador ganhou!')
        else:
            print('JOGADA INVALIDA')

    if computador == 2: #Computador jogou TESOURA
        if jogador == 0:
            print('Jogador ganhou!')
        elif jogador == 1:
            print('Computador ganhou!')
        elif jogador == 2:
            print('Empatou!')
        else:
            print('JOGADA INVALIDA')
