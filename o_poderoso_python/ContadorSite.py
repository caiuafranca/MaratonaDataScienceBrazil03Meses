dias = int(input())
acessos = []
i = 0
while i < dias:
  acessos.append(int(input()))
  i += 1
dia  = 0
soma = 0
for i in acessos:
  soma += i
  dia += 1
  if soma >= 1000000:
    print("No {} dia, foi batido a meta dos 1000000 acessos!".format(dia))
    break


