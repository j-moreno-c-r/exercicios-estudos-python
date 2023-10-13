n1 = float(input("digite a sua nota de teste(0-10):"))
n2 = float(input("digite sua nota de prova(0-10):"))
m = (n1+n2)/2
print("a sua média foi:{}".format(m))
if m >= 6.0:
  print("párabens nota azul!!!")
if m >= 8.0:
  print("párabens nota exemplar!!!")
if m < 6.0:
  print("sinto muito reprovado!!! ESTUDE MAIS !!!")
else:
  print("você digitou uma nota invalida.")