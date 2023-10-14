def area():
  l = int(input("largura em metros: "))
  c = int(input("comprimento em metros: "))
  s = l * c
  print(f"a área das medidas recebida é de : {float(s)}m²")


def linha():
  print("=:"*25)


#programa principal
linha()
print("programa de medição de terrenos.")
linha()
area()
linha()