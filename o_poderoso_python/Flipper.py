l = int(input())
r = int(input())

if l == 0 and r == 0:
  print('Bolinha caiu na porta A')
elif l == 0 and r == 1:
  print('Bolinha caiu na porta B')
else:
  print('Bolinha caiu na porta C')