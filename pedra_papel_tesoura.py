import random
itens = ("", "pedra", "papel", "tesoura")
comp = random.choice(itens[0])
print('''suas opções:
[ 1 ] pedra
[ 2 ] papel 
[ 3 ] tesoura''')
jog = int(input("qual é a sua jogada?"))
print("-="*30)
print(f"computador jogou: {comp}!!!")
print("-="*30)
print(f"você jogou : {(itens[jog])}!!!")
print("-="*30)
if comp == 1:
    if jog == 1:
        print(" empate!")
    elif jog == 2:
        print("parabéns você ganhou!!!")
    elif jog == 3:
        print("sinto muito você perdeu!!")
    else:
        print("JOGADA INVALIDA!")


if comp == 2:
    if jog == 1:
        print("parabéns você ganhou!!!")
    elif jog == 2:
        print("empate!")
    elif jog == 3:
        print("sinto muito você perdeu!!")
    else:
        print("JOGADA INVALIDA!")


if comp == 3:
    if jog == 1:
        print("sinto muito você perdeu!!")
    elif jog == 2:
        print("parabéns você ganhou!!!")
    elif jog == 3:
        print("empate!")
    else:
        print("JOGADA INVALIDA!")
