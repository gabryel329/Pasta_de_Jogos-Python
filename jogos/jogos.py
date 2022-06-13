#  jogos.py


import adivinhacacao_teste
import forca
import pedra_papel_tesoura

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Pedra_Papel_Tesoura")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print ("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print ("Jogando adivinhacao")
        adivinhacacao_teste.jogar()
    elif (jogo == 3):
        print("Jogando pedra_papel_tesoura")
        pedra_papel_tesoura.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()