from random import randint
from operator import itemgetter
esc1 = randint(1,6)
esc2 = randint(1,6)
esc3 = randint(1,6)
esc4 = randint(1,6)
jogadores = {"jog1":esc1 ,"jog2":esc2,"jog3":esc3,"jog4":esc4}
print("valores sorteados:")
ranking = list()
for k, v in jogadores.items():
  print(f"{k} tirou {v} no dado.")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True )
print("=:"*30)

#print(ranking)
for i,  v in enumerate(ranking):
  print(f"{i+1}º lugar: {v[0]} com {v[1]}")