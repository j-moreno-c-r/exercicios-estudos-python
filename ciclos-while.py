n1 = int(input("digite um valor:"))
n2 = int(input("digite outro valor:"))
escolha = 0
while escolha != 5:
    print('''

     [1] somar 
     [2] multiplicar
     [3] maior
     [4] novos números
     [5] sair do programa''')

    escolha = int(input("escolha uma opção:"))

    if escolha == 1:
        print(f"resultado é:{n1 + n2}")
    elif escolha == 2:
        print(f"o resultado é:{n1 * n2}")
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
            print(f"o maior numero é :{maior}")
        else:
            print("os numeros são iguais")
    elif escolha == 4:
        n1 = int(input("digite um valor:"))
        n2 = int(input("digite outro valor:"))

    else:
        print("=-=" * 10)
print("fim do programa!!!")