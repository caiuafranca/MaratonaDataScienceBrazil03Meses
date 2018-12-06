import random

numero_jogada = int(input('Entre com o Número de jogadas!'))

lampada01 = 0
lampada02 = 0
jogada = 0

for jogada in range(numero_jogada):
  interface = random.randint(0,1)
  if interface == 0:
    lampada01 += 1
  else:
    lampada02 += 1   

print("você tem {} jogadas, advinhe quantas lampadas de cada foram acendidas".format(numero_jogada))
sugestaoLampada01 = int(input('Sugestão lampada 01'))
sugestaoLampada02 = int(input('Sigestão Lampada 02'))

if sugestaoLampada01 == lampada01 and sugestaoLampada02 == lampada02:
  print('Parabens você acertou!')
else:
  print('Desculpe você foi infeliz nas suas escolhas! kkkkkkkkk')
  print("Lampada 01: {}".format(lampada01))
  print("Lampada 02: {}".format(lampada02))


