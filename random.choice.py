import random
n1 = str(input("primeira frase: "))
n2 = str(input("segunda frase: "))
n3 = str(input("terceira frase: "))
n4 = str (input("quarta frase:"))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print("a frase escolhida foi: {}".format (escolhido ))