"""\faça um programa que mostra na tela um contagem regressiva
para o estouro de fogos de artificio. indo de 10 até 0, com uma pausa de
1 segundo entre eles."""

import time
for c in range(10, -1, -1):
    time.sleep(1.0)
    print(c)
print("happy new year")
