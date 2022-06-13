# forca.py

def jogar():

    if (__name__ == "__main__"):
        jogar()

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "MELANCIA".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        mensagem_ganhador()
    else:
        mensagem_perdedor()

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

def mensagem_ganhador():
    print("Voce ganhou!!")

def mensagem_perdedor():
    print("Voce perdeu!!")


# def jogar():
#     print("*********************************")
#     print("***Bem vindo ao jogo da Forca!***")
#     print("*********************************")

#     palavra_secreta = "maça".upper()
#     letras_acertadas = ["_", "_", "_", "_"]


#     erros = 0
#     print(len(palavra_secreta))
#     print(letras_acertadas)

#     while(True):

#         chute = input("Qual letra? ")
#         chute = chute.strip().upper()

#         if(chute in palavra_secreta):
#             index = 0
#             for letra in palavra_secreta:
#                 if(chute == letra):
#                     letras_acertadas[index] = letra
#                 index += 1
#         else:
#             erros += 1

#         if (erros == 6):
#             break
#         if ("_" not in letras_acertadas):
#             break
#         print(letras_acertadas)


#     if("_" not in letras_acertadas):
#         print("Você ganhou!!")
#     else:
#         print("Você perdeu!!")
#     print("Fim do jogo")