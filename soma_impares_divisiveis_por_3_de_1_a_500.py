"""faça um programa que calcule a soma entre todos os números impares
   que são multiplos de três e que se encontram no intervalo de 1 a 500"""

sum = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        sum = sum + c
        count += 1

print(f"a soma de {count} requisitados é de {sum}")
