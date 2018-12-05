A = int(input())
B = int(input())
C = int(input())


if A != B and A != C:
  print("o Jogador A Ganhou!")
elif B != A and B != C:
  print("o Jogador B Ganhou!")
elif C != A and C != B:
  print("o Jogador C Ganhou!")  
else:
  print("o Game Empatou")

